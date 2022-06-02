import argparse
from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse

def get_number_pages(input):
    '''Get the number of pages of a PDF'''
    inputpdf = PdfFileReader(open(input, "rb"))
    return inputpdf.numPages


def split_pdf(input):
    '''Split a PDF into as many PDF as its number of pages'''
    inputpdf = PdfFileReader(open(input, "rb"))
    outputspdf = []
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(f"{input.split('.')[0]}_page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)
            outputspdf.append(f"{input.split('.')[0]}_page%s.pdf" % i)
    return outputspdf


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-input', help='file path of PDF', required=True)

    args = parser.parse_args()

    split_pdf(args.input)