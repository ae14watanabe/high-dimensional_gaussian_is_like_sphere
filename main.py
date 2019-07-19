import numpy as np
import matplotlib.pyplot as plt

n_samples = 10000
max_dimension = 1000
step = 100
dimension_list = np.arange(0,max_dimension,step)
dimension_list[0] = 1
n_dimension = len(dimension_list)

seed = 100
np.random.seed(seed)

fig = plt.figure(figsize=[15,3*(max_dimension//5)])

for i,dim in enumerate(dimension_list):
    mean = np.zeros(dim)
    cov = np.identity(dim)
    x = np.random.multivariate_normal(mean,cov,size=n_samples)
    x_norm = np.sqrt(np.sum(np.square(x),axis=1))
    ax = fig.add_subplot(n_dimension // 5, 5, i+1)
    ax.set_title('dim={}\nanalytical mean={}'.format(dim,np.sqrt(2)))
    ax.hist(x_norm,bins=50,range=(0,50))

plt.show()