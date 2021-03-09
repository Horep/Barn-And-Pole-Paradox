import mpmath as mp
mp.mp.dps = 100


def probability(r):
    q = (1-r*r)/(1+r*r)
    return q + r*mp.sqrt(1 - q*q) - r*mp.asech(q)-mp.log(q) - 1/2


r_0 = mp.findroot(probability, 0.946, solver='anewton')
print(f"r_0 = {r_0}.")

print(f"probability(r_0) - 1/2 = {probability(r_0)}.")
