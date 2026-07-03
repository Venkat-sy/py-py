"""
Project 7: QR Code Generator
External Requirements: pip install qrcode Image
"""
import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")
    print("QR Code generated and saved as qrimg.png")

# generate_qrcode("https://www.google.com")
