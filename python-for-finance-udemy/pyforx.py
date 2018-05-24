
# Imports
import pandas as pd
import numpy as np
import datetime as dt
import tulipy as ti
# import oandapyV20 as oa - UNNEEDED?
from time import sleep

# Oanda Package Imports
from oandapyV20 import API
import oandapyV20
from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20.contrib.requests import TakeProfitDetails, StopLossDetails
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.accounts as accounts

# TODO Add variables here


def get_account():
    """Get account information including balance and check for open orders. Only one order at a time so if there is an
    open order sleep for 5 mins then check again. If order was 1 and changes to zero check balance and if it's less
    than it was then iterate a counter. If counter reaches 3 in a 24 hour period exit the app. Once orders == 0
    continue onto strategy function"""
    pass


def strategy():
    """Define indicators here (i.e. Bollinger, RSI, MACD, Parabolic SAR) and pull info from Oanda on pair. Preferably
    at least 3. If the majority of indicators say to short/long then perform that operation. So define ordering here,
    short/long, risk (pass current account balance here), trailing stop. Pull candles here?"""
    pass

def make_order():
    """Place the order based on risk against balance. So define ordering here, short/long, risk (pass current account
    balance here), trailing stop, lot size."""
    pass


# Run the bot and kill it if kill switch is engaged
if __name__ == "__main__":
    pass
