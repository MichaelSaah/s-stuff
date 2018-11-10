import pandas
from scipy import stats
import numpy as np

max_window = 240

df = pandas.read_csv('pairs-reg1.csv')
df['coeff'] = np.nan

for i in reversed(df.index):
    ticker_pair = df.loc[i, 'tickerPair']
    
    window = 1
    while window <= max_window and i-window > 1 and df.loc[i-window, 'tickerPair'] == ticker_pair:
        window+=1

    x = df.loc[i-window+1:i, 'Spread1.log']
    y = df.loc[i-window+1:i, 'Spread2.log']
    
    reg = stats.linregress(x, y)
    df.loc[i, 'coeff'] = reg.slope

print(df)
