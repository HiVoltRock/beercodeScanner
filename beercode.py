import usb.core
import usb.util

def foundCode(barcode):
    print ("The barcode is: ")
    print (barcode)

#grab the barcode scanner
while True:
    try:
        code = int(input('Input:'))
        foundCode(code)
    except ValueError:
        print("Not a number")







