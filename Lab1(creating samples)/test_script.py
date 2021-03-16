from scipy.stats import cauchy
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)

mean, var, skew, kurt = cauchy.stats(moments='mvsk')

def first_main_task():
    normal_distribution()  # normal distribution for all sizes
    cauchy_distribution()  # cauchy distribution for all sizes
    laplace_distribution()  # laplace distribution for all sizes
    poisson_distribution()  # poisson distribution for all sizes
    uniform_distribution()  # uniform distribution for all sizes


first_main_task()  # all generated samples from task (for 5 distributions)
