import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#=============================== Numeric theory
def simulation_generated_nums(n_step: int, show_table: bool):
    """
        For each subset of k numbers, we have 3^k different combination, for example
            * With 1, we obtain {-1, 0, 1}
            * With 2, we obtain {-1, 0, 1} +/- 3 = {-4,-3,...,3,4}
            * With 3, we need {-4,...,4} +/- 3^2 = {-13,12,...,12,13}
            * With 4, then {-13,..,13} +/- 3^3 = {-40,-39,...,39,40}
    """
    init_set = set([-1,0,1])
    if show_table:
        print(f"|{45*'=': ^50}{'Show process as table': ^25}{45*'=': ^50}|")
        print(f"|{' Step ': ^6}|{'+/- ?? to.the.set.g.before': ^30}|{'Generated set': ^60}")
        print(f"|{5*'-': ^6}|{35*'-': ^30}|{80*'-': ^60}|")
    else:
        print(f"|{45*'=': ^45}{f'Generating process within {n_step} steps': ^25}{45*'=': ^45}|")
    for round in range(0, n_step+1):
        if round > 0:
            add_num = 3**round
            init_set = [e + add_num for e in init_set] + [e -add_num for e in init_set]            
        else:
            add_num = 0
        new_list = ','.join([str(x) for x in sorted(set(list(init_set)))])

        if show_table:
            print(f"|{round: ^6}|{add_num:^36}|{new_list: <60}")
        else:
            if round > 0:
                print(f"|* At step {round}, we will add {add_num} into the set generated before,\n|\tthen we obtain `{new_list}`")
            else:
                print("|* Initially (step 0), we consider `{-1, 0, 1}`")
        
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

# Stats. 4
def escape_cave_simulation():
    for example in range(3):
        N = 5 * (example + 1)
        time_try = 0
        print(f"Example {example+1} ==============================================")
        for n in range(N):
            prob_trial = np.random.rand()
            if prob_trial < 1/3:
                time_try += 3
                print(f"Successfully escape the cave after {n} failed turns [total: {time_try} hours]")
                break
            elif (prob_trial >= 1/3)*(prob_trial < 2/3):
                time_try += 2
                print(f"At {n} th trial, you drop back in the cave after 1hour travelling [total: {time_try} hours]")
                continue
            else:
                time_try += 1
                print(f"At {n} th trial, you drop back in the cave after 2hour travelling [total: {time_try} hours]")
                continue

def expectation_escape_cave(n_samples):
    def escape_simulation():
        N = 5000
        time_try = 0
        for n in range(N):
            prob_trial = np.random.rand()
            if prob_trial < 1/3:
                time_try += 3                
                break
            elif (prob_trial >= 1/3)*(prob_trial < 2/3):
                time_try += 2
                continue
            else:
                time_try += 1
                continue
        return time_try
    ls_trials = []
    for trial in range(n_samples):
        ls_trials.append( escape_simulation() )
    return sum(ls_trials) / n_samples

def illustration_curve(x, y, xlab, ylab, tit):
    plt.figure(figsize=(10, 3))
    plt.plot(x, y, '-')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(tit)
    plt.show()

def tossing_3HEAD_simulation(N=10):
    # Tossing coins N times
    ls = []    
    for _ in range(N):
        p = np.random.rand()
        ls.append('H' if p > 0.5 else 'T')
        res = ','.join(ls)
        # if
        if 'H,H,H' in res:
            break    
    return ls

def expect_time_get_3H_consec(n_samples):
    EX = 0
    for _ in range(n_samples):
        rs = tossing_3HEAD_simulation(50000)
        EX += len(rs) / n_samples
    return round(EX)

def inv_transform_rvs(f, f_inv, title, xmax=3):
    U = [np.random.uniform() for _ in range(10000)]
    X = [f_inv(u) for u in U]
    fig, ax = plt.subplots(1, 3, figsize=(20, 4))
    sns.distplot(U, ax=ax[0])
    ax[0].set_title("rvs of $\mathcal{U}(0,1)$")
    x_range = np.linspace(0, max(U), 101)
    ax[1].plot(x_range, [f_inv(u) for u in x_range], label='inverse of cdf')
    ax[1].plot([0,4],[0,4], '--', label='identity function y=x')
    ax[1].plot(np.linspace(0,5), [f(u) for u in np.linspace(0, 5)], label='cdf F(x)')
    ax[1].set_xlim(0, xmax)
    ax[1].set_ylim(0, xmax)    
    ax[1].set_title(title)
    ax[1].legend()
    sns.distplot(X, ax=ax[2])
    ax[2].set_title("rvs of $F^{-1}(\mathcal{U}(0,1))$")