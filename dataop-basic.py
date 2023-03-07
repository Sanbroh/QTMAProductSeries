import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import math
import statistics
import scipy as sp
import random
from scipy.interpolate import interp1d
from scipy import interpolate
from scipy.signal import savgol_filter
from scipy.optimize import minimize, basinhopping, differential_evolution, fmin, curve_fit

x = np.linspace(0,1,1000)
f = 1/4

sine = np.sin(2*np.pi*f*x) + np.random.normal(scale=0.1, size=len(x))
plt.plot(sine)

poly = np.polyfit(x, sine, deg=5)

fig, ax = plt.subplots()
ax.plot(sine, label='data')
ax.plot(np.polyval(poly, x), label='fit')
ax.legend()

plt.show()
