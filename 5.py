import pandas
from scipy import stats
import numpy as np

max_window = 240

df = pandas.read_csv('pairs-reg1.csv')
df['coeff'] = np.nan # initialize coeff column with NaNs

for i in reversed(df.index): # loop through indicies backwards
    ticker_pair = df.loc[i, 'tickerPair']
    
    # set window size to 240 if possible
    # use trading days (indicies), not calendar days
    window = 1
    while window < max_window and i-window > 1 and df.loc[i-window, 'tickerPair'] == ticker_pair:
        window+=1

    x = df.loc[i-window+1:i, 'Spread1.log']
    y = df.loc[i-window+1:i, 'Spread2.log']

    x = np.array(x)
    y = np.array(y)
    x = x[:,np.newaxis]    
    reg = np.linalg.lstsq(x, y)
    df.loc[i, 'coeff'] = reg[0]

print(df)
