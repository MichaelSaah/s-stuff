import pandas
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

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

styles = ['r-', 'b-', 'g-']
pairs = df['tickerPair'].unique()  
for p, s in zip(pairs, styles):
    coeffs = df.loc[df['tickerPair'] == p]['coeff'].tolist()
    plt.plot(coeffs, s, label=p)

plt.legend()
plt.show()
 

#xx = df.loc[0:240, 'Spread1.log']
#yy = df.loc[0:240, 'Spread2.log']
#plt.plot(xx, yy, 'b.')

#dom = np.arange(min(xx), max(xx), 0.2)
#plt.plot(dom, dom*df.loc[240, 'coeff'], 'r--')
#plt.show()
