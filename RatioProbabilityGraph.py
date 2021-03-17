import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 1000)


def P(R):
    res = []
    for r in R:
        if 0 <= r < 1:
            val = 2*r*np.log(1+r) + (1 - r)*np.log(1 - r*r) - np.log(1 + r*r)
            res.append(val)
        elif r == 1:
            val = np.log(2)
            res.append(val)
    return np.array(res)


y = P(x)
y_2 = 1 - y
r_equal = 0.9464586434189278
r_mean = 0.67369968572800811
fig, ax = plt.subplots()
ax.plot(x, y, label=r"$P(\tau_{ro}'' < \tau_{lc}'')$", color='#1f77b4')
ax.plot(x, y_2, label=r"$P(\tau_{ro}'' > \tau_{lc}'')$", color='#d62728')
ax.plot(r_equal, 1/2, marker='x', color='black')
ax.plot(r_mean, P([r_mean]), marker='x', color='black')
ax.plot(r_mean, 1 - P([r_mean]), marker='x', color='black')
plt.xlabel(r"$r$")
plt.ylabel(r"$P$")
plt.xlim(0, 1)
plt.ylim(0, 1)
x_ticks = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, r_mean, 0.7, 0.8, 0.9, r_equal, 1.]
x_ticks2 = ['0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', r'$r_{mean}$',
            '0.7', '0.8', '0.9', r'$r_{equal}$', '1']
plt.xticks(x_ticks, x_ticks2, rotation=-40)
plt.yticks(np.arange(0, 1.1, step=0.1))
plt.legend()
plt.savefig("RatioProbability.png", dpi=1000,
            bbox_inches='tight', pad_inches=0.01)
plt.savefig("RatioProbability.pdf",
            bbox_inches='tight', pad_inches=0.01)
plt.show()
