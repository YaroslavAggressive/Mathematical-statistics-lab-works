import scipy.stats as sc
import numpy as np
import math


def get_cauchy_sample(size):
    res = sc.cauchy.rvs(size=size)
    res.sort()
    return res


def get_laplace_sample(size):
    res = sc.laplace.rvs(loc=0, scale=1 / math.sqrt(2), size=size)
    res.sort()
    return res


def get_poisson_sample(size, mu):
    res = sc.poisson.rvs(mu, size=size)
    res.sort()
    return res


def get_uniform_sample(size):
    res = sc.uniform.rvs(loc=-math.sqrt(3), scale=2 * math.sqrt(3), size=size)
    res.sort()
    return res


def get_normal_sample(size):
    res = sc.norm.rvs(loc=0, scale=1, size=size)
    res.sort()
    return res


def normal_sample(x):
    return 1 / math.sqrt(2 * math.pi) * math.exp(-x**2/2)


def cauchy_sample(x):
    return 1 / (math.pi * (x**2 + 1))


def laplace_sample(x):
    pass


def poisson_sample(x):
    return (10 ** x) * math.exp(-10)  # не дописана


def uniform_sample(x):
    if math.fabs(x) <= math.sqrt(3):
        return 1 / (2 * math.sqrt(3))
    else:
        return 0


def normal_function(x):
    return 1 / math.sqrt(2 * math.pi) * math.exp(- x**2 / 2)


def cauchy_function(x):
    return 1 / (math.pi * (x**2 + 1))


def laplace_function(x):
    return 1 / math.sqrt(2) * math.exp(-math.fabs(x) * math.sqrt(2))


def poisson_function(x):
    return 10**x * math.exp(-10) / math.factorial(x)


def uniform_function(x):
    if math.fabs(x) < math.sqrt(3):
        return 1 / (2 * math.sqrt(3))
    else:
        return 0

