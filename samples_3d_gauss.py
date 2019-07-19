import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# import seaborn as sns

if __name__ == '__main__':
    n_samples = 10000
    mean = np.zeros(3)
    cov = np.identity(3)
    x = np.random.multivariate_normal(mean,cov,size=n_samples)

    fig =plt.figure(figsize=[5,5])
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(x[:,0],x[:,1],x[:,2],alpha=0.3)
    plt.savefig('3d_gaussian_samples.png')