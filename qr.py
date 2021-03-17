#importing the required packages.
import image
import qrcode

#defining the requirements.
qr = qrcode.QRCode(
    version = 1,          #version parameter is an integer from 1 to 40 that controls the size of the QRCode(smallest being, 21x21 matrix).
    box_size = 10,        #box_size parameter controls how many pixels each 'box' of QRCode is.
    border = 5            #border parameter controls how many boxes thick the border should be(default is 4, which is minimum).
)

#enter the data that has to be stored inside the QRCode, scanning the genetrated QRCode will contain this.
data = "https://www.linkedin.com/in/karttiik/"

#adding the entered data into the defined QRCode.
qr.add_data(data)

#genetrate QRCode on the defined requirements.
qr.make(fit = True)

#genetrate and save qrcode as an image. 
img = qr.make_image(fill = "black", back_color = "white")
img.save("1.png")
