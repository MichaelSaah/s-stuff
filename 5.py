import pandas
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

max_window = 240

df = pandas.read_csv('pairs-reg1.csv')
df['coeff'] = np.nan # initialize coeff column with NaNs

for i in reversed(df.index): # loop through indicies backwards
    ticker_pair = df.loc[i, 'tickerPair']
    
    # set window size to largest possible value <= max_window
    # using trading days (indicies), not calendar days
    window = 1
    while window < max_window and i-window >= 0 and df.loc[i-window, 'tickerPair'] == ticker_pair:
        window+=1

    x = df.loc[i-window+1:i, 'Spread1.log']
    y = df.loc[i-window+1:i, 'Spread2.log']

    x = np.array(x)
    y = np.array(y)
    x = x[:,np.newaxis]    
    reg = np.linalg.lstsq(x, y)
    df.loc[i, 'coeff'] = reg[0]

    if reg[1].size > 0:
        df.loc[i, 'resid'] = reg[1][0]
    else:
        df.loc[i, 'resid'] = 0 # we can do this because we're forcing 0 y-intercept

# do zscores
df['zscore'] = df.groupby('tickerPair')['resid'].transform(stats.zscore)

print(df)

#plotting

styles = ['r-', 'b-', 'g-']
pairs = df['tickerPair'].unique()

plt.subplot(2, 1, 1)
for p, s in zip(pairs, styles):
    coeffs = df.loc[df['tickerPair'] == p]['coeff'].tolist()
    plt.plot(coeffs, s, label=p)
    plt.title('coefficients')

plt.subplot(2, 1, 2)
for p, s in zip(pairs, styles):
    zscores = df.loc[df['tickerPair'] == p]['zscore'].tolist()
    plt.plot(zscores, s, label=p)
    plt.title('z-scores')

plt.legend()
#plt.legend(bbox_to_anchor=(0, -0.2), loc=8, borderaxespad=0.)
plt.show()
