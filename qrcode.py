#This is a QR Code Generator

import qrcode

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    return img

def save_qr_code(image, file_name="qrcode.png"):
    image.save(file_name)

def main():
    data_to_encode = input("Enter the data to be encoded in the QR code: ")
    
    qr_code_image = generate_qr_code(data_to_encode)
    
    file_name = input("Enter the file name to save the QR code image (default is qrcode.png): ").strip() or "qrcode.png"
    
    save_qr_code(qr_code_image, file_name)
    
    print(f"QR code generated and saved as {file_name}")

if __name__ == "__main__":
    main()
