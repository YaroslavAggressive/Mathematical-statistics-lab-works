import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt
from lab_source import least_squares_test, least_modulus_test


size = 20
x = np.linspace(-1.8, 2, size)
beta_0, beta_1 = 2, 2
error = normal(0, 1, size)
y = beta_0 + beta_1 * x  # built a reference dependence

# non-noisy linear regression
# res_1 = least_squares(mnk_function, [0, 0])
# print(res_1.x)

print("Regression without noise")
print("########################")

plt.plot(x, y + error, 'o', label='Original data', markersize=5)
# plt.plot(x, res_1.x[0] * x + res_1.x[1], label='Fitted line')
plt.plot(x, y, label='Fitted line')

beta_1, beta_0 = least_squares_test(x, y + error)
plt.plot(x, beta_1 * x + beta_0, label="MNK estim")
print("mnk_beta_0 = {}, mnk_beta_1 = {}".format(beta_0, beta_1))

beta_1, beta_0 = least_modulus_test(x, y + error)
plt.plot(x, beta_1 * x + beta_0, label="MNM estim")
print("mnm_beta_0 = {}, mnm_beta_1 = {}".format(beta_0, beta_1))

plt.legend()
plt.grid()
plt.title("Regression without noises")
plt.show()

# regression with noises
size = 20
x = np.linspace(-1.8, 2, size)
beta_0, beta_1 = 2, 2
error = normal(0, 1, size)
y = beta_0 + beta_1 * x  # built a reference dependence

# res_1 = least_squares(mnk_function, [0, 0])
# print(res_1.x)
print("Regression with noise")
print("#####################")

plt.plot(x, y, label='Fitted line')

noise = {0: 10,
         19: -10}  # noise in the regression function

for key in noise.keys():
    y[key] += noise.get(key)

plt.plot(x, y + error, 'o', label='Original data', markersize=5)
# plt.plot(x, res_1.x[0] * x + res_1.x[1], label='Fitted line')

beta_1, beta_0 = least_squares_test(x, y + error)
plt.plot(x, beta_1 * x + beta_0, label="MNK estim")
print("mnk_beta_0 = {}, mnk_beta_1 = {}".format(beta_0, beta_1))

beta_1, beta_0 = least_modulus_test(x, y + error)
plt.plot(x, beta_1 * x + beta_0, label="MNM estim")
print("mnm_beta_0 = {}, mnm_beta_1 = {}".format(beta_0, beta_1))

plt.legend()
plt.grid()
plt.title("Regression with noises")
plt.show()
