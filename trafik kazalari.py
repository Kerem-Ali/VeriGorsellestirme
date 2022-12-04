import numpy as np
import matplotlib.pyplot as plt
yil=np.arange(2010,2021)
yarali=[211496,238074,268079,274829,285059,304421,303812,300383,
        307071,283234,226226]

olumlu=[4045,3835,3750,3685,3524,7530,7300,7427,6675,5473,4866]

plt.subplot(2,1,1)
plt.plot(yil,yarali,"b",label="yaralanmalı kazalar")
plt.subplot(2,1,2)
plt.plot(yil,olumlu,"r-.",label="ölümlü kazalar")
plt.legend()
plt.suptitle("trafik kazalari")
plt.tight_layout()
plt.xlabel("yillar")
plt.show()
