import numpy as np
from random import random
from math import atanh
L_pole = 0.946458643418927883671540044113170697616106528899307
L_barn = 1
r = L_pole/L_barn


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


def probability(r):
    if r < 1:
        q = (1-r*r)/(1+r*r)
        return q + r*np.sqrt(1 - q*q) - r*atanh(np.sqrt(1 - q*q))-np.log(q)
    elif r == 1:
        return 1 - np.log(2)


N = 500
count = 0
for i in range(N+1):
    x = random()
    y = random()
    if t_ro_double_dash(x, y) - t_lc_double_dash(x, y) > 0:
        count = count + 1

print(f"Experimental from {N} tests = {count/N}.")
print(f"Predicted value {probability(r)}.")
