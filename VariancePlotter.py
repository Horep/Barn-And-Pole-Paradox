import numpy as np
import matplotlib.pyplot as plt

numdensity = 100
print("Calculating input values")
b = np.linspace(0, 1, numdensity)
g = 1/np.sqrt(1-b*b)
r = np.linspace(0, 3, numdensity)
B, R = np.meshgrid(b, r)
guaranteed_death = np.sqrt((1-b)/(1+b))
middle_section = g * (1+b*b)/(1+b)


# def W(b, r):
#    g = 1/np.sqrt(1-b*b)
#    dark_middle = -g*b/2 - r/2
#    shift = 1/(2*b) * (g - r)
#    left_dark = -shift + dark_middle
#    right_dark = shift + dark_middle
#    right = np.minimum(0, right_dark)
#    left = np.maximum(-r, left_dark)
#    return np.maximum(0, right - left)

print("Calculating probabilities")
dark_middle = -g*B/2 - R/2
shift = 1/(2*B) * (g - R)
left_dark = -shift + dark_middle
right_dark = shift + dark_middle
# clear memory of dark_middle and shift
print("Clearing Memory")
dark_middle = None
shift = None
right = np.minimum(0, right_dark)
left = np.maximum(-R, left_dark)
# clear memory of left_dark and right_dark
print("Clearing Memory")
left_dark = None
right_dark = None

calculated_probability = 5*np.pi*np.pi/48 - np.log(2)/2
W_array = (np.maximum(0, right - left)/R - calculated_probability)**2
# clear memory of left, right, B, R
print("Clearing Memory")
left = None
right = None
B = None
R = None

plt.pcolormesh(b, r, W_array, cmap='inferno')
print("Drawing colormesh.")
plt.colorbar(label=r"Variance")
print("Plotting lines.")
plt.plot(b, g, linewidth=1, color='g', label=r'$\gamma_p$')
plt.plot(b, guaranteed_death, '#1f77b4', linewidth=1, label=r'$\sqrt{\frac{1-\beta_p}{1+\beta_p}}$')
plt.plot(b, middle_section, '#ff7f0e', linewidth=1, label=r'$\frac{\gamma_p(1+\beta_p^2)}{1+\beta_p}$')
plt.grid(linewidth=0.2)
plt.ylim(0, 3)
plt.xlim(0, 1)
plt.legend()
plt.xlabel(r'$\beta_p$')
plt.ylabel(r'$r$')
print("Saving image.")
plt.savefig("FlyDeathVarianceGraph.png", dpi=1000,
            bbox_inches='tight', pad_inches=0.0)
print("Done!")
