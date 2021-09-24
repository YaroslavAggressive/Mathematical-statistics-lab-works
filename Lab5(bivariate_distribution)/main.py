import numpy as np
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from lab_methods import pearson_correlation, quadrant_correlation, eigsorted
from lab_methods import sample_mean, sample_dispersion, sample_quadratic_mean
sizes = [20, 60, 100]
iterations = 1000
rhos = [0.0, 0.5, 0.9]
means = [0, 0]  # for two normal distributions
cov_matrices = [[[1, rho], [rho, 1]] for rho in rhos]

sigmas = [1, 1]

nstd = 2

print("Counting Pearson correlation:")
print("################################")
pearson_coeffs = []
for size in sizes:
    fig = plt.figure()
    axes = [fig.add_subplot(1, 3, 1), fig.add_subplot(1, 3, 2), fig.add_subplot(1, 3, 3)]
    for index, cov_matrix in enumerate(cov_matrices):
        # for i in range(iterations):
        x, y = np.random.multivariate_normal(means, cov_matrix, size).T
        vals, vecs = eigsorted(cov_matrix)
        theta = np.degrees(np.arctan2(*vecs[:, 0][::-1]))
        w, h = 2 * nstd * np.sqrt(vals)
        ell = Ellipse(xy=(means[0], means[1]),
                      width=w, height=h,
                      angle=theta, color='black')
        ell.set_facecolor('none')
        axes[index].set(title="Rho = {}, size = {}".format(cov_matrix[0][1], size))
        axes[index].plot(x, y, "x")
        axes[index].add_artist(ell)
        axes[index].grid()
        axes[0].set_ylabel('Pearson correlation')
        # plt.show()
        pearson_coeffs.append(pearson_correlation(x, y, means[0], means[1]))
        # print("For n = {0}, rho = {1}, r_mean = {2}, r_quad_mean = {3}, r_disp = {4}".
        #       format(size, cov_matrix[0][1], sample_mean(pearson_coeffs), sample_quadratic_mean(pearson_coeffs),
        #              sample_dispersion(pearson_coeffs)))

    plt.savefig('Pearson correlation, size = {}'.format(size) + '.png')
    plt.cla()

print("\n")
print("Counting quadrant correlation:")
print("################################")
quadrant_coeffs = []
for size in sizes:
    fig = plt.figure()
    axes = [fig.add_subplot(1, 3, 1), fig.add_subplot(1, 3, 2), fig.add_subplot(1, 3, 3)]
    for index, cov_matrix in enumerate(cov_matrices):
        # for i in range(iterations):
        x, y = np.random.multivariate_normal(means, cov_matrix, size).T
        vals, vecs = eigsorted(cov_matrix)
        theta = np.degrees(np.arctan2(*vecs[:, 0][::-1]))
        w, h = 2 * nstd * np.sqrt(vals)
        ell = Ellipse(xy=(means[0], means[1]),
                      width=w, height=h,
                      angle=theta, color='black')
        ell.set_facecolor('none')
        axes[index].set(title="Rho = {}, size = {}".format(cov_matrix[0][1], size))
        axes[index].plot(x, y, "x")
        axes[index].add_artist(ell)
        axes[index].grid()
        axes[0].set_ylabel('Quadrant correlation')
        quadrant_coeffs.append(quadrant_correlation(x, y))
        # print("For n = {0}, rho = {1}, r_q_mean = {2}, r_q_quad_mean = {3}, r_q_disp = {4}".
        #       format(size, cov_matrix[0][1], sample_mean(pearson_coeffs), sample_quadratic_mean(pearson_coeffs),
        #              sample_dispersion(pearson_coeffs)))

    plt.savefig('Quadrant correlation, size = {}'.format( size) + '.png')
    plt.cla()

print("\n")
print("Counting Spearman correlation:")
print("################################")
spearman_coeffs = []
for size in sizes:

    fig = plt.figure()
    axes = [fig.add_subplot(1, 3, 1), fig.add_subplot(1, 3, 2), fig.add_subplot(1, 3, 3)]
    for index, cov_matrix in enumerate(cov_matrices):
        # for i in range(iterations):
        x, y = np.random.multivariate_normal(means, cov_matrix, size).T
        vals, vecs = eigsorted(cov_matrix)
        theta = np.degrees(np.arctan2(*vecs[:, 0][::-1]))
        w, h = 2 * nstd * np.sqrt(vals)
        ell = Ellipse(xy=(means[0], means[1]),
                      width=w, height=h,
                      angle=theta, color='black')
        ell.set_facecolor('none')
        axes[index].set(title="Rho = {}, size = {}".format(cov_matrix[0][1], size))
        axes[index].plot(x, y, "x")
        axes[index].add_artist(ell)
        axes[index].grid()
        axes[0].set_ylabel('Spearman correlation')
        spearman_coeffs.append(spearmanr(x, y)[0])
        # print("For n = {0}, rho = {1}, r_s_mean = {2}, r_s_quad_mean = {3}, r_s_disp = {4}".
        #       format(size, cov_matrix[0][1], sample_mean(spearman_coeffs), sample_quadratic_mean(spearman_coeffs),
        #              sample_dispersion(spearman_coeffs)))

    plt.savefig('Spearman correlation, size = {}'.format(size) + '.png')
    plt.cla()




