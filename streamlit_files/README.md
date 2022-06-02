# Folder to host temporary files

This folder hosts all temporary files when running the streamlit app:
- the uploaded file is stored in this folder
- the file is then split into one PDF for every page, which are saved in the folder
- each PDF file is then converted to a PNG image, which are saved in the folder
- each image is then processed by Tesseract and renamed according to the ID of the receipt

Once the zip file has been downloaded, all the data in the folder is deleted.