#!/usr/bin/env python3

import requests ## 3rd party URL lookup
import os
## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=2018-06-01'  ## start date for data
    enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    mykey = f'&api_key={os.environ["NASA_API_KEY"]}' ## replace this with our API key

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)

## call main
main()

