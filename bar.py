import qrcode

qr = qrcode.make("hi  hello  Rama raju")
qr.save('hello2.jpg')
qr.show()