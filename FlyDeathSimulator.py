import numpy as np
import matplotlib.pyplot as plt
from random import random

# Size of the danger markers used in the plot
marker_size_d = 300
marker_size_f = 20

# Number of trials
n = 7
N = 10**n

# Initialise deathcount
deathcount = 0

# Perform N trials
for i in range(1, N+1):
    # Generate random speed, pole ratio and fly position on pole
    b = random()
    g = 1/np.sqrt(1 - b*b)
    r = g*random()
    fly_pos = -r*random()
    dark_middle = -g*b/2 - r/2
    shift = 1/(2*b) * (g - r)
    x_A_dash = -shift + dark_middle
    x_B_dash = shift + dark_middle
    left_dark = max(-r, x_A_dash)
    right_dark = min(0, x_B_dash)

    # Calculate count
    if left_dark < fly_pos < right_dark:
        fly_color = 'r'
        fly_status = 'died'
        deathcount = deathcount + 1
    else:
        fly_color = 'g'
        fly_status = 'lived'
    if i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] or i % 10**(n-2) == 0:
        # Plot pole
        plt.plot([-r, 0], [0, 0])

        # Plot dangerous section edge markers
        plt.plot(left_dark, 0, marker='|', color="red", markersize=marker_size_d)
        plt.plot(right_dark, 0, marker='|', color="red", markersize=marker_size_d)

        # Plot dangerous section on pole
        plt.plot([left_dark, right_dark], [0, 0], color="red")
        plt.plot(fly_pos, 0, marker=7, markersize=marker_size_f, color=fly_color)
        plt.xlim([-r, 0])

        # Plot markers on the x' axis
        if -r < x_A_dash:
            x_ticks = [-r, x_A_dash, x_B_dash, 0]
            x_ticks2 = [r"$-r$", r"$x_{A}'$", r"$x_{B}'$", r"$0$"]
        elif x_B_dash < 0:
            x_ticks = [-r, x_B_dash, 0]
            x_ticks2 = [r"$-r$", r"$x_{B}'$", r"$0$"]
        else:
            x_ticks = [-r, 0]
            x_ticks2 = [r"$-r$", r"$0$"]

        plt.xticks(x_ticks, x_ticks2)
        plt.yticks([], [])
        plt.xlabel(r"$x'$")
        plt.title(f"beta = {round(b,5)},\n g={round(g,5)},\n fly {fly_status},\n r={round(r, 5)},\n deathcount ={deathcount}, \n count = {i},\n death chance = {round(deathcount/i,8)}.")
        plt.savefig(f"image{i}.png", dpi=200, bbox_inches='tight', pad_inches=0.0)
        plt.clf()
