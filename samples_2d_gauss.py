import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    n_dimension = 2
    n_samples = 10000
    mean = np.zeros(n_dimension)
    cov = np.identity(n_dimension)
    x = np.random.multivariate_normal(mean,cov,size=n_samples)

    fig =plt.figure(figsize=[5,5])
    ax = fig.add_subplot(111,aspect='equal')
    ax.scatter(x[:,0],x[:,1],alpha=0.3)
    plt.savefig('dimension{}.png'.format(n_dimension))
