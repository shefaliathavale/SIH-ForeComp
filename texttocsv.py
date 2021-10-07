

from flask import Flask, render_template
import csv
import os

def conversion(pdfname):
	fil="static/"+pdfname+"/textfiles"
	os.mkdir("static/"+pdfname+"/csvfiles")
	hists = os.listdir(fil)
	for hist in hists:
		with open("static/"+pdfname+"/csvfiles/"+hist[:-4]+'.csv', 'w') as writeFile:
			in_txt = csv.reader(open(fil+"/"+hist[:-4]+".txt", "rb"), delimiter = ' ')
			out_csv = csv.writer(writeFile)
			out_csv.writerows(in_txt)
			#writeFile.save("static/"+pdfname[:-4]+"/csvfiles/"+hist[:-4]+".csv")
	return







	


	
	
	
	
	





# use 'with' if the program isn't going to immediately terminate
# so you don't leave files open
# the 'b' is necessary on Windows
# it prevents \x1a, Ctrl-z, from ending the stream prematurely
# and also stops Python converting to / from different line terminators
# On other platforms, it has no effect


