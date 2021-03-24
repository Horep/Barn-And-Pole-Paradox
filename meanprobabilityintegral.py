import mpmath as mp
mp.mp.dps = 100


def probability(r):
    q = (1-r*r)/(1+r*r)
    return r*mp.asech(q)+mp.log(q)


meanprobability = mp.quad(probability, [0, 1], verbose=True)
print(f"mean probability = {meanprobability}.")


def mean_ratio(r):
    q = (1-r*r)/(1+r*r)
    return r*mp.asech(q)+mp.log(q) - meanprobability


r_mean = mp.findroot(mean_ratio, 0.7, solver='anewton', verbose=True)

print(f"r_mean = {r_mean}.")

print(f"mean_ratio(r_mean) - meanprobability = {mean_ratio(r_mean)}.")
