from flask import Flask, render_template
from wand.image import Image as wi
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import glob
import sys


def conversion(inputpdfname):
    inputpdf=PdfFileReader(open(inputpdfname, "rb"))
    print(inputpdf)


    
    
    fil="static/"+inputpdfname[:-4]+"/pdfimages"

    """outpath='pdfs/'"""
    os.mkdir("static/"+inputpdfname[:-4])
    os.mkdir("static/"+inputpdfname[:-4]+"/pdfimages")
    inputpdf=PdfFileReader(open(inputpdfname, "rb"))
    print(inputpdf)



    i=1
    
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(str(i)+".pdf", "wb") as outputStream:
            output.write(outputStream)
        pdf = wi(filename=str(i)+".pdf",resolution=500)
        pdfImage = pdf.convert("jpeg")
        for img in pdfImage.sequence:
            page = wi(image=img)
            filename=str(i)+".jpg"
            page.save(filename= fil+"/"+str(i)+".jpg")
        os.remove(str(i)+".pdf")
        print("File(s) Removed")
    return






"""inputpdf = PdfFileReader(open("multi-page.pdf", "rb"))"""

    
    
    
        
   
    
    
    
        
        
        
    
    

