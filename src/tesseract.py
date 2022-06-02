import re 
import argparse
import subprocess

def extract_ocr_tesseract(file):
    '''Extract the output of Tesseract OCR from an image into a txt file'''
    subprocess.run(["tesseract", file, f"{file.split('.')[0]}"])
    return file.split('.')[0]+'.txt'


def get_id_with_tesseract(file):
    '''Extract the ID of the receipt thanks to the txt path of the output of Tesseract OCR'''
    with open(file, 'r') as f:
        document = f.read()
    f.close()
    for line in document.split('\n'):
        pattern = '.*(\d[A-Z].\d{3,3}.\d{3,3}.\d{4,4}.\d).*'
        res = re.search(pattern, line)
        if res:
            id = res.group(1)
            return id


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-png', help='path to text file')

    args = parser.parse_args()

    txt = extract_ocr_tesseract(args.png)
    id = get_id_with_tesseract(txt)
    print('The ID is: ', id)