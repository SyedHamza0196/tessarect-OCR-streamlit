import argparse
import pytesseract
import imutils
import cv2

def detect_orientation(img, orientation=None):
    '''Loads an image, detects the orientation of the text thanks to Tesseract OSD, and downloads the image rotated'''
    # load the input image via open-cv
    image = cv2.imread(img)
    # and use Tesseract to determine the text orientation
    results = pytesseract.image_to_osd(img, config='--psm 0 -c min_characters_to_try=5')
    # display the orientation information
    results = results.replace('\n', ' ').split(' ')
    rotate = 0
    for i, elem in enumerate(results):
        if elem == 'Rotate:':
            rotate = int(results[i+1])
    
    # rotate the image to correct the orientation
    if orientation == None:
        rotated = imutils.rotate_bound(image, angle=rotate)
        cv2.imwrite(f"{img}", rotated)
    else:
        rotated = imutils.rotate_bound(image, angle=orientation)
        cv2.imwrite(f"{img}", rotated)


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-png", required=True, help="path to input image")

    args = parser.parse_args()
    detect_orientation(args.png)