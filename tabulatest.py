from PyPDF2 import PdfFileWriter, PdfFileReader


import tabula
import os
import pandas as pd 
from tabula import convert_into
from tabula import read_pdf
import re
import csv


def conversion(pdfname):

	inputpdf = PdfFileReader(open(pdfname+".pdf", "rb"))
	os.mkdir("static/"+pdfname+"/cleantabulacsv")

	os.mkdir("static/"+pdfname+"/tabulacsv")
	for i in range(inputpdf.numPages):
		output = PdfFileWriter()
		output.addPage(inputpdf.getPage(i))
		with open("static/"+pdfname+"/test.pdf", "wb") as outputStream:
			output.write(outputStream)


		convert_into("static/"+pdfname+"/test.pdf","static/"+pdfname+"/tabulacsv/page"+str(i+1)+".csv",output_format="csv")

	n=[]
	t=[]
	hists=os.listdir("static/"+pdfname+"/tabulacsv")
	for hist in hists:


		with open("static/"+pdfname+"/tabulacsv/"+hist, "r+") as f:
			reader = csv.reader(f, delimiter="\t")
			
			for i, line in enumerate(reader):	
				x = format(line)
				if(re.findall(r'[0-9]+', x) and len(x)<30):
					t.append(x)
				
				
		with open("static/"+pdfname+"/cleantabulacsv/"+hist,"w") as f:
			f.write(str(t))

		






    
    
    
        
