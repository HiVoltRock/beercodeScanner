import requests

# static variables
API_KEY = "d29027a2a252328486a76ac7e586dd37"
URL = "http://api.brewerydb.com/v2/"
#test UPC for debug purposes. Should be Sierra Nevada Pale Ale
TEST_UPC = "736211628367"
UPC = ""


# pass the barcode into the BreweryDB API
def beerdb(UPC):
    # TODO: remove print statement
    print('in the beerdb method')

    #API call
    req = requests.get(URL+"search/upc?code="+UPC+"&key="+API_KEY+"&format=json")
    data = req.json()

    #print output of call for testing purposes
    print(data)

# function executes when a barcode is scanned
def foundCode(barcode):
    print("The barcode is: ")
    print(barcode)

    #having verified the barcode "works" we'll make the value the universal UPC
    UPC = str(barcode)
    beerdb(UPC)


#Main() equivalent starts here
# grab the barcode scanner
while True:
    try:
        scannedBarcode = input('Input:')
        scannedBarcode = int(scannedBarcode)
        foundCode(scannedBarcode)
    except:
        print("Problem in main True loop. Barcode likely not an integer")
