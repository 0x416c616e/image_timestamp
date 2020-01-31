#!/usr/bin/env python3
#Adds a timestamp to an image

import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import argparse
import asio
from datetime import date, datetime

def main():
    #filename, date, text, color, size
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--filename', help='name of the image file to add the date to')
    args = parser.parse_args()
    filename = str(args.filename)
    print("Filename: " + filename)
    if (asio.does_not_exist(filename)):
        print("Error: file with filename " + filename + "does not exist")
        sys.exit(1)
    else:
        today = "date goes here"
        photo = Image.open(filename)
        photodraw = ImageDraw.Draw(photo)
        myfont = ImageFont.truetype("ariblk.ttf", 16)
        photodraw.text((10,10), today, fill=(255,0,0), font=myfont)
        photo.save(filename)
        photo.close()
        




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting. Goodbye.")
        sys.exit()
