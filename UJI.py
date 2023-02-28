# # import tkinter as tk
# # from tkinter import Button, Entry,Frame, Label, BitmapImage
# # from pyqrcode import create
# # window=tk.Tk()
# # frame=Frame(window,width=1100,height=680, background="#f6f6f6")
# # frame.pack()
# # frame2=Frame(frame,width=1100,height=400, background="#1b61e1")
# # frame2.place(x=0,y=0)
# # frame3=Frame(frame,width=280,height=280, background="#f6f6f6")
# # frame3.place(x=700,y=180)
# # frame4=Frame(frame,width=138,height=35, background="#fcbc35")
# # frame4.place(x=140,y=500)
# # frame5=Frame(frame,width=138,height=35, background="#1b61e1")
# # frame5.place(x=900,y=600)
# # frame6=Frame(frame2,width=200,height=40, background="#d3e1fe")
# # frame6.place(x=50,y=20)
# # text1=Label(frame2,text="Parkir With",font=('Cooper Black',40), bg='#1b61e1', fg='#f6f6f6')
# # text1.place(x=50, y=200)
# # text2=Label(frame2,text="Payment Gateway",font=('Book Antiqua',30), bg='#1b61e1', fg='#f6f6f6')
# # text2.place(x=50, y=280)

# # window.mainloop()
# # Python program to Scan and Read a QR code
# import cv2
# cap=cv2.VideoCapture(0)
# qcd = cv2.QRCodeDetector()
# while cap.isOpened():
#     ret, frame = cap.read()

#     if ret:
#         ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
#         if ret_qr:
#             for s, p in zip(decoded_info, points):
#                 if s:
#                     print(s)
#                     color = (0, 255, 0)
#                 else:
#                     color = (0, 0, 255)
#                 frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
#         cv2.imshow('window_name', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

# # from qrtools import qrtools
# # qr = qrtools.QR(filename = "C:/python program/qrcode.png")
# # # from qrtools import QR
# # # my_QR = QR(filename = "C:/python program/qrcode.png")

# # # # decodes the QR code and returns True if successful
# # # my_QR.decode()

# # # # prints the data
# # # print (my_QR.data)
# from cvzone.SerialModule import SerialObject
# arduino=SerialObject("COM4")
# f=3
# arduino.sendData([f])
import time
from cvzone.SerialModule import SerialObject
arduino = SerialObject("COM4")
while True:
    arduino.sendData([1])
    time.sleep(1)
    arduino.sendData([0])
    time.sleep(1)
# import pandas as pd
# data=pd.read_csv('QR_ID.csv')
# data["tgl"]=pd.to_datetime(data["tgl"][1])
# baru=pd.to_datetime('today')
# data["day"]=(baru-data["tgl"]).astype('<m8[D]').astype(int)
# data["hours"]=(baru-data["tgl"]).astype('<m8[h]').astype(int)
# data["minute"]=(baru-data["tgl"]).astype('<m8[m]').astype(int)

# d=str(data["day"][0])
# h=str(data["hours"][0])
# m=str(data["minute"][0])
# print(d)
# print(h)
# print(m)