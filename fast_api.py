from fastapi import FastAPI
from fastapi.responses import FileResponse
import png
from pyqrcode import create
from fpdf import FPDF
app=FastAPI()
import sys

@app.get("/p/{id}")
def root(id):
    from pyqrcode import QRCode
    from pyqrcode import create
    import pyqrcode 
    dataterima=id
    fpdf = FPDF('P', 'mm',(90,100))
    fpdf.add_page()
    number =create(dataterima)
    number.svg('big-number.svg',scale=40)
    number.png('big-number.png',scale=40)
    fpdf.image("big-number.png",15,35,w=60)
    fpdf.set_font("Arial",'B',size=19)
    fpdf.text(32,38, txt="Si-Pacer")
    fpdf.set_font("Arial",size=9)
    fpdf.text(19,93, txt="Terimakasih Atas Kepercayan Anda")
    fpdf.set_font("Arial",'B',size=10)
    fpdf.text(31,12, txt="SMART PARKIR")
    fpdf.set_font("Arial",size=6)
    fpdf.text(22,15, txt="email:smartparkir@gmail.com  tlp:+62858765493")
    fpdf.text(28,19, txt="Jl.pemuda no 4 sebelah ruko merah")
    fpdf.text(36,23, txt="Kebonarum,Klaten")
    fpdf.line(10, 26, 80, 26)
    fpdf.output('tuto1.pdf')
    return FileResponse('tuto1.pdf')
#FileResponse(path="big-number.png", filename="big-number.png", media_type='text')

