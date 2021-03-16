from scipy.stats import cauchy
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)

mean, var, skew, kurt = cauchy.stats(moments='mvsk')

x = np.linspace(cauchy.ppf(0.01),
                cauchy.ppf(0.99), 100)
ax.plot(x, cauchy.pdf(x),
       'r-', lw=5, alpha=0.6, label='cauchy pdf')
plt.show()