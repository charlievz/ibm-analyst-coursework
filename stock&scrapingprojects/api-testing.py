#%%
import yfinance as yf
import pandas as pd
import json

ups = yf.Ticker('UPS')
print(ups)
apple_info=None
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
ups_share_price_data = ups.history(period="10y")
ups_share_price_data
ups_share_price_data.reset_index(inplace=True)
ups_share_price_data.plot(x="Date", y="High")
ups.dividends.plot()

amd_info = None
with open('amd.json') as json_file:
    amd_info = json.load(json_file)
print(amd_info['Country'], amd_info['sector'], sep='\n')
