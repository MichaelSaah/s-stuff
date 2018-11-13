import pandas as pd

munging = pd.read_csv("python-munging1.csv")
print(munging.head())

x = munging["CMATicker"] + '-' + munging["Tenor"].astype(str)
munging["ClientEntityId"].fillna(x)
if munging["InstrumentType"] == "Index" and munging["ClientEntityId"] == '':
    munging["ClientEntityId"].fillna(x)

print(munging.head())
