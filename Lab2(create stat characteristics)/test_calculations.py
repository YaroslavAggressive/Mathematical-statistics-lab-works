from methods import get_cauchy_sample, get_normal_sample, get_laplace_sample, get_poisson_sample, get_uniform_sample
from methods import get_sample_mean, get_quartile, get_sample_median, get_sample_variance, get_half_sum_quartiles
from methods import get_half_sum_extrem, get_truncated_mean, get_dispersion

sizes = [10, 100, 1000]
iterations = 1000

# Counting stat characteristics for Cauchy distribution

for size in sizes:
    cauchy_sample = get_cauchy_sample(size)
    x_ = []  # выборочное среднее
    med_x = []  # выборочная медиана
    z_R = []  # полусумма экстремальных выборочных элементов
    z_Q = []  # поусумма квартилей
    z_tr = []  # усеченное среднее

    D = []
    E = []

    for i in range(iterations):
        x_.append(get_sample_mean(cauchy_sample))
        med_x.append(get_sample_median(cauchy_sample))
        z_R.append(get_half_sum_extrem(cauchy_sample))
        z_Q.append(get_half_sum_quartiles(cauchy_sample))
        z_tr.append(get_truncated_mean(cauchy_sample))

    statistic_specifications = [x_, med_x, z_R, z_Q, z_tr]
    for lst in statistic_specifications:
        E.append(get_sample_mean(lst))
        D.append(get_dispersion(lst))
    print(E)
    print(D)

# Counting stat characteristics for Poisson distribution

for size in sizes:
    poisson_sample = get_poisson_sample(size, 10)
    x_ = []  # выборочное среднее
    med_x = []  # выборочная медиана
    z_R = []  # полусумма экстремальных выборочных элементов
    z_Q = []  # поусумма квартилей
    z_tr = []  # усеченное среднее

    D = []
    E = []

    for i in range(iterations):
        x_.append(get_sample_mean(poisson_sample))
        med_x.append(get_sample_median(poisson_sample))
        z_R.append(get_half_sum_extrem(poisson_sample))
        z_Q.append(get_half_sum_quartiles(poisson_sample))
        z_tr.append(get_truncated_mean(poisson_sample))

    statistic_specifications = [x_, med_x, z_R, z_Q, z_tr]
    for lst in statistic_specifications:
        E.append(get_sample_mean(lst))
        D.append(get_dispersion(lst))
    print(E)
    print(D)

# Counting stat characteristics for Laplace distribution

for size in sizes:
    laplace_sample = get_laplace_sample(size)
    x_ = []  # выборочное среднее
    med_x = []  # выборочная медиана
    z_R = []  # полусумма экстремальных выборочных элементов
    z_Q = []  # поусумма квартилей
    z_tr = []  # усеченное среднее

    D = []
    E = []

    for i in range(iterations):
        x_.append(get_sample_mean(laplace_sample))
        med_x.append(get_sample_median(laplace_sample))
        z_R.append(get_half_sum_extrem(laplace_sample))
        z_Q.append(get_half_sum_quartiles(laplace_sample))
        z_tr.append(get_truncated_mean(laplace_sample))

    statistic_specifications = [x_, med_x, z_R, z_Q, z_tr]
    for lst in statistic_specifications:
        E.append(get_sample_mean(lst))
        D.append(get_dispersion(lst))
    print(E)
    print(D)

# Counting stat characteristics for Normal distribution

for size in sizes:
    normal_sample = get_normal_sample(size)
    x_ = []  # выборочное среднее
    med_x = []  # выборочная медиана
    z_R = []  # полусумма экстремальных выборочных элементов
    z_Q = []  # поусумма квартилей
    z_tr = []  # усеченное среднее

    D = []
    E = []

    for i in range(iterations):
        x_.append(get_sample_mean(normal_sample))
        med_x.append(get_sample_median(normal_sample))
        z_R.append(get_half_sum_extrem(normal_sample))
        z_Q.append(get_half_sum_quartiles(normal_sample))
        z_tr.append(get_truncated_mean(normal_sample))

    statistic_specifications = [x_, med_x, z_R, z_Q, z_tr]
    for lst in statistic_specifications:
        E.append(get_sample_mean(lst))
        D.append(get_dispersion(lst))
    print(E)
    print(D)

# Counting stat characteristics for Uniform distribution

for size in sizes:
    uniform_sample = get_uniform_sample(size)
    x_ = []  # выборочное среднее
    med_x = []  # выборочная медиана
    z_R = []  # полусумма экстремальных выборочных элементов
    z_Q = []  # поусумма квартилей
    z_tr = []  # усеченное среднее

    D = []
    E = []

    for i in range(iterations):
        x_.append(get_sample_mean(uniform_sample))
        med_x.append(get_sample_median(uniform_sample))
        z_R.append(get_half_sum_extrem(uniform_sample))
        z_Q.append(get_half_sum_quartiles(uniform_sample))
        z_tr.append(get_truncated_mean(uniform_sample))

    statistic_specifications = [x_, med_x, z_R, z_Q, z_tr]
    for lst in statistic_specifications:
        E.append(get_sample_mean(lst))
        D.append(get_dispersion(lst))
    print(E)
    print(D)