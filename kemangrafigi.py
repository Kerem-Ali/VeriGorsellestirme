import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")
df=sns.load_dataset("tips")
sns.violinplot(x="day",y="tip",inner=None,linewidth=3,data=df)
sns.swarmplot(x="day",y="tip",hue="sex",palette=["k","w"],data=df)
plt.show()
