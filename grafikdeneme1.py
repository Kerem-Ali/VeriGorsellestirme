import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2,50)
plt.plot(x,x,label="Dogrusal")
plt.plot(x,x**2,"g-.",label="Kesikli")

plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
plt.title("çizgi grafiği")

plt.legend()
plt.show()
