## Pipeline of ID extraction and PDF downloading

> This GitHub repository is linked to a [deployed Streamlit app](https://share.streamlit.io/thomasmonnier/ocr_id_receipts/main/app.py). It uses Tesseract OCR to extract the information from the scanned receipts.

## Quick start

This shows how to use the app.

### 0. Link to the Streamlit App

> Go to [the app](https://share.streamlit.io/thomasmonnier/ocr_id_receipts/main/app.py).

### 1. Upload a PDF file

> Upload a PDF file containing one or multiple pages. Each page must have only one receipt (*accusé de réception*).

### 2. Get the IDs

> Click on the button **Get the IDs**.

This process will be launched:
- the PDF file is split into as many PDF as there are pages
- the PDF files are converted to PNG images
- The images are rotated according to the sense of the scan thanks to Tesseract OSD
- The images are parsed by Tesseract OCR
- The images are renamed according to the ID extracted thanks to a REGEXP
- The images without IDs are not renamed

### 3. Download the ZIP file

> Click on **Download** to download all the renamed images into a folder called *streamlit_files*

## Run locally the app

It is possible to run locally the app (in order to make changes to the app for example):
- Clone [the GitHub repository](https://github.com/ThomasMonnier/ocr_id_receipts)
- Create a virtual environment: `python3 -m venv env`
- Activate the virtual environment: `source env/bin/activate`
- Install the apt get pacakges according to your environment (MacOs, Linux, Windows) from `packages.txt`
- Install the pip packages: `pip install -r requirements.txt`
- Run the app: `streamlit run app.py`
- See your app running on: `http://localhost:8051` if the 8501 port is not already been occupied, otherwise +1

> Every changes that you make while running the app locally will be automacally applied: no need to kill and re-run the app

## Commit changes

> If you commit changes to this repository, the deployed app will be refreshed automatically by Streamlit.