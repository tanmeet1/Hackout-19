import pandas as pd

data = pd.read_csv("res/Multidata User Info1.csv")

print(data.head())

print(data.UID[data.UID==1])