import qrcode
import wifi_qrcode_generator.generator as qr

ssid = input("Type your wi-fi's ssid:")
hidden = False  # Set to True if the SSID is hidden
authentication_type = "WPA"  # Could be 'WPA', 'WEP', or 'nopass' for open networks
password = input("Type your password:")

# Create a QR code for Wi-Fi network details
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

wifi_string = f"WIFI:T:WPA;S:{ssid};P:{password};;"
qr.add_data(wifi_string)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("wifi_qrcode.png")