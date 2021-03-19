import matplotlib.pyplot as plt
import numpy as np
import sys
L_pole = 0.78
L_barn = 1


# define relative speed of pole and farmer
beta_pole = 0.3
beta_farmer = 0.9

# Enables red square of death for the fly
FlyCheck = 0
# Enables the farmer x'' and t'' axes
PlotFarmer = 1

# Checks to see if rapidities are greater than 1
if abs(beta_pole) >= 1 or abs(beta_farmer) >= 1:
    sys.exit(f"\u03B2 = {beta_pole},{beta_farmer} >= 1. Lorentz factor is not defined.")

# Lorentz factor gamma for pole and farmer
g_pole = 1/np.sqrt(1 - beta_pole*beta_pole)
g_farmer = 1/np.sqrt(1 - beta_farmer*beta_farmer)

# Input x values, increase to larger value for more points on axes
num = np.arange(-50, 50+1)
# stretches the points for the S' and S'' reference frames appropriately
x_pole = g_pole*num
x_farmer = g_farmer*num
fig, ax = plt.subplots()

# Sets equal spacing, and introduces x, t grid.
ax.set_aspect('equal', adjustable='box')
# ax.grid()
# Restrict region of graph
Region = (-2, 5)
plt.ylim(Region)
plt.xlim(Region)

# Form of [Reference frame, left close, right close, left open, right open]
S_Array = [["S"], [0, L_pole/(g_pole*beta_pole)],
                  [L_barn, L_pole/(g_pole*beta_pole)],
                  [0, L_barn/beta_pole],
                  [L_barn, L_barn/beta_pole]]

S_Dash_Array = [["S\'"], [-L_pole, L_pole/beta_pole],
                         [g_pole*L_barn - L_pole,
                          L_pole/beta_pole - g_pole*beta_pole*L_barn],
                         [-g_pole*L_barn, g_pole*L_barn/beta_pole],
                         [0, g_pole*L_barn*(1/beta_pole - beta_pole)]]

S_D_Dash_Array = [["S\'\'"], [-g_farmer*beta_farmer*L_pole/(g_pole*beta_pole),
                              g_farmer*L_pole/(beta_pole*g_pole)],
                             [g_farmer*(L_barn - beta_farmer * L_pole / (g_pole*beta_pole)),
                              g_farmer*(L_pole/(g_pole*beta_pole) - beta_farmer*L_barn)],
                             [-g_farmer*beta_farmer*L_barn/beta_pole, g_farmer*L_barn/beta_pole],
                             [g_farmer*L_barn*(1 - beta_farmer/beta_pole),
                              g_farmer*L_barn*(1/beta_pole - beta_farmer)]]

# Creates a lightlike line of gradient m, through (x_0,y_0)
def CreateLightLine(m, x_0, y_0, col):
    c = y_0 - m*x_0
    ax.plot(num, m*num + c, color=col, linewidth=lightlikewidth)


# Plot Lightlike lines
lightlikewidth = 0.1
CreateLightLine(1, 0, 0, 'orange')
CreateLightLine(-1, 0, 0, 'orange')

# This mess of code produces the light-like lines and red square for the fly
if FlyCheck == 1:
    CreateLightLine(1, S_Array[1][0], S_Array[1][1], 'red')
    CreateLightLine(-1, S_Array[2][0], S_Array[2][1], 'red')
    CreateLightLine(-1, S_Array[3][0], S_Array[3][1], 'red')
    CreateLightLine(1, S_Array[4][0], S_Array[4][1], 'red')
    SquareTop = [L_barn/2, L_barn/2 + S_Array[1][1]]
    SquareLeft = [(-S_Array[1][1]+S_Array[3][1])/2, (S_Array[1][1]+S_Array[3][1])/2]
    SquareRight = [L_barn+(S_Array[2][1]-S_Array[3][1])/2, (S_Array[1][1]+S_Array[3][1])/2]
    SquareBot = [L_barn/2, -L_barn/2+S_Array[4][1]]
    plt.fill([SquareTop[0], SquareLeft[0], SquareRight[0]],
             [SquareTop[1], SquareLeft[1], SquareRight[1]], "r")
    plt.fill([SquareBot[0], SquareLeft[0], SquareRight[0]],
             [SquareBot[1], SquareLeft[1], SquareRight[1]], "r")

# Plot x' axis
ax.plot(x_pole, beta_pole*x_pole,
        color='green', marker='.',
        label=r"$\beta_p=$"+f"{np.round(beta_pole,2)}")

# Plot points at (gamma,0) and (0,gamma).
ax.plot(g_pole, 0, marker='x', color='blue')
ax.plot(0, g_pole, marker='x', color='blue')

# Doors shut
ax.plot(0, L_pole/(g_pole*beta_pole), marker='x', color='hotpink', label='Close')
ax.plot(L_barn, L_pole/(g_pole*beta_pole), marker='x', color='hotpink')

# Doors open

ax.plot(0, L_barn/(beta_pole), marker='x', color='crimson', label='Open')
ax.plot(L_barn, L_barn/(beta_pole), marker='x', color='crimson')

# Plot t' axis
ax.plot(x_pole*beta_pole, x_pole, color='green', marker='.')


if PlotFarmer == 1:
    # Plot x'' axis
    ax.plot(x_farmer, beta_farmer*x_farmer,
            color='purple', marker='.',
            label=r"$\beta_f=$"+f"{np.round(beta_farmer,2)}")
    # Plot t'' axis
    ax.plot(x_farmer*beta_farmer, x_farmer, color='purple', marker='.')

# Place y axis at zero
ax.spines['left'].set_position('zero')
# Place x axis at zero
ax.spines['bottom'].set_position('zero')
# Remove right line of graph
ax.spines['right'].set_color('none')
# Remove top line of graph
ax.spines['top'].set_color('none')

worldlinewidth = 0.5
# Plot barn back and front
plt.axvline(0, color='blue', linewidth=worldlinewidth)
plt.axvline(L_barn, color='blue', linewidth=worldlinewidth)

# Plot pole front and back
plt.plot(x_pole - L_pole/g_pole, x_pole/beta_pole,
         color='orange', linewidth=worldlinewidth)
plt.plot(x_pole, x_pole/beta_pole, color='orange', linewidth=worldlinewidth)
plt.title(r"$L_p/L_b=$"+f"{round(L_pole/L_barn,3)}")
plt.legend()
# Saves as a high quality png
plt.savefig("MinkowskiDiagram.png", dpi=1000,
            bbox_inches='tight', pad_inches=0.0)
# Saves as high quality pdf
plt.savefig("MinkowskiDiagram.pdf", bbox_inches='tight', pad_inches=0.0)
plt.show()

# Defines a matrix of all events.
Event_Matrix = [S_Array, S_Dash_Array, S_D_Dash_Array]

# Outputs into the console the reference frame and spacetime event coords
for X in Event_Matrix:
    event_names = ['LC', 'RC', 'LO', 'RO']
    alist = [X[1][1], X[2][1], X[3][1], X[4][1]]
    alist, event_names = zip(*sorted(zip(alist, event_names)))
    print(f"In reference frame {X[0]}")
    print(f"Left Close  {X[1]}")
    print(f"Right Close {X[2]}")
    print(f"Left Open   {X[3]}")
    print(f"Right Open  {X[4]}")
    print(event_names)
    print()
