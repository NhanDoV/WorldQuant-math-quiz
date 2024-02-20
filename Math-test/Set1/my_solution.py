import math
import numpy as np
import matplotlib.pyplot as plt

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

def determinant_unif_rvs(rank):
    list_matrices = [np.array([np.random.uniform(0,1,1) for _ in range(rank**2)]).reshape(rank, rank) for _ in range(5000)]
    list_det = [np.linalg.det(A) for A in list_matrices]
    return sum(list_det) / 5000
