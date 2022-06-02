from pdf2image import convert_from_path
import argparse
import fitz

class Convertor:
    def __init__(self, pdf, png):
        self.pdf = pdf
        self.png = png
        self.outputs = []
        self.pages = int

    def convert_to_png(self):
        '''to use locally'''
        pages = convert_from_path(self.pdf, 500)
        self.pages = len(pages)
        for iter, page in enumerate(pages):
            page.save(self.png+f'_page{iter}.png', 'PNG')
            self.outputs.append(self.png+f'_page{iter}.png')

    def convert_to_png_fitz(self):
        '''to use with streamlit'''
        dpi = 500
        zoom = dpi / 72
        magnify = fitz.Matrix(zoom, zoom)
        doc = fitz.open(self.pdf)
        self.pages = len(doc)
        for page in doc:
            pix = page.get_pixmap(matrix=magnify)
            pix.save(self.png+f'_page{iter}.png')
            self.outputs.append(self.png+f'_page{iter}.png')


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-pdf', help='input file path of PDF', required=True)
    parser.add_argument('-png', help='output file path of PNGs', required=True)

    args = parser.parse_args()
    convertor = Convertor(args.pdf, args.png)

    convertor.convert_to_png()