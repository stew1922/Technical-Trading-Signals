# # Exponential Weighted Moving Average
# ## creates an exponentially weighted moving average for signal generation
import pandas as pd
from pathlib import Path
from datetime import datetime
import numpy as np

def ewma():

    # Use this section to connect and parse out the data you want to use
    # Right now, this is just pulling in historical daily BTC pricing from Yahoo.  In the future, this could be a function itself to connect to the websocket, web server, etc...

    data = pd.read_csv(Path('../../data/btc_test_data.csv'), index_col='Date', parse_dates=True, infer_datetime_format=True)
    data.dropna(inplace=True)
    data.sort_index(ascending=False, inplace=True)

    # build out an exponential moving average
    # standard is to use windows of 9 and 13 for fast and slow, respectively
    # can tweak these later

    # EWMA 9
    window = 9
    halflife = 7
    ewma_fast = data.Close.ewm(span=window).mean()

    # EWMA 13
    window = 13
    halflife = 7
    ewma_slow = data.Close.ewm(span=window).mean()

    # Create a dataframe that consolidates and generates signal data
    # the signal column of the dataframe will be binary: 0 = bearish, 1 = bullish
        # 0 is bearish in the condition that the fast ewma is below or equal to the slow ewma
        # 1 is bullish in the condiditon that the fast ewma is above the slow ewma
    signal_df = pd.DataFrame(
        {
        'asset': data.Close, 
        'fast_ewma': ewma_fast, 
        'slow_ewma': ewma_slow, 
        'ewma_diff': ewma_fast - ewma_slow
        }
        )

    signal_df['signal'] = signal_df.ewma_diff.apply(lambda x: 1 if x > 0 else 0)

    return signal_df.signal[0]


