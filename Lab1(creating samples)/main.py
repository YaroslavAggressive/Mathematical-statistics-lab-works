#!/usr/bin/env python
# coding: utf-8

# In[62]:


import scipy.stats as sc
import numpy
import matplotlib.pyplot as plt
import math

# In[63]:


sizes = [10, 50, 1000]
distribNames = ["NormalDistribution", "CauchyDistribution", "LaplaceDistribution", "PoissonDistribution",
                "UniformDistribution"]
DENSITY, SIZE = "Density", "Size:"


def normal_distribution():
    fig = plt.figure()
    axes = [fig.add_subplot(1, 3, 1), fig.add_subplot(1, 3, 2), fig.add_subplot(1, 3, 3)]

    for size in sizes:
        dens = sc.norm(0, 1)
        hist = sc.norm.rvs(0, 1, size)
        x = numpy.linspace(dens.ppf(0.01), dens.ppf(0.99), 100)
        y = dens.pdf(x)  # processing Probability Density Function (PDF) on the interval
        axes[sizes.index(size)].set(title=SIZE + str(size))
        axes[sizes.index(size)].hist(hist, density=True, histtype='stepfilled', alpha=0.2, color='green')
        axes[sizes.index(size)].plot(x, y, color='black')

    plt.show()
    return


def cauchy_distribution():
    fig = plt.figure()
    axes = [fig.add_subplot(1, 3, 1), fig.add_subplot(1, 3, 2), fig.add_subplot(1, 3, 3)]

    for size in sizes:
        dens = sc.cauchy()
        hist = sc.cauchy.rvs(size=size)
        x = numpy.linspace(dens.ppf(0.01), dens.ppf(0.99), 100)
        y = dens.pdf(x)
        axes[sizes.index(size)].set(title=SIZE + str(size))
        axes[sizes.index(size)].hist(hist, density=True, histtype='stepfilled', alpha=0.2, color='green')
        axes[sizes.index(size)].plot(x, y, color='black')

    plt.show()
    return


def laplace_distribution():
    fig = plt.figure()
    axes = [fig.add_subplot(1, 3, 1), fig.add_subplot(1, 3, 2), fig.add_subplot(1, 3, 3)]

    for size in sizes:
        dens = sc.laplace(loc=0, scale=1 / math.sqrt(2))
        hist = sc.laplace.rvs(size=size, scale=1 / math.sqrt(2), loc=0)
        x = numpy.linspace(dens.ppf(0.01), dens.ppf(0.99), 100)
        y = dens.pdf(x)
        axes[sizes.index(size)].set(title=SIZE + str(size))
        axes[sizes.index(size)].hist(hist, density=True, histtype='stepfilled', alpha=0.2, color='green')
        axes[sizes.index(size)].plot(x, y, color='black')

    plt.show()
    return


def poisson_distribution():
    fig = plt.figure()
    axes = [fig.add_subplot(1, 3, 1), fig.add_subplot(1, 3, 2), fig.add_subplot(1, 3, 3)]

    for size in sizes:
        mu = 10  # value from task
        dens = sc.poisson(mu)
        hist = sc.poisson.rvs(mu, size=size)
        x = numpy.arange(dens.ppf(0.01), dens.ppf(0.99))
        y = dens.pmf(x)
        axes[sizes.index(size)].set(title=SIZE + str(size))
        axes[sizes.index(size)].hist(hist, density=True, histtype='stepfilled', alpha=0.2, color='green')
        axes[sizes.index(size)].plot(x, y, color='black')

    plt.show()
    return


def uniform_distribution():
    fig = plt.figure()
    axes = [fig.add_subplot(1, 3, 1), fig.add_subplot(1, 3, 2), fig.add_subplot(1, 3, 3)]

    for size in sizes:
        dens = sc.uniform(loc=0, scale=1)
        hist = sc.uniform.rvs(size=size, loc=0, scale=1)
        x = numpy.linspace(dens.ppf(0.01), dens.ppf(0.99), 100)
        y = dens.pdf(x)
        axes[sizes.index(size)].set(title=SIZE + str(size))
        axes[sizes.index(size)].hist(hist, density=True, histtype='stepfilled', alpha=0.2, color='green')
        axes[sizes.index(size)].plot(x, y, color='black')

    plt.show()
    return


def first_main_task():
    normal_distribution()  # normal distribution for all sizes
    cauchy_distribution()  # cauchy distribution for all sizes
    laplace_distribution()  # laplace distribution for all sizes
    poisson_distribution()  # poisson distribution for all sizes
    uniform_distribution()  # uniform distribution for all sizes


first_main_task()  # all generated samples from task (for 5 distributions)
