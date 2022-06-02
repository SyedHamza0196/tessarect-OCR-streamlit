from zipfile import ZipFile

def create_zip_file(zip_name, files_path):
    '''Create a zip file with a list of file paths'''
    # create a ZipFile object
    zipObj = ZipFile(zip_name, 'w')
    # Add multiple files to the zip
    for file in files_path:
        zipObj.write(file)
    # close the Zip File
    zipObj.close()