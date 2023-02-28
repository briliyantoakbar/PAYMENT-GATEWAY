import random
# Python3 code to generate the
# random id using uuid1()
from PIL import ImageTk, Image
import cv2
import torch
import numpy as np
import time
from cvzone.SerialModule import SerialObject
arduino=SerialObject("COM3")
import pandas as pd
df=pd.read_csv('QR_ID.csv')
dfbaru=pd.DataFrame()
x=0
model_name='C:/python program/yolov5/runs/train/exp2/weights/best.pt'
# model = torch.hub.load(os.getcwd(), 'custom', source='local', path = model_name, force_reload = True)
model = torch.hub.load('C:/python program/yolov5', 'custom', source='local', path = model_name, force_reload = True)
from PIL import ImageTk, Image
lebar, tinggi= 180, 180
lebar2, tinggi2= 180, 180
cap=cv2.VideoCapture(0)
cap2=cv2.VideoCapture(1)
cap.set(3,lebar)
cap.set(4, tinggi)
cap2.set(1,lebar2)
cap2.set(3, tinggi2)
global kondisi
kondisi=0
global s
s=0
dt2=1

import uuid
# Printing random id using uuid1()
# print ("The random id using uuid1() is : ",end="")
import midtransclient
import tkinter as tk
from tkinter import Button, Entry,Frame, Label, BitmapImage
from pyqrcode import create
window=tk.Tk()
frame=Frame(window,width=1366,height=768, background="#f6f6f6")
frame.pack()
frame2=Frame(frame,width=1366,height=500, background="#1b61e1")
frame2.place(x=0,y=0)
frame3x=Frame(frame,width=370,height=410, background="#d3e1fe")
frame3x.place(x=865,y=195)
frame3=Frame(frame,width=360,height=400, background="#f6f6f6")
frame3.place(x=870,y=200)
framekondisikeluar=Frame(frame2,width=245,height=35, background="#f6f6f6")
framekondisikeluar.place(x=925,y=150)
framekondisimasuk=Frame(frame2,width=245,height=35, background="#f6f6f6")
framekondisimasuk.place(x=60,y=150)
# frame4=Frame(frame,width=653,height=10, background="#fcbc35")
# frame4.place(x=0,y=400)
# frame5=Frame(frame,width=138,height=35, background="#1b61e1")
# frame5.place(x=900,y=600)
frame6=Frame(frame2,width=200,height=40, background="#d3e1fe")
frame6.place(x=50,y=20)

# frame7=Frame(frame,width=650,height=200, background="#d3e1fe")
# frame7.place(x=20,y=450)
frame9x=Frame(frame,width=370,height=410, background="#d3e1fe")
frame9x.place(x=15,y=195)
frame9=Frame(frame,width=360,height=400, background="#f6f6f6")
frame9.place(x=20,y=200)
framemotor=Frame(frame2,width=300,height=48, background="#d3e1fe")
framemotor.place(x=1000,y=20)
text1=Label(frame2,text="Parkir With",font=('Cooper Black',30), bg='#1b61e1', fg='#f6f6f6')
text1.place(x=360, y=10)
text2=Label(frame2,text="Payment Gateway",font=('Book Antiqua',30), bg='#1b61e1', fg='#f6f6f6')
text2.place(x=620, y=10)
L1=Label(frame3,bg="#fcbc35")
L1.place(x=0,y=0)
L2=Label(frame9,bg="#d3e1fe")
L2.place(x=0,y=0)
framegaya1=Frame(frame2,width=60,height=60, background="#1b61e1",highlightbackground="#f5d00e",highlightthickness=5)
framegaya1.place(x=40, y=60)
framegaya1=Frame(frame2,width=63,height=63, background="#f5d00e",highlightbackground="#1b61e1",highlightthickness=5)
framegaya1.place(x=20, y=35)
framegaya2=Frame(frame2,width=60,height=60, background="#1b61e1",highlightbackground="#f5d00e",highlightthickness=5)
framegaya2.place(x=860, y=60)
framegaya2=Frame(frame2,width=63,height=63, background="#f5d00e",highlightbackground="#1b61e1",highlightthickness=5)
framegaya2.place(x=840, y=35)
# tulisanL1=Label(frame,text="  Pintu Masuk  ",font=('Arial',11), bg="#f6f6f6")
# tulisanL1.place(x=100,y=410)
# tulisanL2=Label(frame,text="Pintu Keluar",font=('Arial',11), bg="#f6f6f6")
# tulisanL2.place(x=450,y=410)
global dta
global dtt
global sekon
global hours
global t
t=0
global img41
qcd = cv2.QRCodeDetector()
def countdownTimer(start_minute, start_second):
                    total_second = start_minute * 60 + start_second
                    window.update()
                    global img41
                    global ddt2

                    import time
                    while total_second:
                        seccess,img=cap.read()
                        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                        img=ImageTk.PhotoImage(Image.fromarray(img))
                        window.update()
                        mins, secs = divmod(total_second, 60)
                        L1=Label(frame3,bg="#f6f6f6")
                        L1.place(x=15,y=30)
                        L1['image']=img41
                        window.update()
                        print(f'{mins:02d}:{secs:02d}', end='\r')
                        time.sleep(1)
                        total_second -= 1
                        timer=Label(frame,text=str(secs),font=('Arial',25), bg='#f6f6f6', fg='#4d4e4d')
                        timer.place(x=0,y=540)
                        # timer=Label(frame2,text=str(secs),font=('Arial',20), bg='#1b61e1', fg='#f6f6f6')
                        # timer.place(x=700,y=150)
                        if(secs==0):
                            return()
                            
def gen_qr():
        global dta
        global dtt
        global sekon
        global kondisi
        global hours
        global t
        dt=uuid.uuid4()
        dtt=str(dt)
        global img41
        global harga
        jam=int(hours)
        if(jam <=1):
            harga=5000
        elif(jam >1):
            harga=int(hours)*5000
        snap = midtransclient.Snap(
    # Set to true if you want Production Environment (accept real transaction).
                is_production=True,
                server_key='Mid-server-LhAuiwUK7c1dQp8W_lmxtNWr'
                    )
# Build API parameter
        param = {
            "transaction_details": {
                "order_id":dtt,
                "gross_amount": 20000
            }, "credit_card":{
                "secure" : True
            }
        }
        
        transaction = snap.create_transaction(param)
        x=transaction["redirect_url"]
        dta=transaction["redirect_url"]
        dta = create(dta)
        test = dta.xbm(scale=8)

        xbm_image = BitmapImage(data=test, foreground="black", background='white')
        image_view.config(image=xbm_image)
        t=1

        if(t==1):
            import time
            def countdownTimer(start_minute, start_second):
                total_second = start_minute * 60 + start_second
                window.update()
                global sekon
                while total_second:
                    seccess,img=cap.read()
                    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                    img=ImageTk.PhotoImage(Image.fromarray(img))
                    window.update()
                    global sekon
                    mins, secs = divmod(total_second, 60)
                    sekon=secs
                    print(f'{mins:02d}:{secs:02d}', end='\r')
                    time.sleep(1)
                    total_second -= 1
                    timer=Label(frame,text=str(secs),font=('Arial',25), bg='#f6f6f6', fg='#4d4e4d')
                    timer.place(x=860,y=540)
                    # timer=Label(frame2,text=str(secs),font=('Arial',20), bg='#1b61e1', fg='#f6f6f6')
                    # timer.place(x=700,y=150)
                    h=1
                    h=secs%5
                    if(h==0):
                        api_client = midtransclient.CoreApi(
                        is_production=True,
                        server_key='Mid-server-LhAuiwUK7c1dQp8W_lmxtNWr',
                        client_key='Mid-client-Pr7pP47Gyd_7lXFG')
                        status_response = api_client.transactions.status(dtt)
                        print(status_response['transaction_status'])
                        window.update()
                        if(status_response['transaction_status']=="settlement" or secs==0):
                            return()


            if __name__ == '__main__':
                countdownTimer(00, 30) 
               
while cap.isOpened():
    # seccess,img=cap.read()
    # img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    # img=ImageTk.PhotoImage(Image.fromarray(img))
    # L1['image']=
    # L2['image']=img
   
    #pomodoro timer
                # api_client = midtransclient.CoreApi(
                # is_production=False,
                # server_key='SB-Mid-server-jdslTONbVvrONwy77BIV9PRe',
                # client_key='SB-Mid-client-ztDc1KJnedAz6k5r')
                # status_response = api_client.transactions.status(dtt)
                # print(status_response['transaction_status'])
    ret, framew = cap.read()
    ret, framew1 = cap2.read()
    image = Image.fromarray(cv2.cvtColor(framew, cv2.COLOR_BGR2RGB))
    image = image.resize((640, 640))

    if ret:
        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(framew1)
        if ret_qr:
            for s, p in zip(decoded_info, points):
                if s:
                    print(s)
                    color = (0, 255, 0)
                    
                else:
                    color = (0, 0, 255)
                framew1 = cv2.polylines(framew1, [p.astype(int)], True, color, 8)
                op=cv2.resize(framew1,(320,247))
                img3=cv2.cvtColor(framew,cv2.COLOR_BGR2RGB)
                img4=ImageTk.PhotoImage(Image.fromarray(img3))
                img31=cv2.cvtColor(op,cv2.COLOR_BGR2RGB)
                img41=ImageTk.PhotoImage(Image.fromarray(img31))
                L1['image']=img41
                L2['image']=img4
                window.update()

    results1 = model(framew)


    results = results1.pandas().xyxy[0].to_dict(orient="records")
    for result in results:
                con = result['confidence']
                data= result['class']
                x1 = int(result['xmin'])
                y1 = int(result['ymin'])
                x2 = int(result['xmax'])
                y2 = int(result['ymax'])
                if(data==0):

                    cv2.rectangle(framew, (x1, y1), (x2,y2), (255, 0 , 255), 2)
                    img3=cv2.cvtColor(framew,cv2.COLOR_BGR2RGB)
                    img4=ImageTk.PhotoImage(Image.fromarray(img3))
                    img31=cv2.cvtColor(framew1,cv2.COLOR_BGR2RGB)
                    img41=ImageTk.PhotoImage(Image.fromarray(img31))
                    L1['image']=img41
                    L2['image']=img4
                    window.update()
                    time.sleep(4)
                    dt2=uuid.uuid4()
                    dtt2=str(dt2)
                    dta2 = create(dtt2)
                    import pandas as pd
                    dfQR= pd.read_csv('QR_ID.csv')
                    dfbaru=pd.DataFrame()
                    QRlist=[""]
                    QRlist.append(dtt2)
                    dfbaru['id']=QRlist[-1:]
                    datawaktu=pd.to_datetime('today')
                    dfbaru["tgl"]=datawaktu

                    HG="QR_ID.csv"
                    listdat=[dfQR,dfbaru]
                    baru=pd.concat(listdat)
                    baru.to_csv(HG, index=False)
                    test2 = dta2.xbm(scale=8)
                    xbm_image2 = BitmapImage(data=test2, foreground="black", background='white')
                    image_view2.config(image=xbm_image2)
                    window.update()
                    if __name__ == '__main__':
                        countdownTimer(00, 20) 
    terima=str(dt2)
    print(s)
    if(s!=0):
        listID=[]
        dfQR= pd.read_csv('QR_ID.csv')
        dftampung=pd.DataFrame()

        for n in dfQR["id"]:
            listID.append(n)
        jumlahID=len(dfQR['id'])
        i=range(jumlahID)
        for n in (i):
            x+=1
            if (s==listID[x]):
                dfQR["tgl"]=pd.to_datetime(dfQR["tgl"][x])
                baru=pd.to_datetime('today')
                dftampung["day"]=(baru-dfQR["tgl"]).astype('<m8[D]').astype(int)
                dftampung["hours"]=(baru-dfQR["tgl"]).astype('<m8[h]').astype(int)
                dftampung["minute"]=(baru-dfQR["tgl"]).astype('<m8[m]').astype(int)
                day=str(dftampung["day"][0])
                hours=str(dftampung["hours"][0])
                minute=str(dftampung["minute"][0])
                print(day)
                print(hours)
                print(minute)
                
                gen_qr()
                i =range(0)
                dt2=1
                s=0
                x=0
    op=cv2.resize(framew1,(320,247))
    img3=cv2.cvtColor(framew,cv2.COLOR_BGR2RGB)
    img4=ImageTk.PhotoImage(Image.fromarray(img3))
    img31=cv2.cvtColor(op,cv2.COLOR_BGR2RGB)
    img41=ImageTk.PhotoImage(Image.fromarray(img31))
    L1['image']=img41
    L2['image']=img4
    window.update()
    frame3=Frame(frame,width=360,height=400, background="#f6f6f6")
    frame3.place(x=870,y=200)
    frame9=Frame(frame,width=360,height=400, background="#f6f6f6")
    frame9.place(x=20,y=200)
    print("utama")
    L1=Label(frame3,bg="#f6f6f6")
    L1.place(x=15,y=30)
    L2=Label(frame9,bg="#f6f6f6")
    L2.place(x=15,y=30)
    image_view = Label(frame3)
    statement = Label(frame3)
    image_view.place(x=0, y= 0)
    statement.place(x=0, y= 0)
    image_view2 = Label(frame9)
    statement2 = Label(frame3)
    image_view2.place(x=0, y= 0)
    statement2.place(x=0, y= 0)

window.mainloop()

