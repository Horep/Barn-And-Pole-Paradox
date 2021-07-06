import matplotlib.pyplot as plt
import numpy as np
L_barn = 1
# define relative speed
x = np.linspace(0, 1, 1000)
y = np.linspace(0, 1, 1000)
X, Y = np.meshgrid(x, y)

r = np.linspace(0, 1, 500)
i = 0

for L_pole in r:
    i += 1

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
    plt.axis('square')
    plt.xlabel(r"$\beta_p$")
    plt.ylabel(r"$\beta_f$")
    plt.title(r"$L_p/L_b=$"+f"{round(L_pole/L_barn,3)}")
    plt.savefig("S_Double_Dash_Surface"+f"{i}.png", dpi=1000,
                bbox_inches='tight', pad_inches=0.0)
    plt.close()
