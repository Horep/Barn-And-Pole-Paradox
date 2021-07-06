import matplotlib.pyplot as plt
import numpy as np
L_pole = 1
L_barn = 1
r = L_pole/L_barn
crit = np.sqrt(1 - r*r)
# define relative speed
x = np.linspace(0.2, 1, 2000)


def t_lc_double_dash(beta_p):
    g_p = 1/(np.sqrt(1-beta_p*beta_p))
    return L_pole/(beta_p*g_p)


def t_rc_double_dash(beta_p):
    g_p = 1/(np.sqrt(1-beta_p*beta_p))
    return (L_pole/(g_p*beta_p))


def t_lo_double_dash(beta_p):
    return L_barn/beta_p


def t_ro_double_dash(beta_p):
    return L_barn/beta_p


fig, ax = plt.subplots()
ax.plot(x, t_lc_double_dash(x), label=r"$\tau_{LC}$")
ax.plot(x, t_rc_double_dash(x), label=r"$\tau_{RC}$")
ax.plot(x, t_lo_double_dash(x), label=r"$\tau_{LO}$")
ax.plot(x, t_ro_double_dash(x), label=r"$\tau_{RO}$")


plt.xlabel(r"$\beta_p$")
plt.ylabel(r"$\tau$")
plt.title(r"$L_p/L_b=$"+f"{round(L_pole/L_barn,3)}")
# Place x axis at zero
ax.spines['bottom'].set_position('zero')
# Remove right line of graph
ax.spines['right'].set_color('none')
# Remove top line of graph
ax.spines['top'].set_color('none')
plt.xlim(0.2, 1)
plt.ylim(-0.1, 5)
plt.legend()
plt.savefig("S_Time_Diagram.png", dpi=1000,
            bbox_inches='tight', pad_inches=0.0)
plt.savefig("S_Time_Diagram.pdf",
            bbox_inches='tight', pad_inches=0.0)
plt.show()
