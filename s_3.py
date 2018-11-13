import pandas as pd


quint = pd.read_csv("PE-ratio1.csv")
print(quint.head())

quint[['PE_RATIO']] = quint[['PE_RATIO']].apply(lambda x: pd.to_numeric(x, errors='coerce'))
quint = quint.dropna(subset=['PE_RATIO'])

for i in range(1, 5):
    quint['q'+str(i)] = quint.groupby(['INDUSTRY_SECTOR'])['PE_RATIO'].transform(lambda x: x.quantile(0.2*i))

print(quint.head())
