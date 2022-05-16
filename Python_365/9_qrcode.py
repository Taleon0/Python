# pip install qrcode
import io
import qrcode
qr = qrcode.QRCode()
qr.add_data("Hello world")
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())