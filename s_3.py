import pandas as

pdquint = pd.read_csv("/Users/shanametcalf/Desktop/PE-ratio1.csv")
quint[['PE_RATIO']] = quint[['PE_RATIO']].apply(lambda x: pd.to_numeric(x, errors='coerce'))
quint = quint.dropna(subset=['PE_RATIO'])
quint['percentile'] = quint.groupby(['INDUSTRY_SECTOR'])['PE_RATIO'].transform(lambda x: x.quintile(0.2))

