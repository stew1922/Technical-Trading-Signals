# Data collector
## returns a dataframe with the daily BTC data from Yahoo

import pandas as pd
from pathlib import Path
from datetime import datetime

# Use this section to connect and parse out the data you want to use
# Right now, this is just pulling in historical daily BTC pricing from Yahoo.  
# In the future, this could be a function itself to connect to the websocket, web server, etc...
# datasource needs to include Date, Open, High, Low, Close and Volume
    # Date is set as the index, just FYI

def data_df():

    data = pd.read_csv(Path('../../data/btc_test_data.csv'), index_col='Date', parse_dates=True, infer_datetime_format=True)
    data.dropna(inplace=True)

    return data


