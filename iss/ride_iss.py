#!/usr/bin/python3
"""Alta3 || Tracking ISS"""

import urllib.request
import json

##Define URL
MAJORTOM =  "http://api.open-notify.org/astros.json"

def main():
    ## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)
    
    ## PUT THE FILE OBJECT INTO HELMET
    helmet = groundctrl.read()

    ## decode JSON to Python data structure
    helmetson = json.loads(helmet.decode('utf-8'))

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    for p in people:
        print(f'{p["name"]} is  on the {p["craft"]}')
    print(people)


main()
