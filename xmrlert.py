#!/usr/bin/env python3

# XMR price alerts using CoinMarketCap's API
# Goal: Create a script to send XMR value alerts via SMS
# server URL: https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest 
# Read the docs here: https://coinmarketcap.com/api/documentation/v1/#section/Endpoint-Overview 

from requests import Request, Session
import json
import pprint 
import os


# api_key = "place your coinmarket cap API key here"
url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"


def xmr_price(url) -> float:
    parameters = {
        "slug":"monero",
        "convert":"USD"
    }

    headers = {
        "Accepts":"application/json",
        "X-CMC_PRO_API_KEY":"place your coinmarket cap API key here"
    }

    session = Session()
    session.headers.update(headers)


    # Filter output for price output only
    response = session.get(url, params=parameters)
    pprint.pprint(json.loads(response.text)["data"]["328"]["quote"]["USD"]["price"])


xmr_price(url)
