import random
# Python3 code to generate the
# random id using uuid1()
from PIL import ImageTk, Image
import cv2
import torch
import numpy as np
import time
from cvzone.SerialModule import SerialObject
arduino=SerialObject("COM4")
global rodadua
global rodaempat
rodadua="00"
rodaempat="00"
import pandas as pd
df=pd.read_csv('QR_ID.csv')
dfbaru=pd.DataFrame()
dfharga= pd.read_csv('data.csv')
global listharga
listharga=[]
listkapasitas=[]
for o in dfharga["harga"]:
    listharga.append(o)
for kap in dfharga["kapasitas"]:
    listkapasitas.append(kap)
count=0
# model_name='C:/python program/yolov5/runs/train/exp2/weights/best.pt'
model_name='C:\python program\yolov5-master\yolov5s.pt'
# model = torch.hub.load(os.getcwd(), 'custom', source='local', path = model_name, force_reload = True)
model = torch.hub.load('C:/python program/yolov5-master', 'custom', source='local', path = model_name, force_reload = True)
from PIL import ImageTk, Image
lebar, tinggi= 180, 180
lebar2, tinggi2= 180, 180
cap=cv2.VideoCapture(0)
cap2=cv2.VideoCapture(2)
# cap2.set(cv2.CAP_PROP_AUTOFOCUS, 1)
cap.set(3,lebar)
cap.set(4, tinggi)
cap2.set(1,lebar2)
cap2.set(3, tinggi2)
global kondisi
kondisi=0
global s
s=0
dt2=1
sikon=0
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
framekondisimasuk.place(x=160,y=150)
# frametransaksi=Frame(frame,width=245,height=40, background="#1b61e1",highlightbackground="#d3e1fe",highlightthickness=3)
# frametransaksi.place(x=925,y=610)
frame9x=Frame(frame,width=370,height=410, background="#d3e1fe")
frame9x.place(x=105,y=195)

frame9=Frame(frame,width=360,height=400, background="#f6f6f6")
frame9.place(x=110,y=200)
frameinformasi=Frame(frame2,width=300,height=50, background="#d3e1fe",highlightbackground="#f6f6f6",highlightthickness=1)
frameinformasi.place(x=1000,y=20)
frameinformasiharga=Frame(frame2,width=300,height=50, background="#d3e1fe",highlightbackground="#f6f6f6",highlightthickness=1)
frameinformasiharga.place(x=40,y=20)
text1=Label(frame2,text="PARKIR WITH",font=('Arial Bold',29), bg='#1b61e1', fg='#f6f6f6')
text1.place(x=520, y=10)
text2=Label(frame2,text="PAYMENT GATEWAY",font=('Arial Bold',27), bg='#1b61e1', fg='#f6f6f6')
text2.place(x=480, y=70)
L1=Label(frame3,bg="#fcbc35")
L1.place(x=0,y=0)
L2=Label(frame9,bg="#d3e1fe")
L2.place(x=0,y=0)
imgmotor = ImageTk.PhotoImage(Image.open("iconmotor.png"))

# Create a Label Widget to display the text or Image
labelmotor = Label(frameinformasiharga, image = imgmotor)
labelmotor.place(x=0,y=0)

labelmotor2 = Label(frameinformasiharga, text=str(listharga[1])+"/ Hours",font=('Arial',12),bg='#d3e1fe',fg="#6f6f6f")
labelmotor2.place(x=60,y=3)
labelmobil2 = Label(frameinformasiharga,text=str(listharga[0])+"/ Hours",font=('Arial',12),bg='#d3e1fe',fg="#6f6f6f")
labelmobil2.place(x=60,y=25)

# framegaya1=Frame(frame2,width=60,height=60, background="#1b61e1",highlightbackground="#f6f6f6",highlightthickness=5)
# framegaya1.place(x=40, y=60)
# framegaya1=Frame(frame2,width=63,height=63, background="#f5d00e",highlightbackground="#1b61e1",highlightthickness=5)
# framegaya1.place(x=20, y=35)
# framegaya2=Frame(frame2,width=60,height=60, background="#1b61e1",highlightbackground="#f5d00e",highlightthickness=5)
# framegaya2.place(x=860, y=60)
# framegaya2=Frame(frame2,width=63,height=63, background="#f5d00e",highlightbackground="#1b61e1",highlightthickness=5)
# framegaya2.place(x=840, y=35)
# tulisanL1=Label(frame,text="  Pintu Masuk  ",font=('Arial',11), bg="#f6f6f6")
# tulisanL1.place(x=100,y=410)
# tulisanL2=Label(frame,text="Pintu Keluar",font=('Arial',11), bg="#f6f6f6")
# tulisanL2.place(x=450,y=410)

global data
global dta
global dtt
global sekon
global hours

global img41
qcd = cv2.QRCodeDetector()
def countdownTimer(start_minute, start_second):
                    total_second = start_minute * 60 + start_second
                    window.update()
                    global img41
                    global ddt2
                    global rodadua
                    global rodaempat
                    textmasuk=Label(framekondisimasuk,text="                           ", font=('sanserif',15),bg='#f6f6f6', fg='#6f6f6f')
                    textmasuk.place(x=50,y=2)   
                    textmasuk=Label(framekondisimasuk,text="Foto Tiket Anda", font=('sanserif',15),bg='#f6f6f6', fg='#6f6f6f')
                    textmasuk.place(x=50,y=2)
                    window.update()

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
                        if(secs>=10):
                            timer=Label(frame,text=str(secs),font=('Arial',25), bg='#f6f6f6', fg='#4d4e4d')
                            timer.place(x=260,y=620)
                        elif(secs <10):
                            timer=Label(frame,text="0"+str(secs),font=('Arial',25), bg='#f6f6f6', fg='#4d4e4d')
                            timer.place(x=260,y=620)
                        # timer=Label(frame2,text=str(secs),font=('Arial',20), bg='#1b61e1', fg='#f6f6f6')
                        # timer.place(x=700,y=150)
                        if(secs<=1):
                            df_motordanmobil=pd.read_csv('QR_ID.csv')
                            h1=(df_motordanmobil.loc[(df_motordanmobil['jenis_kendaraan'] == 'mobil') & (df_motordanmobil['status_payment'] == '-')].count())
                            arduino.sendData([1])
                            introdaempat=int(h1['id'])
                            k1=(df_motordanmobil.loc[(df_motordanmobil['jenis_kendaraan'] == 'motor') & (df_motordanmobil['status_payment'] == '-')].count())
                            introdadua=int(k1['id'])
                            if(introdaempat <10):
                                rodaempat=str(0)+str(introdaempat)

                            if(introdaempat >=10):
                                rodaempat=str(introdaempat)

                            if(introdadua <10):
                                rodadua=str(0)+str(introdadua)

                            if(introdadua >=10):
                                rodaempat=str(introdadua)

                            textmobil=Label(frame2,text="        ",font=('sanserif',40),bg='#1b61e1', fg='#f6f6f6')
                            textmobil.place(x=630,y=230)
                            textmotor=Label(frame2,text="        ",font=('sanserif',40),bg='#1b61e1', fg='#f6f6f6')
                            textmotor.place(x=630,y=370)
                            textmobil=Label(frame2,text=str(rodaempat),font=('sanserif',40),bg='#1b61e1', fg='#f6f6f6')
                            textmobil.place(x=630,y=230)
                            textmotor=Label(frame2,text=str(rodadua),font=('sanserif',40),bg='#1b61e1', fg='#f6f6f6')
                            textmotor.place(x=630,y=370)
                            dayatampungmobil=int(rodaempat)
                            dayatampungmotor=int(rodadua)
                            motor_supra=int(listkapasitas[0])
                            mobil_supra=int(listkapasitas[0])
                            kapasitasmotor=str(motor_supra-dayatampungmotor)
                            kapasitasmobil=str(mobil_supra-dayatampungmobil)
                            textinfomobil=Label(frameinformasi,text=kapasitasmobil,font=('Arial',20),bg='#d3e1fe', fg='#6f6f6f')
                            textinfomobil.place(x=185,y=15)
                            nilaiinfomotor=Label(frameinformasi,text=kapasitasmotor,font=('Arial',20),bg='#d3e1fe', fg='#6f6f6f')
                            nilaiinfomotor.place(x=70,y=15) 
                            textmasuk=Label(framekondisimasuk,text="                        ", font=('sanserif',15),bg='#f6f6f6', fg='#6f6f6f')
                            textmasuk.place(x=50,y=2)

                            window.update()
                            return()
                            
def gen_qr():
        global dta
        global s
        global dtt
        global sekon
        global kondisi
        global hours
        global listharga
        global sikon
        global listjeniskendaraan
        dt=uuid.uuid4()
        dtt=str(dt)
        global img41
        global harga
        jam=int(hours)
        global count
        id= pd.read_csv('QR_ID.csv')
        ID=str(id['id'][count])
        IN=str(id['tgl'][count])

        if(listjeniskendaraan[count]=="mobil"):
            if(jam <=1):
                harga=int(listharga[0])
            elif(jam >1):
                komulatif=int(listharga[0])
                harga=int(hours)*komulatif
        elif(listjeniskendaraan[count]=="motor"):
            if(jam <=1):
                harga=int(listharga[1])
            elif(jam >1):
                komulatif=int(listharga[1])
                harga=int(hours)*komulatif
        core_api = midtransclient.CoreApi(
            is_production=False,
            server_key='SB-Mid-server-jdslTONbVvrONwy77BIV9PRe',
            client_key='SB-Mid-client-ztDc1KJnedAz6k5r'
        )
        # Build API parameter
        param = {
            "payment_type": "gopay",
            "transaction_details": {
                "gross_amount": harga,
                "order_id":dtt,
            },
            "gopay": {
                "enable_callback": False,                # optional
                # "callback_url": "someapps://callback"   # optional
            }
        }
        OUT=pd.to_datetime('today')
        OUT1=str(OUT)
        textrincianID=Label(frame,text=ID,font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
        textrincianID.place(x=570,y=540)
        textrincianIN=Label(frame,text=IN,font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
        textrincianIN.place(x=570,y=570) 
        textrincianOut=Label(frame,text=OUT1,font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
        textrincianOut.place(x=570,y=600)
        textrincianharga=Label(frame,text=harga,font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
        textrincianharga.place(x=570,y=625)
        window.update()
        # charge transaction
        charge_response = core_api.charge(param)
        print(charge_response)
        dta=charge_response["actions"][1]['url']
        dta = create(dta)
        test = dta.xbm(scale=5)

        xbm_image = BitmapImage(data=test, foreground="black", background='white')
        image_view.config(image=xbm_image)
        api_client = midtransclient.CoreApi(
        is_production=False,
        server_key='SB-Mid-server-jdslTONbVvrONwy77BIV9PRe',
        client_key='SB-Mid-client-ztDc1KJnedAz6k5r'
        )
        status_response = api_client.transactions.status(dtt)
        
        if(status_response['transaction_status']=="pending"):
            textkeluar=Label(framekondisikeluar,text="                 ", font=('sanserif',15),bg='#f6f6f6', fg='#6f6f6f')
            textkeluar.place(x=60,y=2)
            textkeluar=Label(framekondisikeluar,text="PENDING", font=('sanserif',15),bg='#f6f6f6', fg='#f5d00e')
            textkeluar.place(x=60,y=2)
            window.update()
            import time
            global sekon

            def countdownTimer(start_minute, start_second):
                total_second = start_minute * 60 + start_second
                window.update()
                global sekon
                global sikon
                global s
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
                    if(secs >=10):
                        timer2=Label(frame,text=str(secs),font=('Arial',25), bg='#f6f6f6', fg='#4d4e4d')
                        timer2.place(x=1015,y=620)
                    elif(secs <10):
                        timer2=Label(frame,text="0"+str(secs),font=('Arial',25), bg='#f6f6f6', fg='#4d4e4d')
                        timer2.place(x=1015,y=620)
                    # timer=Label(frame2,text=str(secs),font=('Arial',20), bg='#1b61e1', fg='#f6f6f6')
                    # timer.place(x=700,y=150)
                    h=1
                    h=secs%5
                    if(h==0):
                        api_client = midtransclient.CoreApi(
                        is_production=False,
                        server_key='SB-Mid-server-jdslTONbVvrONwy77BIV9PRe',
                        client_key='SB-Mid-client-ztDc1KJnedAz6k5r')
                        status_response = api_client.transactions.status(dtt)
                        print(status_response['transaction_status'])
                        window.update()
                        if(status_response['transaction_status']=="settlement" or secs==0):
                            dftransaksi= pd.read_csv('QR_ID.csv')
                            if(status_response['transaction_status']=="settlement"):
                                sikon=1
                                textkeluar=Label(framekondisikeluar,text="                 ", font=('sanserif',15),bg='#f6f6f6', fg='#6f6f6f')
                                textkeluar.place(x=60,y=2)
                                textkeluar=Label(framekondisikeluar,text="SETTLEMENT", font=('sanserif',15),bg='#f6f6f6', fg='#00ff04')
                                textkeluar.place(x=50,y=2)
                                window.update()
                                HF="QR_ID.csv"
                                dftransaksi.loc[count,'status_payment'] = "settlement"
                                dftransaksi.to_csv(HF, index=False)
                            elif(status_response['transaction_status']=="panding"):
                                HF="QR_ID.csv"
                                dftransaksi.loc[count,'status_payment'] = "expired"
                                dftransaksi.to_csv(HF, index=False)
                            df_motordanmobil=pd.read_csv('QR_ID.csv')
                            h1=(df_motordanmobil.loc[(df_motordanmobil['jenis_kendaraan'] == 'mobil') & (df_motordanmobil['status_payment'] == '-')].count())

                            introdaempat=int(h1['id'])
                            k1=(df_motordanmobil.loc[(df_motordanmobil['jenis_kendaraan'] == 'motor') & (df_motordanmobil['status_payment'] == '-')].count())
                            introdadua=int(k1['id'])
                            if(introdaempat <10):
                                rodaempat=str(0)+str(introdaempat)

                            if(introdaempat >=10):
                                rodaempat=str(introdaempat)

                            if(introdadua <10):
                                rodadua=str(0)+str(introdadua)

                            if(introdadua >=10):
                                rodaempat=str(introdadua)
                            textmobil=Label(frame2,text="        ",font=('sanserif',40),bg='#1b61e1', fg='#f6f6f6')
                            textmobil.place(x=610,y=230)
                            textmotor=Label(frame2,text="        ",font=('sanserif',40),bg='#1b61e1', fg='#f6f6f6')
                            textmotor.place(x=610,y=370)
                            textmobil=Label(frame2,text=str(rodaempat),font=('sanserif',40),bg='#1b61e1', fg='#f6f6f6')
                            textmobil.place(x=630,y=230)
                            textmotor=Label(frame2,text=str(rodadua),font=('sanserif',40),bg='#1b61e1', fg='#f6f6f6')
                            textmotor.place(x=630,y=370)
                            dayatampungmobil=int(rodaempat)
                            dayatampungmotor=int(rodadua)
                            motor_supra=int(listkapasitas[0])
                            mobil_supra=int(listkapasitas[0])
                            kapasitasmotor=str(motor_supra-dayatampungmotor)
                            kapasitasmobil=str(mobil_supra-dayatampungmobil)
                            textinfomobil=Label(frameinformasi,text=kapasitasmobil,font=('Arial',20),bg='#d3e1fe', fg='#6f6f6f')
                            textinfomobil.place(x=185,y=15)
                            nilaiinfomotor=Label(frameinformasi,text=kapasitasmotor,font=('Arial',20),bg='#d3e1fe', fg='#6f6f6f')
                            nilaiinfomotor.place(x=70,y=15) 
                            textrincianID=Label(frame,text="                                                ",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
                            textrincianID.place(x=570,y=540)
                            textrincianIN=Label(frame,text="                                                ",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
                            textrincianIN.place(x=570,y=570) 
                            textrincianOut=Label(frame,text="                                                ",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
                            textrincianOut.place(x=570,y=600)
                            textrincianharga=Label(frame,text='                                                ',font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
                            textrincianharga.place(x=570,y=625)
                            window.update()
                            if(status_response['transaction_status']=="panding" and secs==0):
                                textkeluar=Label(framekondisikeluar,text="                               ", font=('sanserif',15),bg='#f6f6f6', fg='#6f6f6f')
                                textkeluar.place(x=30,y=2)
                                textkeluar=Label(framekondisikeluar,text="Transaction Failed", font=('sanserif',15),bg='#f6f6f6', fg='#ff0000')
                                textkeluar.place(x=30,y=2)
                                time.sleep(2)
                                window.update()
                                return()
                            s=0
                            time.sleep(1)
                            return()

                            



            if __name__ == '__main__':
                countdownTimer(00, 58)

textmobil=Label(frame2,text=str(rodaempat),font=('sanserif',40),bg='#1b61e1', fg='#f6f6f6')
textmobil.place(x=630,y=230)
textmobil1=Label(frame2,text="Mobil",font=('Arial',12),bg='#1b61e1', fg='#f6f6f6')
textmobil1.place(x=637,y=190)
textmotor=Label(frame2,text=str(rodadua),font=('sanserif',40),bg='#1b61e1', fg='#f6f6f6')
textmotor.place(x=630,y=370)   
textmotor1=Label(frame2,text="Motor",font=('Arial',12),bg='#1b61e1', fg='#f6f6f6')
textmotor1.place(x=637,y=330)     
textinfomobil=Label(frameinformasi,text="Mobil",font=('Arial Bold',9),bg='#d3e1fe', fg='#6f6f6f')
textinfomobil.place(x=182,y=0)
textinfomotor=Label(frameinformasi,text="Motor",font=('Arial Bold',9),bg='#d3e1fe', fg='#6f6f6f')
textinfomotor.place(x=76,y=0)

textmasuk=Label(framekondisimasuk,text="Create Tiket", font=('sanserif',15),bg='#f6f6f6', fg='#6f6f6f')
textmasuk.place(x=50,y=2)
textkeluar=Label(framekondisikeluar,text="Scan Tiket", font=('sanserif',15),bg='#f6f6f6', fg='#6f6f6f')
textkeluar.place(x=60,y=2)
# texttransaksi=Label(frametransaksi,text="PANDING", font=('sanserif',15),bg='#1b61e1', fg='#f6f6f6')
# texttransaksi.place(x=65,y=3)
textrincian=Label(frame,text="Rincian Transaksi:",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
textrincian.place(x=590,y=510)
textrincianID=Label(frame,text="ID           :   -",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
textrincianID.place(x=490,y=540)
textrincianIN=Label(frame,text="Cek In     :   -",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
textrincianIN.place(x=490,y=570) 
textrincianOut=Label(frame,text="Cek Out   :   -",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
textrincianOut.place(x=490,y=600)
textrincianharga=Label(frame,text="Nominal   :   -",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
textrincianharga.place(x=490,y=625)
df_motordanmobil=pd.read_csv('QR_ID.csv')
h=(df_motordanmobil.loc[(df_motordanmobil['jenis_kendaraan'] == 'mobil') & (df_motordanmobil['status_payment'] == '-')].count())

introdaempat=int(h['id'])
k=(df_motordanmobil.loc[(df_motordanmobil['jenis_kendaraan'] == 'motor') & (df_motordanmobil['status_payment'] == '-')].count())
introdadua=int(k['id'])

if(introdaempat <10):
    rodaempat=str(0)+str(introdaempat)

if(introdaempat >=10):
    rodaempat=str(introdaempat)

if(introdadua <10):
    rodadua=str(0)+str(introdadua)

if(introdadua >=10):
    rodaempat=str(introdadua)

textmobil=Label(frame2,text="        ",font=('sanserif',40),bg='#1b61e1', fg='#f6f6f6')
textmobil.place(x=630,y=230)
textmotor=Label(frame2,text="        ",font=('sanserif',40),bg='#1b61e1', fg='#f6f6f6')
textmotor.place(x=630,y=370)
textmobil=Label(frame2,text=str(rodaempat),font=('sanserif',40),bg='#1b61e1', fg='#f6f6f6')
textmobil.place(x=630,y=230)
textmotor=Label(frame2,text=str(rodadua),font=('sanserif',40),bg='#1b61e1', fg='#f6f6f6')
textmotor.place(x=630,y=370) 

dayatampungmobil=int(rodaempat)
dayatampungmotor=int(rodadua)

motor_supra=int(listkapasitas[0])
mobil_supra=int(listkapasitas[0])
kapasitasmotor=str(motor_supra-dayatampungmotor)
kapasitasmobil=str(mobil_supra-dayatampungmobil)

textinfomobil=Label(frameinformasi,text=kapasitasmobil,font=('Arial',20),bg='#d3e1fe', fg='#6f6f6f')
textinfomobil.place(x=185,y=15)
nilaiinfomotor=Label(frameinformasi,text=kapasitasmotor,font=('Arial',20),bg='#d3e1fe', fg='#6f6f6f')
nilaiinfomotor.place(x=70,y=15)
timer=Label(frame,text="00",font=('Arial',25), bg='#f6f6f6', fg='#4d4e4d')
timer.place(x=260,y=620)
timer2=Label(frame,text="00",font=('Arial',25), bg='#f6f6f6', fg='#4d4e4d')
timer2.place(x=1015,y=620)
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
    timer=Label(frame,text="00",font=('Arial',25), bg='#f6f6f6', fg='#4d4e4d')
    timer.place(x=260,y=620)
    timer2=Label(frame,text="00",font=('Arial',25), bg='#f6f6f6', fg='#4d4e4d')
    timer2.place(x=1015,y=620)
    textmasuk=Label(framekondisimasuk,text="Create Tiket", font=('sanserif',15),bg='#f6f6f6', fg='#6f6f6f')
    textmasuk.place(x=50,y=2)
    textrincianID=Label(frame,text="ID           :   -",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
    textrincianID.place(x=490,y=540)
    textrincianIN=Label(frame,text="Cek In     :   -",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
    textrincianIN.place(x=490,y=570) 
    textrincianOut=Label(frame,text="Cek Out   :   -",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
    textrincianOut.place(x=490,y=600)
    textrincianharga=Label(frame,text="Nominal   :   -",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
    textrincianharga.place(x=490,y=625)
    # textkeluar=Label(framekondisikeluar,text="Scan Tiket", font=('sanserif',15),bg='#f6f6f6', fg='#6f6f6f')
    # textkeluar.place(x=60,y=2)
    textkeluar=Label(framekondisikeluar,text="Scan Tiket", font=('sanserif',15),bg='#f6f6f6', fg='#6f6f6f')
    textkeluar.place(x=60,y=2)
    if ret:
        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(framew1)
        if ret_qr:
            for s, p in zip(decoded_info, points):
                if s:
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
                if(data==2 or data==3):
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
                    if(data==2):
                        jeniskendaraan="mobil"
                    elif(data==3):
                        jeniskendaraan="motor"

                    import pandas as pd
                    dfQR= pd.read_csv('QR_ID.csv')
                    dfbaru=pd.DataFrame()
                    QRlist=[""]
                    QRlist.append(dtt2)
                    dfbaru['id']=QRlist[-1:]
                    datawaktu=pd.to_datetime('today')
                    dfbaru["tgl"]=datawaktu
                    dfbaru["jenis_kendaraan"]=jeniskendaraan
                    dfbaru["status_payment"]="-"

                    HG="QR_ID.csv"
                    listdat=[dfQR,dfbaru]
                    baru=pd.concat(listdat)
                    baru.to_csv(HG, index=False)
                    test2 = dta2.xbm(scale=8)
                    xbm_image2 = BitmapImage(data=test2, foreground="black", background='white')
                    image_view2.config(image=xbm_image2)
                    window.update()
                    if __name__ == '__main__':
                        countdownTimer(00, 30) 
    terima=str(dt2)
    print(s)
    if(s!=0):
        listID=[]
        listjeniskendaraan=[]
        dfQR= pd.read_csv('QR_ID.csv')
        dftampung=pd.DataFrame()

        for n in dfQR["id"]:
            listID.append(n)
        jumlahID=len(dfQR['id'])
        i=range(jumlahID)
        
        for b in dfQR["jenis_kendaraan"]:
            listjeniskendaraan.append(b)

        for n in (i):
            count +=1
            try:
                if (s==listID[count] and dfQR['status_payment'][count]=="-" ):
                    dfQR["tgl"]=pd.to_datetime(dfQR["tgl"][count])
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
                    textmasuk=Label(framekondisimasuk,text="                        ", font=('sanserif',15),bg='#f6f6f6', fg='#6f6f6f')
                    textmasuk.place(x=60,y=2)
                    textmasuk=Label(framekondisimasuk,text="Foto Tiket Anda", font=('sanserif',15),bg='#f6f6f6', fg='#6f6f6f')
                    textmasuk.place(x=50,y=2)
                    window.update()  
                    gen_qr()
                    if(sikon==1):
                        arduino.sendData([2])
                        time.sleep(1)
                        sikon=0
                    textkeluar=Label(framekondisikeluar,text="                               ", font=('sanserif',15),bg='#f6f6f6', fg='#6f6f6f')
                    textkeluar.place(x=37,y=2)
                    textrincianID=Label(frame,text="                                                                 ",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
                    textrincianID.place(x=570,y=540)
                    textrincianIN=Label(frame,text="                                                ",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
                    textrincianIN.place(x=570,y=570) 
                    textrincianOut=Label(frame,text="                                                ",font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
                    textrincianOut.place(x=570,y=600)
                    textrincianharga=Label(frame,text='                                                ',font=('sanserif',13),bg='#f6f6f6', fg='#6f6f6f')
                    textrincianharga.place(x=570,y=625)
                    window.update()
                    i =range(0)
                    dt2=1
                    s=0
                    count=0
            except:
                print("gagal")
                s=0
                count=0
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
    frame9.place(x=110,y=200)
    print("utama")
    arduino.sendData([0])
    L1=Label(frame3,bg="#f6f6f6")
    L1.place(x=15,y=30)
    L2=Label(frame9,bg="#f6f6f6")
    L2.place(x=15,y=30)
    image_view = Label(frame3)
    statement = Label(frame3)
    image_view.place(x=15, y= 0)
    statement.place(x=0, y= 0)
    image_view2 = Label(frame9)
    statement2 = Label(frame3)
    image_view2.place(x=0, y= 0)
    statement2.place(x=0, y= 0)

window.mainloop()

