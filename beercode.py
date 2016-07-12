import usb.core
import usb.util

#function executes when a barcode is scanned
def foundCode(barcode):
    print ("The barcode is: ")
    print (barcode)

#grab the barcode scanner
while True:
    try:
        code = int(input('Input:'))
        foundCode(code)
    except:
        print("Problem in main True loop. Barcode likely not an integer")
