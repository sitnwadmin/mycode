#!/usr/bin/env python3
import urllib.request
import json
import webbrowser
import os
from pprint import pprint as pp
## Define APOD
## define some constants

MYKEY = f"api_key={os.environ['NASA_API_KEY']}" ## this is our api key
NASAAPI = f"https://api.nasa.gov/planetary/apod?{MYKEY}" # this is our API to call
## pretty print json
def main():
    """run-time code"""
    nasaapiobj = urllib.request.urlopen(NASAAPI)  # call the webservice
    nasaread = nasaapiobj.read()  # parse the JSON blob returned
    convertedjson = json.loads(nasaread.decode('utf-8'))  # convert JSON

    # Show converted json
    print(convertedjson)  # show convereted JSON without pprint
    input('\nThis is converted json. Press ENTER to continue.')  # pause for enter

    # Show Pretty Print json
    pp(convertedjson)  # this is pretty print in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.')  # pause for ENTER

    # Print the description of the photo we are about to view
    print(convertedjson['explanation'])  # display the value for the key explanation
    print("Link to the APOD:", convertedjson['hdurl'])

    # input('\nPress ENTER to view this photo of the day') # pause for ENTER
    # webbrowser.open(convertedjson['hdurl']) # open in the webbrowser


main()
