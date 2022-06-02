# Import packages
import streamlit as st
import cv2
from pathlib import Path
import shutil
import os
import glob

# Import modules
from src.split_pdf import get_number_pages, split_pdf
from src.pdf_to_png import Convertor
from src.zip_files import create_zip_file
from src.tesseract import extract_ocr_tesseract, get_id_with_tesseract
from src.detect_orientation import detect_orientation
from src import st_stdout


def read_file(file, name):
    with open(f"streamlit_files/{name}", "wb") as buffer:
        shutil.copyfileobj(file, buffer)


def download_zip(zip_file):
    with open('streamlit_files/receipts.zip', 'rb') as f:
        st.download_button('Download Zip', f, file_name=zip_file)


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


def main():    
    st.markdown('# Use the App')
    file_uploaded = st.file_uploader("Choose a file", type=["pdf"])

    response = st.button("Get the IDs")

    if response:
        filename = file_uploaded.name
        read_file(file_uploaded, filename)

        file_path = f"streamlit_files/{filename}"

        if get_number_pages(file_path) > 1:
            with st_stdout('code'):
                print('The PDF has multiple pages. It will be split and then processed.')
            files_path = split_pdf(file_path)
        else:
            files_path = [file_path]

        all_ids = []
        for file in files_path:
            convertor = Convertor(file, file.split('.')[0])
            convertor.convert_to_png_fitz()
            if convertor.pages == 1:
                with st_stdout('success'):
                    for png_path in convertor.outputs:
                        detect_orientation(png_path)
                        txt_path = extract_ocr_tesseract(png_path)
                        id = get_id_with_tesseract(txt_path)
                        if id == None:
                            # it probably means that the image has been rotated in the wrong sense
                            # so rotate it from bottom to top
                            detect_orientation(png_path, 180)
                            txt_path = extract_ocr_tesseract(png_path)
                            id = get_id_with_tesseract(txt_path)
                        print('File is: ', file.split('/')[-1], '\n')
                        print('The ID is: ', id, '\n')

                        if id == None:
                            all_ids.append(png_path.split('.')[0].split('/')[1])
                        else:
                            all_ids.append(id)
                            os.rename(png_path, f'streamlit_files/{id}.png')

            else:
                with st_stdout('error'):
                    print('The file has not been splitted correctly.')
        
        create_zip_file('streamlit_files/receipts.zip', [f'streamlit_files/{id}.png' for id in all_ids])
        download_zip('receipts.zip')

        files = glob.glob('streamlit_files/*')
        for f in files:
            os.remove(f)
    
    st.markdown('# Documentation')
    intro_markdown = read_markdown_file("README.md")
    st.markdown(intro_markdown, unsafe_allow_html=True)


if __name__=="__main__":
    main()