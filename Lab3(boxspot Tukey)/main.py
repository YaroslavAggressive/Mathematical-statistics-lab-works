from methods import get_poisson_sample, get_cauchy_sample, get_normal_sample, get_uniform_sample, get_laplace_sample
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import normal, standard_cauchy, poisson, laplace, uniform
from methods import normal_function, cauchy_function, laplace_function, poisson_function, uniform_function


sizes = [20, 100]
iterations = 1000

sample = get_cauchy_sample(sizes[0])

Q1 = np.percentile(sample, 25)
Q3 = np.percentile(sample, 75)

print(Q1)
print(Q3)

X1 = Q1 - 1.5 * (Q3 - Q1)
X2 = Q3 + 1.5 * (Q3 - Q1)

print(X1)
print(X2)


# Normal density
normals = []
for size in sizes:
    normal_sample = get_normal_sample(size)
    normals.append(normal_sample)

# чисто рисование
fig, ax = plt.subplots(1)
bp = plt.boxplot(normals, labels=["20", "100"], vert=False, patch_artist=True)
ax.set_title("Нормальное распределение", fontsize=16)
ax.set_xlabel("x")
ax.set_ylabel("n")
ax.grid()

for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(bp[element], color='black')
boxes = bp['boxes']
boxes[0].set(facecolor='orange')
boxes[1].set(facecolor='blue')
plt.show()


# Cauchy density
cauchies = []
for size in sizes:
    cauchy_sample = get_cauchy_sample(size)
    cauchies.append(cauchy_sample)

# чисто рисование
fig, ax = plt.subplots(1)
bp = plt.boxplot(cauchies, labels=["20", "100"], vert=False, patch_artist=True)
ax.set_title("Распределение Коши", fontsize=16)
ax.set_xlabel("x")
ax.set_ylabel("n")
ax.grid()

for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(bp[element], color='black')
boxes = bp['boxes']
boxes[0].set(facecolor='orange')
boxes[1].set(facecolor='blue')
plt.show()


# Laplace density
laplaces = []
for size in sizes:
    laplace_sample = get_laplace_sample(size)
    laplaces.append(laplace_sample)

# чисто рисование
fig, ax = plt.subplots(1)
bp = plt.boxplot(laplaces, labels=["20", "100"], vert=False, patch_artist=True)
ax.set_title("Распределение Лапласа", fontsize=16)
ax.set_xlabel("x")
ax.set_ylabel("n")
ax.grid()

for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(bp[element], color='black')
boxes = bp['boxes']
boxes[0].set(facecolor='orange')
boxes[1].set(facecolor='blue')
plt.show()


# Poisson density
poissons = []
for size in sizes:
    poisson_sample = get_poisson_sample(size, 10)
    poissons.append(poisson_sample)

# чисто рисование
fig, ax = plt.subplots(1)
bp = plt.boxplot(poissons, labels=["20", "100"], vert=False, patch_artist=True)
ax.set_title("Распределение Пуассона", fontsize=16)
ax.set_xlabel("x")
ax.set_ylabel("n")
ax.grid()

for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(bp[element], color='black')
boxes = bp['boxes']
boxes[0].set(facecolor='orange')
boxes[1].set(facecolor='blue')
plt.show()


# Uniform density
uniforms = []
for size in sizes:
    uniform_sample = get_uniform_sample(size)
    uniforms.append(uniform_sample)

# чисто рисование
fig, ax = plt.subplots(1)
bp = plt.boxplot(uniforms, labels=["20", "100"], vert=False, patch_artist=True)
ax.set_title("Равномерное распределение", fontsize=16)
ax.set_xlabel("x")
ax.set_ylabel("n")
ax.grid()

for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(bp[element], color='black')
boxes = bp['boxes']
boxes[0].set(facecolor='orange')
boxes[1].set(facecolor='blue')
plt.show()


# доли выбросов


for size in sizes:

    normal_blowout = []
    normal_p = []
    cauchy_blowout = []
    cauchy_p = []
    laplace_blowout = []
    laplace_p = []
    poisson_blowout = []
    poisson_p = []
    uniform_blowout = []
    uniform_p = []

    for i in range(iterations):
        normal_sample = get_normal_sample(size)
        cauchy_sample = get_cauchy_sample(size)
        laplace_sample = get_laplace_sample(size)
        poisson_sample = get_poisson_sample(size, 10)
        uniform_sample = get_uniform_sample(size)

        # normal sample
        Q1 = np.percentile(normal_sample, 25)
        Q3 = np.percentile(normal_sample, 75)
        X1 = Q1 - 1.5 * (Q3 - Q1)
        X2 = Q3 + 1.5 * (Q3 - Q1)

        # p = normal_function(X1) + (1 - normal_function(X2))
        # normal_p.append(p)

        sum = 0
        for x in normal_sample:
            if x < X1 or x > X2:
                sum += 1

        dolya = sum / len(normal_sample)
        normal_blowout.append(dolya)

        # cauchy sample

        Q1 = np.percentile(cauchy_sample, 25)
        Q3 = np.percentile(cauchy_sample, 75)
        X1 = Q1 - 1.5 * (Q3 - Q1)
        X2 = Q3 + 1.5 * (Q3 - Q1)

        # p = cauchy_function(X1) + (1 - cauchy_function(X2))
        # cauchy_p.append(p)

        sum = 0
        for x in cauchy_sample:
            if x < X1 or x > X2:
                sum += 1

        dolya = sum / len(cauchy_sample)
        cauchy_blowout.append(dolya)

        # laplace sample

        Q1 = np.percentile(laplace_sample, 25)
        Q3 = np.percentile(laplace_sample, 75)
        X1 = Q1 - 1.5 * (Q3 - Q1)
        X2 = Q3 + 1.5 * (Q3 - Q1)

        # p = laplace_function(X1) + (1 - laplace_function(X2))
        # laplace_p.append(p)

        sum = 0
        for x in laplace_sample:
            if x < X1 or x > X2:
                sum += 1

        dolya = sum / len(laplace_sample)
        laplace_blowout.append(dolya)

        # poisson sample

        Q1 = np.percentile(poisson_sample, 25)
        Q3 = np.percentile(poisson_sample, 75)
        X1 = Q1 - 1.5 * (Q3 - Q1)
        X2 = Q3 + 1.5 * (Q3 - Q1)

        # p = poisson_function(X1) + (1 - poisson_function(X2))
        # poisson_p.append(p)

        sum = 0
        for x in poisson_sample:
            if x < X1 or x > X2:
                sum += 1

        dolya = sum / len(poisson_sample)
        poisson_blowout.append(dolya)

        # uniform sample

        Q1 = np.percentile(uniform_sample, 25)
        Q3 = np.percentile(uniform_sample, 75)
        X1 = Q1 - 1.5 * (Q3 - Q1)
        X2 = Q3 + 1.5 * (Q3 - Q1)

        # p = uniform_function(X1) + (1 - uniform_function(X2))
        # uniform_p.append(p)

        sum = 0
        for x in uniform_sample:
            if x < X1 or x > X2:
                sum += 1

        dolya = sum / len(uniform_sample)
        uniform_blowout.append(dolya)

    d_normal = 0
    d_cauchy = 0
    d_laplace = 0
    d_poisson = 0
    d_uniform = 0

    for elem in normal_blowout:
        d_normal += elem
    d_normal /= len(normal_blowout)

    for elem in cauchy_blowout:
        d_cauchy += elem
    d_cauchy /= len(cauchy_blowout)

    for elem in laplace_blowout:
        d_laplace += elem
    d_laplace /= len(laplace_blowout)

    for elem in poisson_blowout:
        d_poisson += elem
    d_poisson /= len(poisson_blowout)

    for elem in uniform_blowout:
        d_uniform += elem
    d_uniform /= len(uniform_blowout)

    # sum = 0
    # for elem in normal_p:
    #     sum += elem
    # normal_p = sum / len(normal_p)
    #
    # sum = 0
    # for elem in cauchy_p:
    #     sum += elem
    # cauchy_p = sum / len(cauchy_p)
    #
    # sum = 0
    # for elem in laplace_p:
    #     sum += elem
    # laplace_p = sum / len(laplace_p)
    #
    # sum = 0
    # for elem in poisson_p:
    #     sum += elem
    # poisson_p = sum / len(poisson_p)
    #
    # sum = 0
    # for elem in uniform_p:
    #     sum += elem
    # uniform_p = sum / len(uniform_p)

    print("\n")
    print("\n")
    print("\n")
    print("normal, n = " + str(size) + ", D_blow = " + str(d_normal))
    print("cauchy, n = " + str(size) + ", D_blow = " + str(d_cauchy))
    print("laplace, n = " + str(size) + ", D_blow = " + str(d_laplace))
    print("poisson, n = " + str(size) + ", D_blow = " + str(d_poisson))
    print("uniform, n = " + str(size) + ", D_blow = " + str(d_uniform))
    # print("\n")
    # print("\n")
    # print("\n")
    # print("normal, n = " + str(size) + ", P_blow = " + str(normal_p))
    # print("cauchy, n = " + str(size) + ", P_blow = " + str(cauchy_p))
    # print("laplace, n = " + str(size) + ", P_blow = " + str(laplace_p))
    # print("poisson, n = " + str(size) + ", P_blow = " + str(poisson_p))
    # print("uniform, n = " + str(size) + ", P_blow = " + str(uniform_p))
