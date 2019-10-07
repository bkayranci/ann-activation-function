# turkalp burak kayrancioglu - 150101011
import numpy as np
import matplotlib.pyplot as plt

# sigmoid fonksiyonu
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.linspace(-5, 5, 100)
plt.plot(X, sigmoid(X), 'b')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sigmoid Fonksiyonu')
plt.grid()
plt.text(4, 0.8, r'$\sigmoid(x)=\frac{1}{1+e^{-x}}$', fontsize=16)
plt.show()
