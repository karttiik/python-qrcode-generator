#importing the required packages.
import image
import qrcode

#defining the requirements.
qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 5
)

#enter the data that has to be stored inside the QRCode, scanning the genetrated QRCode will contain this.
data = "https://www.linkedin.com/in/karttiik/"

#adding the entered data into the defined QRCode.
qr.add_data(data)

qr.make(fit = True)

#genetrate qrcode as an image. 
img = qr.make_image(fill = "black", back_color = "white")
img.save("1.png")
