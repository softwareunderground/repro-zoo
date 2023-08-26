#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy.optimize as so

rng = np.random.default_rng(999)

n = 26

x = np.linspace(0.5, 3.0, n) + 0.2 * rng.standard_normal(n)
y = 3 + 0.2 * np.exp(x) + 0.5 * rng.standard_normal(n)
e = np.abs(rng.standard_normal(n))


# In[2]:


def model(t, c0, c1):
    return  c0 + c1 * np.exp(t)

t = np.linspace(x.min(), x.max(), n)

(c0, c1), pcov = so.curve_fit(model, x, y, p0=(0, 0), method='lm')
y_hat_fit = model(t, c0, c1)

(c0, c1), pcov = so.curve_fit(model, x, y, p0=(0, 0), sigma=e, method='lm')
y_hat_fit_weighted = model(t, c0, c1)


# In[4]:


import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5))

params = {'elinewidth': 0.75,
          'capsize': 3,
          'markersize': 15,
          'markerfacecolor': 'C0',
          'markeredgewidth': 0.75,
         }

ax.errorbar(x, y, yerr=e, fmt='k.', label='Data with errors', **params)
ax.plot(t, y_hat_fit, 'r', label='Nonlinear least squares')
ax.plot(t, y_hat_fit_weighted, 'gold', label='Weighted nonlinear least squares')
ax.tick_params(direction="in")
ax.set_title('Comparison of unweighted and weighted fit', fontweight='bold')
ax.set_xlim(0, 3.5)
ax.set_xlabel('Depth in sediment [m]')
ax.set_ylim(0, 10)
ax.set_ylabel('Age of sediment [ka]')
ax.legend()

plt.savefig('Figure.svg')
plt.savefig('Figure.png', dpi=300)
plt.show()

