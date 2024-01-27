import numpy as np
import matplotlib.pyplot as plt

t_exact = 10.0
delta_t_values = 10.0**np.arange(-2, -20, -1) 
fdot_exact = np.exp(t_exact)
mistake = []
for delta_t in delta_t_values:
    fdot_approx = (np.exp(t_exact + delta_t) - np.exp(t_exact - delta_t)) / (2 * delta_t)
   
    mistake.append(np.abs(fdot_exact - fdot_approx))
plt.plot(delta_t_values, mistake, '--', label='mistake')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Delta_t')
plt.ylabel('Mistake')
plt.legend()
plt.show()
