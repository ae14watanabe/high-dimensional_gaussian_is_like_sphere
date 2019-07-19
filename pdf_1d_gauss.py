import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    n_dimension = 1
    x = np.linspace(-4.0,4.0,100)
    p = np.exp(-0.5 * (x**2.0)) / np.sqrt(2.0*np.pi)

    plt.plot(x,p)
    plt.savefig('dimension{}.png'.format(n_dimension))
