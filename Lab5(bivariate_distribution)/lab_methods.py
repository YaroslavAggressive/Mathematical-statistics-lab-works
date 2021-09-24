import numpy as np
from math import sqrt
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt


def pearson_correlation(x_sample: list = [], y_sample: list = [],  x_mean: float = 0., y_mean: float = 0.) -> float:

    numerator = sum([(y_component - y_mean) * (x_component - x_mean) / len(x_sample) for x_component, y_component
                     in zip(x_sample, y_sample)])
    denominator = sqrt(sum((y_component - y_mean) ** 2 / len(y_sample) for y_component in y_sample)
                       * sum((x_component - x_mean) ** 2 / len(x_sample) for x_component in x_sample))

    return numerator / denominator


def quadrant_correlation(x_sample: list = [], y_sample: list = []) -> float:
    quadrants = count_quadrants(x_sample, y_sample)
    return ((quadrants[0] + quadrants[2]) - (quadrants[1] + quadrants[3])) / len(x_sample)


def count_quadrants(x_sample: list = [], y_sample: list = []) -> list:
    ns = [0, 0, 0, 0]

    for x, y in zip(x_sample, y_sample):
        if x > 0:
            if y > 0:
                ns[0] += 1
            else:
                ns[3] += 1
        else:
            if y > 0:
                ns[1] += 1
            else:
                ns[2] += 1

    return ns


def eigsorted(cov):
    values, vectors = np.linalg.eigh(cov)
    order = values.argsort()[::-1]
    return values[order], vectors[:, order]


def sample_mean(sample: list = []) -> float:
    return sum(sample) / len(sample)


def sample_quadratic_mean(sample: list = []) -> float:
    return sum([i**2 for i in sample]) / len(sample)


def sample_dispersion(sample: list = []) -> float:
    smpl_mean = sample_mean(sample)
    return sum([i**2 - smpl_mean for i in sample]) / len(sample)


def draw_scattering_ellipse():
    pass
