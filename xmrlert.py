#!/usr/bin/env python3

"""
XMR price alerts using CoinMarketCap's API.

SYNOPSIS
========

::

   python3 xmrlert.py

DESCRIPTION
===========

Put your API Key on line 50. I made up the one below for visual representation.
If you use Linux you can place this script in /usr/bin and then,
Put it in your .bashrc ,(or .zshrc, if you're using the zsh shell).
Everytime you open a new Terminal window, you'll be greeted with the current value of XMR in USD.

This script can be edited to keep up with any crypto, not just XMR.
If so, you'll need to edit the parameters on line 43. And, regex the output on line 60.
And, probably want to change the name of the main function.

Resources:
server URL: https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest 
Read the docs here: https://coinmarketcap.com/api/documentation/v1/#section/Endpoint-Overview

"""
from requests import Request, Session
import json
import pprint 
import os

url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

# Main function.
def xmr_price(url) -> float:
    parameters = {
        "slug":"monero",
        "convert":"USD"
    }

    # Put your API Key on line 50. I made up the one below for visual representation.
    headers = {
        "Accepts":"application/json",
        "X-CMC_PRO_API_KEY":"X-CMC_PRO_API_KEY":"12345e6b-a789-1011-1ee2-131a12345678"
    }

    session = Session()
    session.headers.update(headers)
    # Filter output for price output only. 
    # This will need editing if you want to follow a different coin.
    response = session.get(url, params=parameters)
    pprint.pprint(json.loads(response.text)["data"]["328"]["quote"]["USD"]["price"])


if __name__=="__main__":
    xmr_price(url)
