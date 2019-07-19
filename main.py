import numpy as np
import matplotlib.pyplot as plt

def make_figures(n_dimension=2, n_samples=1000000):
    mean = np.zeros(n_dimension)
    cov = np.identity(n_dimension)
    x = np.random.multivariate_normal(mean,cov,size=n_samples)
    # calculate r, norm of x
    r = np.sqrt(np.sum(np.square(x),axis=1))

    # calculate theta, degree of x
    e = np.zeros(n_dimension) # unit vector
    e[0] = 1.0
    inner_products = np.einsum("d,nd->n",e,x)
    theta = np.arccos(inner_products / r) # 0 ~ pi
    # theta *= np.random.choice([1.0,-1.0],n_samples) # -pi ~ pi

    fig = plt.figure(figsize=[10,5])
    fig.suptitle("{} dimension".format(n_dimension))
    ax_hist_norm = fig.add_subplot(131)
    ax_hist_theta = fig.add_subplot(132)
    ax_polar = fig.add_subplot(133,aspect='equal')

    ax_polar.scatter(r * np.cos(theta), r * np.sin(theta))
    ax_polar.set_title("$(r\cos \theta,r\sin \theta)$")

    ax_hist_norm.hist(r,bins=50,range=(0,50))
    ax_hist_norm.set_title("histgram of norm $r$")

    ax_hist_theta.hist(theta,bins=50)
    ax_hist_theta.set_title("histgram of angle $\theta$")

    plt.show()

if __name__ == '__main__':
    seed = 100
    np.random.seed(seed)

    make_figures(2)
    list_n_dimension = [2,3,4]
    # for n_dimension in list_n_dimension:
    #     pass

