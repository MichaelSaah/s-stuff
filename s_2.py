munging = pd.read_csv("/Users/shanametcalf/Desktop/python-munging1.csv")
x = munging["CMATicker"] + '-' + munging["Tenor"].astype(str)
munging["ClientEntityId"].fillna(x)
if munging["InstrumentType"] == "Index" & munging["ClientEntityId"] == '':
    munging["ClientEntityId"].fillna(x)


