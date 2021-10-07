#import pygame
import sys
from PIL import Image
import os
import argparse
import cv2
#pygame.init()

refPt = []
cropping = False
i=0
b=0
#a=0
#b=0


def conversion(pdfname):
    def click_and_crop(event, x, y, flags, param):
       
        global refPt, cropping,i,b


        if event == cv2.EVENT_LBUTTONDOWN:
            refPt = [(x, y)]
            cropping = True

       
        elif event == cv2.EVENT_LBUTTONUP:
           
            refPt.append((x,y))
            cropping = False
           
            image123 = cv2.rectangle(im, refPt[0], refPt[1], (0, 255, 0), 2)
            print("!!!!!!!!!!!!")
            print(refPt[0][0])
            print(refPt[0][1])
            print(refPt[1][0])
            print(refPt[1][1])
            print(type(refPt[1]))
            image123 = image123[refPt[0][1]:refPt[1][1],refPt[0][0]:refPt[1][0]]
            
            cv2.imwrite( "static/"+pdfname+"/tables/"+str(a)+"-"+str(b)+".jpg", image123)
            cv2.imshow("image", im)
            b=b+1
            i=i+1


#def conversion(pdfname):
    refPt = []
    cropping = False
    i=0
    a=-1

    fil="static/"+pdfname+"/pdfimages"
    os.mkdir("static/"+pdfname+"/tables")
    hists = os.listdir(fil)
    for hist in hists:
        path="static/"+pdfname+"/pdfimages/"+hist
       # image = cv2.imread("static/"+pdfname+"/pdfimages/"+hist)
        im = cv2.imread(path,cv2.IMREAD_UNCHANGED)
        im = cv2.resize(im, (1280,720), interpolation = cv2.INTER_AREA)
        #im = cv2.resize(im,None,fx=0.7, fy=0.7, interpolation = cv2.INTER_LINEAR)
        cv2.imwrite(path,im)
        clone = im.copy()
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", click_and_crop)
        a=a+1
        while True:
            cv2.imshow("image", im)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("r"):
                image = clone.copy()
            elif key == ord("c"):
                break
        if len(refPt) == 2:
            cv2.waitKey(0)
        cv2.destroyAllWindows()


    #roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    #cv2.imshow("ROI", roi)
        

    # ensure output rect always has positive width, height    