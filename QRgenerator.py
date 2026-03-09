#use pip install qrcode
import qrcode
link = input("Enter you link of which QR Code is needed")
myqr=qrcode.make(link)
myqr.save("myqr.png")