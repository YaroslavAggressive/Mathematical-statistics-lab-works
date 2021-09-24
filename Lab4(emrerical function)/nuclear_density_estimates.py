import matplotlib.pyplot as plt
import scipy.stats as scs
from scipy.stats import norm, cauchy, poisson, laplace, uniform
import numpy as np

SILVERMAN_METHOD_ID = 'silverman'

grid_size = 60
sizes = [20, 60, 100]
coefficients = [0.5, 1, 2]

# for Poisson distribution
poisson_left, poisson_right = 6, 14

# for other distributions
continuous_left, continuous_right = -4, 4


# Normal distribution
for coefficient in coefficients:
    fig = plt.figure()
    axes = [fig.add_subplot(1, 3, 1), fig.add_subplot(1, 3, 2), fig.add_subplot(1, 3, 3)]
    for size in sizes:
        sample = norm.rvs(size=size)
        x_normal = np.linspace(continuous_left, continuous_right, grid_size)
        normal_distribution = scs.norm.pdf(x_normal)  # здесь строится точное значение нормального распределения
        kernel = scs.gaussian_kde(sample, bw_method=SILVERMAN_METHOD_ID)
        kernel.set_bandwidth(bw_method=kernel.factor * coefficient)
        y_kernel = kernel(x_normal)

        axes[sizes.index(size)].set(title="Size = " + str(size))
        axes[sizes.index(size)].plot(x_normal, normal_distribution, color='blue')
        axes[sizes.index(size)].plot(x_normal, y_kernel, color='green')
        axes[sizes.index(size)].set_ylabel('Normal distribution, h_n = {}'.format(coefficient))
        axes[sizes.index(size)].set_xlabel('x')
        axes[sizes.index(size)].grid()
        plt.savefig('Normal distribution, h_n = {}'.format(coefficient) + '.png')
        plt.cla()

    # plt.show()


# Cauchy distribution
for coefficient in coefficients:
    fig = plt.figure()
    axes = [fig.add_subplot(1, 3, 1), fig.add_subplot(1, 3, 2), fig.add_subplot(1, 3, 3)]
    for size in sizes:
        sample = cauchy.rvs(size=size)
        x_cauchy = np.linspace(continuous_left, continuous_right, grid_size)
        cauchy_distribution = scs.cauchy.pdf(x_cauchy)  # здесь строится точное значение нормального распределения
        kernel = scs.gaussian_kde(sample, bw_method=SILVERMAN_METHOD_ID)
        kernel.set_bandwidth(bw_method=kernel.factor * coefficient)
        y_kernel = kernel(x_cauchy)

        axes[sizes.index(size)].set(title="Size = " + str(size))
        axes[sizes.index(size)].plot(x_cauchy, cauchy_distribution, color='blue')
        axes[sizes.index(size)].plot(x_cauchy, y_kernel, color='green')
        axes[sizes.index(size)].set_ylabel('Cauchy distribution, h_n = {}'.format(coefficient))
        axes[sizes.index(size)].set_xlabel('x')
        axes[sizes.index(size)].grid()
        plt.savefig('Cauchy distribution, h_n = {}'.format(coefficient) + '.png')
        plt.cla()
    # plt.show()

# Laplace distribution
for coefficient in coefficients:
    fig = plt.figure()
    axes = [fig.add_subplot(1, 3, 1), fig.add_subplot(1, 3, 2), fig.add_subplot(1, 3, 3)]

    for size in sizes:
        sample = laplace.rvs(size=size)
        x_laplace = np.linspace(continuous_left, continuous_right, grid_size)
        laplace_distribution = scs.laplace.pdf(x_laplace)  # здесь строится точное значение нормального распределения
        kernel = scs.gaussian_kde(sample, bw_method=SILVERMAN_METHOD_ID)
        kernel.set_bandwidth(bw_method=kernel.factor * coefficient)
        y_kernel = kernel(x_laplace)

        axes[sizes.index(size)].set(title="Size = " + str(size))
        axes[sizes.index(size)].plot(x_laplace, laplace_distribution, color='blue')
        axes[sizes.index(size)].plot(x_laplace, y_kernel,
                                     color='green')
        axes[sizes.index(size)].set_ylabel('Laplace distribution, h_n = {}'.format(coefficient))
        axes[sizes.index(size)].set_xlabel('x')
        axes[sizes.index(size)].grid()
        plt.savefig('Laplace distribution, h_n = {}'.format(coefficient) + '.png')
        plt.cla()
    # plt.show()

# Poisson distribution
for coefficient in coefficients:
    fig = plt.figure()
    axes = [fig.add_subplot(1, 3, 1), fig.add_subplot(1, 3, 2), fig.add_subplot(1, 3, 3)]
    for size in sizes:
        sample = poisson.rvs(mu=10, size=size)
        x_poisson = np.linspace(poisson_left, poisson_right, grid_size)
        poisson_distribution = scs.poisson.pmf(x_poisson, 10)
        # здесь строится точное значение нормального распределения
        kernel = scs.gaussian_kde(poisson_distribution, bw_method=SILVERMAN_METHOD_ID)
        kernel.set_bandwidth(bw_method=kernel.factor * coefficient)
        y_kernel = kernel(x_poisson)
        axes[sizes.index(size)].set(title="Size = " + str(size))
        axes[sizes.index(size)].plot(x_poisson, poisson_distribution, color='blue')
        axes[sizes.index(size)].plot(x_poisson, y_kernel,
                                     color='green')
        axes[sizes.index(size)].set_ylabel('Poisson distribution, h_n = {}'.format(coefficient))
        axes[sizes.index(size)].set_xlabel('x')
        axes[sizes.index(size)].grid()
        plt.savefig('Poisson distribution, h_n = {}'.format(coefficient) + '.png')
        plt.cla()
    # plt.show()

# Uniform distribution
for coefficient in coefficients:
    fig = plt.figure()
    axes = [fig.add_subplot(1, 3, 1), fig.add_subplot(1, 3, 2), fig.add_subplot(1, 3, 3)]
    for size in sizes:
        sample = uniform.rvs(size=size)
        x_uniform = np.linspace(continuous_left, continuous_right, grid_size)
        uniform_distribution = scs.uniform.pdf(x_uniform)  # здесь строится точное значение нормального распределения
        kernel = scs.gaussian_kde(sample, bw_method=SILVERMAN_METHOD_ID)
        kernel.set_bandwidth(bw_method=kernel.factor * coefficient)
        y_kernel = kernel(x_uniform)
        axes[sizes.index(size)].set(title="Size = " + str(size))
        axes[sizes.index(size)].plot(x_uniform, uniform_distribution, color='blue')
        axes[sizes.index(size)].plot(x_uniform, y_kernel,
                                     color='green')
        axes[sizes.index(size)].set_ylabel('Uniform distribution, h_n = {}'.format(coefficient))
        axes[sizes.index(size)].set_xlabel('x')
        axes[sizes.index(size)].grid()
        plt.savefig('Uniform distribution, h_n = {}'.format(coefficient) + '.png')
        plt.cla()
    # plt.show()
