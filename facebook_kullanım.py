import numpy as np
import matplotlib.pyplot as plt
yil=np.arange(2012,2021)
kSay=[1056,1228,1393,1591,1860,2129,2320,2498,2797]
ax=plt.bar(yil,kSay,color="lightgray",edgecolor="black")

for p in ax:
    plt.annotate(p.get_height(),
               xy=(p.get_x()+p.get_width()/2,p.get_height()),
               xytext=(0,9),
               textcoords="offset points",
               ha="center",va="center")


plt.xlabel("(Yıl)")
plt.ylabel("(Milyon)")
plt.title("Facebook aktif kullanıcı sayısı")
plt.show()
