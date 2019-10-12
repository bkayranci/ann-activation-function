# turkalp burak kayrancioglu - 150101011
import numpy as np
import matplotlib.pyplot as plt

# softplus fonksiyonu
def softplus(x):
    return np.log(1+np.exp(x))

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

plot(softplus, yaxis=(-0.4, 1.4))
plt.show()
