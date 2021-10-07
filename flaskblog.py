from flask import Flask, render_template
from werkzeug.utils import secure_filename
from flask import request, redirect, url_for
import csv
import os
import texttocsv
import pdftoimage
import snipimage
import tespyt
import yolo_opencv
import tabulatest
#import csvtoxlsx
from PyPDF2 import PdfFileWriter, PdfFileReader

app = Flask(__name__)

@app.route("/")
def basic():
	return render_template('basic.html')



@app.route("/home")
def hello():
    return render_template('home.html')

@app.route("/about")
def about():
    return "<h1>ABout Page</h1>"

@app.route('/generate', methods=['GET', 'POST'])
def generate():
	"""txt_file = request.args.get('upload')"""
	#if request.form[convertbtn] == 'Convert':
	if "convertbtn1" in request.form:
		pdf_file=request.files['upload']
		pdf_file.save(secure_filename(pdf_file.filename))
		pdftoimage.conversion(pdf_file.filename)
		hists = os.listdir("static/"+pdf_file.filename[:-4]+"/pdfimages")
		return render_template('generate.html',abc=str(pdf_file.filename),hists=hists)
	elif "convertbtn2" in request.form:
		pdf_file=request.files['upload']
		pdf_file.save(secure_filename(pdf_file.filename))
		pdfname=pdf_file.filename[:-4]
		os.mkdir("static/"+pdfname)
		tabulatest.conversion(pdfname)
		hists=os.listdir("static/"+pdfname+"/tabulacsv")
		return render_template('tabulapage.html',abc=str(pdfname),hists=hists)

@app.route("/snip", methods=['GET', 'POST'])
def snip():
	if "detectbtn1" in request.form:
		name123=request.form.get('hiddenname')
		snipimage.conversion(name123)
		hists = os.listdir("static/"+name123+"/tables")



		return render_template('showtables.html',abc=name123,hists=hists)
	elif "detectbtn2" in request.form:
		name456=request.form.get('hiddenname')		
		yolo_opencv.conversion(name456)
		hists = os.listdir("static/"+name456+"/tables")
		return render_template('showtables.html',abc=name456,hists=hists)




	
	
	
	


	
	


	""" THIS IS IT
	txt_file= request.files['upload']
	txt_file.save(secure_filename(txt_file.filename))
	csv_file = texttocsv.conversion(txt_file)

THIS IS IT
	"""
	


	"""csv_file.savetxt(secure_filename("new"))"""
	"""paramFile = request.args.get('upload').read()
	portfolio = csv.DictReader(paramFile)"""

	"""in_txt = csv.reader(open(csv_file, "rb"), delimiter = ' ')
	out_csv = csv.writer(open(csv_file, 'wb'))
	out_csv.writerows(in_txt)

	temptext = open(txt_file, 'r+')
	content = temptext.read()
	temptext.close() """
	


@app.route("/tes",methods=['GET', 'POST'])
def tesfn():
	name=request.form.get('imhidden')
	tespyt.conversion(name)
	hists = os.listdir("static/"+name+"/csvfiles")
	return render_template('tesht.html',abc=name,hists=hists)


if __name__ ==  '__main__':
	app.run(debug=True)