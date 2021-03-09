import matplotlib.pyplot as plt
import numpy as np
L_pole = 0.9464586434
L_barn = 1
r = L_pole/L_barn
# define relative speed
x = np.linspace(0, 1, 5000)
y = np.linspace(0, 1, 5000)
X, Y = np.meshgrid(x, y)


def t_lc_double_dash(beta_p, beta_f):
    g_f = 1/(np.sqrt(1-beta_f*beta_f))
    g_p = 1/(np.sqrt(1-beta_p*beta_p))
    return g_f*L_pole/(beta_p*g_p)


def t_rc_double_dash(beta_p, beta_f):
    g_f = 1/(np.sqrt(1-beta_f*beta_f))
    g_p = 1/(np.sqrt(1-beta_p*beta_p))
    return g_f*(L_pole/(g_p*beta_p) - beta_f*L_barn)


def t_lo_double_dash(beta_p, beta_f):
    g_f = 1/(np.sqrt(1-beta_f*beta_f))
    return g_f*L_barn/beta_p


def t_ro_double_dash(beta_p, beta_f):
    g_f = 1/(np.sqrt(1-beta_f*beta_f))
    return g_f*L_barn*(1/beta_p - beta_f)


fig = plt.figure()
T_LC = t_lc_double_dash(X, Y)
T_RO = t_ro_double_dash(X, Y)
output = np.greater(T_LC, T_RO)
plt.pcolormesh(X, Y, output, cmap='RdBu')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel(r"$\beta_p$")
plt.ylabel(r"$\beta_f$")
plt.title(r"$L_p/L_b=$"+f"{round(L_pole/L_barn,3)}")
plt.savefig("S_Double_Dash_Surface.png", dpi=2000,
            bbox_inches='tight', pad_inches=0.0)
plt.show()
