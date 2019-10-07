# turkalp burak kayrancioglu - 150101011
import numpy as np
import matplotlib.pyplot as plt

# relu fonksiyonu
def relu(x):
    return np.maximum(0.0, x)

X = np.linspace(-5, 5, 100)
plt.plot(X, relu(X), 'b')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Relu Fonksiyonu')
plt.grid()
plt.text(3, 0.8, r'$relu(x)=max(0.0, x)$', fontsize=16)
plt.show()
