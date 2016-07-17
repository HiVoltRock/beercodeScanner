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
    print("Calling API with UPC "+UPC+":")

    #API call
    req = requests.get(URL+"search/upc?code="+UPC+"&key="+API_KEY+"&format=json")
    data = req.json()

    #print output of call for testing purposes
    print("API call resulted in: ")
    print(data)

# function executes when a barcode is scanned
def foundCode(UPC):
    print("The barcode from the scanner is: ")
    print(UPC)
    beerdb(UPC)


#Main() equivalent starts here
# grab the barcode scanner
while True:
    try:
        UPC = int(input('Input:'))
        foundCode(UPC)
    except:
        print("Problem in main True loop. Barcode likely not an integer")
