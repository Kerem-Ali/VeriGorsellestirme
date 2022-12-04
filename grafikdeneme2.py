import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2,50)

plt.plot(x,x)
plt.plot(x,x**2,"g-.")

plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
plt.title("çizgi grafikleri")

plt.annotate("Kesikli",xy=(1.5,2.4),
             xytext=(1.0,2.5),
             arrowprops={"arrowstyle":"->",
                         "lw":2,"color":"green"})
plt.annotate("Doğrusal",
             xy=(0.45,0.5),
             xytext=(0.01,0.5),
             arrowprops=dict(arrowstyle="->",
                         lw=1,color="blue"))
plt.show()
