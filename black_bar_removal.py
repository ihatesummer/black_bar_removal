import numpy as np
import cv2 as cv
import os
import glob
from PIL import Image

source = './'
dest = './'

for img_name in glob.glob("*.png"):
    img = Image.open(img_name)
    x1, y1, x2, y2 = img.getbbox()
    crop_img = img.crop((x1, y1, x2, y2))
    fullpath = os.path.join(dest, img_name)
    crop_img.save(fullpath)
