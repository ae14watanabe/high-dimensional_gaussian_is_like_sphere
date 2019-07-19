import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    n_samples = 10000
    mean = np.zeros(2)
    cov = np.identity(2)
    x = np.random.multivariate_normal(mean,cov,size=n_samples)

    fig =plt.figure(figsize=[5,5])
    ax = fig.add_subplot(111,aspect='equal')
    ax.scatter(x[:,0],x[:,1],alpha=0.3)
    plt.savefig('2d_gaussian_samples.png')