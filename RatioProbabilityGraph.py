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
fig, ax = plt.subplots()
ax.plot(x, y, label=r"$P(\tau_{ro}'' < \tau_{lc}'')$", color='#1f77b4')
ax.plot(x, y_2, label=r"$P(\tau_{ro}'' > \tau_{lc}'')$", color='#d62728')
plt.xlabel(r"$r$")
plt.ylabel(r"$P$")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xticks(np.arange(0, 1.1, step=0.1))
plt.yticks(np.arange(0, 1.1, step=0.1))
plt.legend()
plt.savefig("RatioProbability.png", dpi=1000,
            bbox_inches='tight', pad_inches=0.0)
plt.savefig("RatioProbability.pdf",
            bbox_inches='tight', pad_inches=0.0)
plt.show()
