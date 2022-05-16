#pip install python-barcode

from barcode import EAN13
from barcode.writer import ImageWriter

number = '7702001148615'
my_code = EAN13(number, writer=ImageWriter())
my_code.save("new_code 2")