import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt

Data = pd.read_excel('res/Multidata User Info1.xlsx',sheet_name=None)
userid = 2
print(Data.UID)
sleep_data = Data[Data["UID"] == userid]
x_axis = sleep_data.TimeStamp
y_axis = sleep_data.Steps
ax = sns.lineplot(x_axis,y_axis)
plt.plot()
ax.get_figure().savefig("res/step_data.png")
