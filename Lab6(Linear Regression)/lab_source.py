import numpy as np
from numpy.random import normal
from scipy import stats
from scipy.optimize import minimize
from math import fabs

size = 20
x = np.linspace(-1.8, 2, size)
sample = stats.norm(0, 1)
# error = sample.pdf(x)
error = normal(0, 1, size)
y = 2 + 2 * x + error  # built a reference dependence

noise = {0: 10,
         19: -10}  # noise in the regression function

# for key in noise.keys():
#     y[key] = noise.get(key)


def get_sign(a: float = 0., b: float = 0.) -> int:
    return -1 if a * b < 0 else 1


def mnk_function(beta):
    return sum([y - beta[0] - beta[1] * x])


def mnk_function_for_minimize(beta):
    return sum([fabs(y[i] - beta[0] - beta[1] * x[i]) for i in range(len(x))])


def least_squares_test(x_sample: np.ndarray, y_sample: np.ndarray) -> list:
    beta_1 = ((x_sample * y_sample).mean() - x_sample.mean() * y_sample.mean()) / ((x_sample * x_sample).mean()
                                                                                   - (x_sample.mean()) ** 2)
    beta_0 = y_sample.mean() - x_sample.mean() * beta_1
    return [beta_1, beta_0]


def least_modulus_test(x_sample: np.ndarray, y_sample: np.ndarray) -> list:
    betas = least_squares_test(x_sample, y_sample)
    solution = minimize(fun=mnk_function_for_minimize, x0=np.asarray(betas), method='BFGS')
    return list(solution.x)
