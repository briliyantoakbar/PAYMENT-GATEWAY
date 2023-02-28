
import tkinter as tk
from tkinter import Button, Entry,Frame, Label, BitmapImage
from pyqrcode import create
window=tk.Tk()
frame=Frame(window,width=1000,height=600, background="#624cab")
frame.pack()
frame2=Frame(frame,width=974.032,height=575.750, background="#758ecd")
frame2.place(x=12,y=12)
global dta
d={'status_code': '201', 'status_message': 'GoPay transaction is created', 'transaction_id': '5072b7a4-f621-4d95-8a9a-f3aaa4798151', 'order_id': 't-to-54321', 'merchant_id': 'G039902526', 'gross_amount': '12145.00', 'currency': 'IDR', 'payment_type': 'gopay', 'transaction_time': '2022-11-22 09:57:04', 'transaction_status': 'pending', 'fraud_status': 'accept', 'actions': [{'name': 'generate-qr-code', 'method': 'GET', 'url': 'https://api.sandbox.midtrans.com/v2/gopay/5072b7a4-f621-4d95-8a9a-f3aaa4798151/qr-code'}, {'name': 'deeplink-redirect', 'method': 'GET', 'url': 'https://simulator.sandbox.midtrans.com/gopay/partner/app/payment-pin?id=c04db8ed-d9b9-47b3-8217-02cd516db091'}, {'name': 'get-status', 'method': 'GET', 'url': 'https://api.sandbox.midtrans.com/v2/5072b7a4-f621-4d95-8a9a-f3aaa4798151/status'}, {'name': 'cancel', 'method': 'POST', 'url': 'https://api.sandbox.midtrans.com/v2/5072b7a4-f621-4d95-8a9a-f3aaa4798151/cancel'}]}



def gen_qr():
    global dta
    dta = create(dta)
    test = dta.xbm(scale=10)
    global xbm_image
    xbm_image = BitmapImage(data=test, foreground="black", background='white')
    image_view.config(image=xbm_image)

make_button =Button(frame2, text=" Make QR", command=gen_qr)
image_view = Label(frame)
statement = Label(frame2)

# gui grid
make_button.place(x=20, y= 40)
image_view.place(x=400, y= 100)
statement.place(x=200, y= 20)

window.mainloop()
