import numpy as np
import matplotlib.pyplot as plt

b = np.linspace(0, 1, 1000)


def W_integral(b):
    g = 1/np.sqrt(1-b*b)
    I_1 = 1-b
    I_2 = np.log((g*(1 + b*b))/(1 + b))/(2*b) - np.log((1 - b)/(1 + b))/(4*b) + (1 - b)/(2*b) - (1 + b*b)/(2*b*(1 + b))
    I_3 = (1+b*b)/(2*(1+b)) + (b-1)/2 + b*np.log((1-b)/(1+b))/4 - b*np.log((g*(1+b*b))/(1+b))/2
    I_4 = np.log((1+b)/(1+b*b))/b - 1/b + (1+b*b)/(b*(1+b))
    return I_1 + I_2 + I_3 + I_4

W_array = W_integral(b)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_aspect('equal', adjustable='box')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid()
r_equal = 0.768079256355335044369928555784925495604
x_ticks = [0, 0.2, 0.4, 0.6, 0.8, r_equal, 1.]
x_ticks2 = ['0', '0.2', '0.4', '0.6', '0.8', r'$\beta_{eq}$', '1']
plt.xticks(x_ticks, x_ticks2, rotation=-20)
plt.ylabel(r"$P($"+"FlyDeath"+r"$)(\beta_p)$")
plt.xlabel(r"$\beta_p$")
plt.plot(b, W_array)
plt.savefig("FlyDeathMeanProbGraph.pdf", dpi=2000,
            bbox_inches='tight', pad_inches=0.0)