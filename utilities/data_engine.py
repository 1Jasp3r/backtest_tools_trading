#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append('./')
from utilities.data_manager import ExchangeDataManager

exchange_name = "binance"

intervals = ["1h"]

# coin_to_dl = ["BTC/USDT", "ETH/USDT", "BNB/USDT", "XRP/USDT", "SOL/USDT"]
coin_to_dl = ['BTC/USDT']

exchange = ExchangeDataManager(
    exchange_name=exchange_name, 
    path_download="./database/exchanges"
)

await exchange.download_data(
    coins=coin_to_dl, 
    intervals=intervals
)


# In[2]:


exchange_name = "binance"

exchange = ExchangeDataManager(
    exchange_name=exchange_name, 
    path_download="./database/exchanges"
)

exchange.load_data(
    coin="BTC/USDT", 
    interval="1h"
)


# In[3]:


exchange.explore_data()

