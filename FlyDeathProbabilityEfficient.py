import numpy as np
plot_histogram = 0
N = 5*100**4


def W(b, r):
    g = 1/np.sqrt(1-b*b)
    dark_middle = -g*b/2 - r/2
    shift = 1/(2*b) * (g - r)
    left_dark = -shift + dark_middle
    right_dark = shift + dark_middle
    right = np.minimum(0, right_dark)
    left = np.maximum(-r, left_dark)
    return np.maximum(0, right - left)


b_array = np.random.uniform(0, 1, N)
g_array = 1/np.sqrt(1 - b_array*b_array)
r_array = np.random.uniform(0, 1, N)*g_array

g_array = None

W_array = W(b_array, r_array)/(r_array)
b_array = None
r_array = None
print(np.average(W_array))
print(np.std(W_array))

if plot_histogram == 1:
    import matplotlib.pyplot as plt
    plt.grid(linewidth=0.2)
    plt.hist(W_array, bins=20, density=True, edgecolor='black', linewidth=1.2)
    plt.xlim(0, 1)
    plt.xticks(np.linspace(0, 1, 10+1))
    plt.xlabel(r"$W(\beta_{p,n},r_{n})/r_{n}$")
    plt.ylabel(r"Frequency")
    plt.yticks(np.linspace(0, 10, 10+1))

    plt.title(r"$N=$"+f"{N:.0e}")
    plt.savefig("FlyDeathHistogram.pdf", dpi=1000,
                bbox_inches='tight', pad_inches=0.0)
