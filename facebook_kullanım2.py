import numpy as np
import matplotlib.pyplot as plt
yil=np.arange(2012,2021)
kSay=[1056,1228,1393,1591,1860,2129,2320,2498,2797]

plt.plot(yil,kSay,"g^",alpha=0.5)
plt.step(yil,kSay,label="[2012-2020]")
plt.legend()

plt.title("Facebook aktif kullanıcı sayısı")
plt.show()
