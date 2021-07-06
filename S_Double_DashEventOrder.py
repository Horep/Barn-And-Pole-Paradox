import matplotlib.pyplot as plt
import numpy as np
L_pole = 0.8
L_barn = 1
beta_f = 0.7
g_f = 1/np.sqrt(1 - beta_f*beta_f)
r = L_pole/L_barn
crit = np.sqrt(1 - r*r)
# define relative speed
x = np.linspace(0.2, 1, 2000)


def t_lc_double_dash(beta_p):
    g_p = 1/(np.sqrt(1-beta_p*beta_p))
    return g_f*L_pole/(beta_p*g_p)


def t_rc_double_dash(beta_p):
    g_p = 1/(np.sqrt(1-beta_p*beta_p))
    return g_f*(L_pole/(g_p*beta_p) - beta_f*L_barn)


def t_lo_double_dash(beta_p):
    return g_f*L_barn/beta_p


def t_ro_double_dash(beta_p):
    return g_f*L_barn*(1/beta_p - beta_f)


fig, ax = plt.subplots()
ax.plot(x, t_lc_double_dash(x), label=r"$\tau_{LC}''$")
ax.plot(x, t_rc_double_dash(x), label=r"$\tau_{RC}''$")
ax.plot(x, t_lo_double_dash(x), label=r"$\tau_{LO}''$")
ax.plot(x, t_ro_double_dash(x), label=r"$\tau_{RO}''$")

if L_pole < L_barn:
    if abs(beta_f) > crit:
        print(f"\u03B2_f={beta_f} > sqrt(1-r^2) = {crit}, two roots.")
        discrim = r * np.sqrt(r * r - 1 + beta_f * beta_f)
        beta_1 = (beta_f + discrim)/(r*r + beta_f * beta_f)
        beta_2 = (beta_f - discrim)/(r*r + beta_f * beta_f)
        ax.plot(beta_1, t_ro_double_dash(beta_1), marker='x', color='black')
        print(f"\u03C4_RO\'\' = \u03C4_LC\'\' when \u03B2ₚ = {beta_1}")
        ax.plot(beta_2, t_ro_double_dash(beta_2), marker='x', color='black')
        print(f"\u03C4_RO\'\' = \u03C4_LC\'\' when \u03B2ₚ = {beta_2}")
    if abs(beta_f) == crit:
        print(f"\u03B2_f={beta_f} = sqrt(1-r^2) = {crit}, one root.")
        beta_1 = (beta_f)/(r*r + beta_f * beta_f)
        ax.plot(beta_1, t_ro_double_dash(beta_1), marker='x', color='black')
        print(f"\u03C4_RO\'\' = \u03C4_LC\'\' when \u03B2ₚ = {beta_1}")
elif L_pole == L_barn:
    beta_1 = (2*beta_f)/(1 + beta_f * beta_f)
    ax.plot(beta_1, t_ro_double_dash(beta_1), marker='x', color='black')
    print(f"\u03C4_RO\'\' = \u03C4_LC\'\' when \u03B2ₚ = {beta_1}")


plt.xlabel(r"$\beta_p$")
plt.ylabel(r"$\tau''$")
plt.title(r"$L_p/L_b=$"+f"{round(L_pole/L_barn,3)}"
          + r"$, \beta_f=$"+f"{beta_f}")
# Place x axis at zero
ax.spines['bottom'].set_position('zero')
# Remove right line of graph
ax.spines['right'].set_color('none')
# Remove top line of graph
ax.spines['top'].set_color('none')
plt.xlim(0.2, 1.005)
plt.ylim(-1, 6)
plt.legend()
plt.savefig("S_Double_Dash_Time_Diagram2.png", dpi=1000,
            bbox_inches='tight', pad_inches=0.0)
plt.savefig("S_Double_Dash_Time_Diagram.pdf",
            bbox_inches='tight', pad_inches=0.0)
plt.show()
