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


########################################################
# выборочное среднее из заданной выборки
def get_sample_mean(sample):
    x_ = 0
    for sample_i in sample:
        x_ += sample_i
    x_ /= len(sample)
    return x_


# выборочная медиана из заданной выборки
def get_sample_median(sample):
    if len(sample) % 2 == 0:
        return (sample[len(sample) // 2] + sample[len(sample) // 2 + 1]) / 2
    else:
        return sample[len(sample) // 2 + 1]


# полусумма экстремальных выборочных элементов выборки
def get_half_sum_extrem(sample):
    return (sample[0] + sample[len(sample) - 1]) / 2


# вычисление квартиля выборки порядка р
def get_quartile(sample, p):
    n = len(sample)
    if int(n * p) == n * p:
        return sample[int(n * p)]
    else:
        return sample[int(n * p) + 1]


# вычисление полусуммы квартилей выборки
def get_half_sum_quartiles(sample):
    z_1_4 = get_quartile(sample, 1/4)
    z_3_4 = get_quartile(sample, 3/4)
    return (z_1_4 + z_3_4) / 2


# вычисление усеченного среднего выборки
def get_truncated_mean(sample):
    r = math.floor(len(sample) / 4)  # берем приближенное значение, округляем вниз
    n = len(sample)
    z_tr = 0
    i = 0
    while i < n - r:
        z_tr += sample[r + i]
        i += 1
    return z_tr / (n - 2 * r)


# вычисление выборочной дисперсии выборки
def get_sample_variance(sample):
    x_ = get_sample_mean(sample)
    n = len(sample)
    D = 0

    for x_i in sample:
        D += (x_i - x_) ** 2

    return D / n


# вычисление дисперсии случайной величины
def get_dispersion(sample):
    disp = 0
    n = len(sample)
    sample_mean = get_sample_mean(sample)
    for i in range(n):
        disp += (sample[i] - sample_mean) ** 2
    return np.std(sample)**2
    # return disp / (n - 1)


########################################################


