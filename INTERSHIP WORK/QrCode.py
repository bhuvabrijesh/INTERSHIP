
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=20,
    border=1
)

message = input("Enter Message : ")

qr.add_data(message)
qr.make(fit=True)

#data = qr.make_image()
data = qr.make_image(fill_color="red",back_color="white")
data.save("QrDemo.png")