import matplotlib.pyplot as plt
import numpy as np
L_pole = 0.8
L_barn = 1
# define relative speed
x = np.linspace(0.2, 0.99, 2000)


def t_lc_dash(beta_p):
    return L_pole/beta_p


def t_rc_dash(beta_p):
    g_p = 1/(np.sqrt(1-beta_p*beta_p))
    return L_pole/beta_p - beta_p*g_p*L_barn


def t_lo_dash(beta_p):
    g_p = 1/(np.sqrt(1-beta_p*beta_p))
    return g_p*L_barn/beta_p


def t_ro_dash(beta_p):
    g_p = 1/(np.sqrt(1-beta_p*beta_p))
    return L_barn/(beta_p*g_p)


fig, ax = plt.subplots()
ax.plot(x, t_lc_dash(x), label=r"$\tau_{LC}'$")
ax.plot(x, t_rc_dash(x), label=r"$\tau_{RC}'$")
ax.plot(x, t_lo_dash(x), label=r"$\tau_{LO}'$")
ax.plot(x, t_ro_dash(x), label=r"$\tau_{RO}'$")

if L_pole < L_barn:
    beta_1 = np.sqrt(1 - (L_pole/L_barn)**2)
    print(f"\u03C4_RO = \u03C4_LC when \u03B2ₚ = {beta_1}")
    ax.plot(beta_1, t_ro_dash(beta_1), marker='x')

beta_2 = np.sqrt((L_pole*np.sqrt(4*L_barn**2 + L_pole**2)-L_pole**2)/2)/L_barn
print(f"\u03C4_RC = 0 when \u03B2ₚ = {beta_2}")
ax.plot(beta_2, 0, marker='x')

plt.title(r"$L_p/L_b=$"+f"{round(L_pole/L_barn,3)}")
# Place x axis at zero
ax.spines['bottom'].set_position('zero')
# Remove right line of graph
ax.spines['right'].set_color('none')
# Remove top line of graph
ax.spines['top'].set_color('none')
plt.xlim(0.2, 1)
plt.ylabel("\u03C4\'")
plt.legend()
plt.savefig("S_Dash_Time_Diagram.png", dpi=1000,
            bbox_inches='tight', pad_inches=0.0)
plt.savefig("S_Dash_Time_Diagram.pdf",
            bbox_inches='tight', pad_inches=0.0)
plt.show()
