import qrcode
my_qr = qrcode.make("https://github.com/Balashanmugam-rathinam")
my_qr.save("myqr.png")