import numpy as np
from random import random, seed
from math import atanh
import matplotlib.pyplot as plt

L_barn = 1
plt.ylim(0, 1)
numoflines = 100
Repeats = 6000+1
colormap = plt.cm.gist_ncar
plt.gca().set_prop_cycle(plt.cycler('color', plt.cm.jet(np.linspace(0, 1, numoflines))))
N = 3000
plt.xlim(0, Repeats+1)
for k in range(1, numoflines+1):
    count_count = []
    roll_avg = []
    for j in range(1, Repeats):
        seed()
        L_pole = random()

        def t_lc_double_dash(beta_p, beta_f):
            g_f = 1/(np.sqrt(1-beta_f*beta_f))
            g_p = 1/(np.sqrt(1-beta_p*beta_p))
            return g_f*L_pole/(beta_p*g_p)

        def t_ro_double_dash(beta_p, beta_f):
            g_f = 1/(np.sqrt(1-beta_f*beta_f))
            return g_f*L_barn*(1/beta_p - beta_f)

        count = 0
        for i in range(N):
            x = random()
            y = random()
            if t_ro_double_dash(x, y) - t_lc_double_dash(x, y) < 0:
                count = count + 1
        count_count.append(count/N)
        roll_avg.append(np.average(count_count))
    plt.plot(roll_avg, linewidth=0.05)
    print(f"{round(100*k/numoflines,2)}% completed.")
plt.xlabel('Step')
plt.ylabel(r'$P_{mean}$')
actualval = 1 + np.log(2) - np.pi/2
plt.plot([0, Repeats+1], [actualval, actualval], 'b--')
plt.savefig("probabilitygraph.pdf", bbox_inches='tight', pad_inches=0.0)
