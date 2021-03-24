import numpy as np
import matplotlib.pyplot as plt

b = np.linspace(0, 1, 10000)
g = 1/np.sqrt(1-b*b)
r = np.linspace(0, 3, 10000)
B, R = np.meshgrid(b, r)

# guaranteed_death = np.sqrt((1-b)/(1+b))
# middle_section = g * (1+b*b)/(1+b)
half_line1 = 1/g
half_line2 = (2*g)/(2+b)
half_line = np.minimum(half_line1, half_line2)


def W(b, r):
    g = 1/np.sqrt(1-b*b)
    dark_middle = -g*b/2 - r/2
    shift = 1/(2*b) * (g - r)
    left_dark = -shift + dark_middle
    right_dark = shift + dark_middle
    right = np.minimum(0, right_dark)
    left = np.maximum(-r, left_dark)
    return np.maximum(0, right - left)


W_array = W(B, R)/R
plt.pcolormesh(b, r, W_array, cmap='inferno')
plt.colorbar(label=r"$P($"+"Fly Death"+r"$)$")
plt.plot(b, g, linewidth=0.2, color='g')
# plt.plot(b, guaranteed_death, 'g', linewidth=0.2)
# plt.plot(b, middle_section, 'g', linewidth=0.2)
# plt.plot(b, half_line, linewidth=1, color='c')
plt.grid(linewidth=0.2)
plt.ylim(0, 3)
plt.xlim(0, 1)
plt.xlabel(r'$\beta_p$')
plt.ylabel(r'$r$')
plt.savefig("FlyDeathGraph.png", dpi=2000,
            bbox_inches='tight', pad_inches=0.0)
