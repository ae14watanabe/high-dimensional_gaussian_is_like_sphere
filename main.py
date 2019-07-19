import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def make_figures(n_dimension=2, n_samples=100000, angle='random'):
    mean = np.zeros(n_dimension)
    cov = np.identity(n_dimension)
    x = np.random.multivariate_normal(mean,cov,size=n_samples)

    # calculate r, norm of x
    r = np.sqrt(np.sum(np.square(x),axis=1))

    # calculate theta, degree of x
    if angle == 'random':
        theta = np.random.uniform(-np.pi,np.pi,n_samples)
    elif angle == 'arccos':
        e = np.zeros(n_dimension) # unit vector
        e[0] = 1.0
        inner_products = np.einsum("d,nd->n",e,x)
        theta = np.arccos(inner_products / r) # 0 ~ pi
        theta *= np.random.choice([1.0,-1.0],n_samples) # -pi ~ pi

    fig = plt.figure(figsize=[10,5])
    fig.suptitle("{} dimension".format(n_dimension))

    ax_hist_norm = fig.add_subplot(121)
    ax_hist_norm.hist(r,bins=50,range=(0,75))
    ax_hist_norm.set_title("histgram of norm")

    ax_polar = fig.add_subplot(122,aspect='equal')
    ax_polar.scatter(r * np.cos(theta), r * np.sin(theta),alpha=0.3)
    ax_polar.set_title("polar cordinate")

    plt.savefig('dimension{}.png'.format(n_dimension))

if __name__ == '__main__':
    seed = 100
    np.random.seed(seed)

    list_n_dimension = [4,5,10,20,50,100,200,500,1000,2000,5000]
    for n_dimension in list_n_dimension:
        make_figures(n_dimension=n_dimension)

