import pandas as pd

data = pd.read_csv("res/Multidata User Info1.csv")

print(data.head())

print(data[data.UID==1])

print(data.TimeStamp)