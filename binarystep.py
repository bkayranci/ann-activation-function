# turkalp burak kayrancioglu - 150101011
import numpy as np
import matplotlib.pyplot as plt

# binary step fonksiyonu
def binary_step(x):
    return np.vectorize(lambda x: 1 if x > 0 else 0, otypes=[np.float])

x = np.arange(-5, 5, 0.01)
def plot(func, yaxis=(-1.4, 1.4)):
    plt.ylim(yaxis)
    plt.locator_params(nbins=5)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.axhline(lw=1, c='black')
    plt.axvline(lw=1, c='black')
    plt.grid(alpha=0.4, ls='-.')
    plt.box(on=None)
    plt.plot(x, func(x), c='r', lw=3)

plot(binary_step(x))
plt.show()
