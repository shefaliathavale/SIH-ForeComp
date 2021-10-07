import cv2
import sys
import pytesseract
import os
import texttocsv
import builtins
from PIL import Image

from django.utils.encoding import smart_str, smart_unicode

original_open = open
def bin_open(filename, mode='rb'):       
    return original_open(filename, mode)


def conversion(pdfname):
  fil="static/"+pdfname+"/tables"
  os.mkdir("static/"+pdfname+"/textfiles")
  hists = os.listdir(fil)
  for hist in hists:
    imPath=fil+"/"+hist
    config = ('-l eng --oem 1 --psm 3')
    #im = cv2.imread(imPath, cv2.IMREAD_COLOR)
    #text = pytesseract.image_to_string(im, config=config)
    img = Image.open(imPath)


    try:
      builtins.open = bin_open
      bts = pytesseract.image_to_string(img)
    finally:
      builtins.open = original_open

    with open("static/"+pdfname+"/textfiles/"+hist[:-4]+'.txt', 'w') as f:
      bts = smart_str(bts)
      f.write(bts)
  texttocsv.conversion(pdfname)
  return

  
  


 
  
    
    
  