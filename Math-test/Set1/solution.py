import math
import numpy as np
import matplotlib.pyplot as plt

#=============================== Pure mathematics
def prob_random_triangle(a, b, c):
    # Write your code here
    ma = max(a, b)
    mi = min(a, b)
    if a + b <= c:
        denom = 1
        numer = 1
    elif (c >= mi)*(c <= ma):
        denom = c**2 - (c - mi)**2 # f"{2*a - 2*c + b}/{2*a}"
        numer = 2*a*b
    elif (c > ma) * (c <= a + b):
        denom = c**2 - (c - mi)**2 - (ma - c)**2 # f"{c**2 - (c - mi)**2 - (ma - c)**2}/{ 2*a*b }"
        numer = 2*a*b
    elif (c > 0) * (c < mi):
        denom = c**2 # f"{c**2}/{2*a*b}"
        numer = 2*a*b
    gcdf = math.gcd(denom, numer)
    return f"{denom // gcdf}/{numer // gcdf}"

#================================ Statistics & probability ===================================== #
# Stats.1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

# Stats.2
def illustration_triangle_from_stick():
    fig, ax = plt.subplots(1, 2, figsize=(20, 5))
    ax[0].plot([0, 2, 5, 0], [1, 4, 0, 1], '-')
    ax[0].plot([0, 2, 5], [1, 4, 0], 'o')
    ax[0].text(x=1, y=2, s='a')
    ax[0].text(x=3.2, y=2.5, s='b')
    ax[0].text(x=3, y=0.5, s='$\ell$ - a - b')
    ax[0].set_title("Length of stick = $\ell$")
    ax[1].plot([0, 1, 0, 0], [1, 0, 0, 1], '-')
    ax[1].plot([0, 1, 0], [1, 0, 0], 'o')
    ax[1].text(x=-.02, y=.95, s='$\ell$')
    ax[1].text(x=-.02, y=.5, s='$\ell$ / 2')
    ax[1].text(y=-.02, x=1.02, s='$\ell$')
    ax[1].text(y=-.02, x=0.52, s='$\ell$ / 2')
    ax[1].text(y=0.55, x=0.5, s='x + y = $\ell$')
    ax[1].text(y=0.25, x=0.2, s='x + y $\geq$ $\ell$ / 2')
    ax[1].plot([0, 0.5, 0.5, 0], [0.5, 0, 0.5, 0.5], '-')        
    ax[1].set_title("Illustration")
    plt.show()

# Stats.3
def determinant_unif_rvs():
    N_sample = 1000000
    EX = 0
    for k in range(N_sample):
        EX1 = np.random.rand()
        EX2 = np.random.rand()
        EX3 = np.random.rand()
        EX += EX1*EX3 - EX2**2
    return EX / N_sample
