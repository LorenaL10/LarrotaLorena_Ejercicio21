import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0, 2*np.pi, 100)

plt.figure()
plt.plot(x, np.cos(x))
plt.title("coseno(x)")
plt.savefig('funcion.png')