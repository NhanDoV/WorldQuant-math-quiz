import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#=============================== Numeric theory
def right_triangle_triplets(limits):
    """
        Tìm 3 cạnh a,b,c của một tam giác vuông sao cho a,b,c <= given limits
        ===================
        Example
        >> right_triangle_triplets(25)
        ..............................
                3 4 5
                8 6 10
                5 12 13
                15 8 17
                12 16 20
                7 24 25
        =====================================================================
    """
    res = []
    c, m = 0, 2
    # Limiting c would limit  
    while c < limits :           
        # Now loop on n from 1 to m-1 
        for n in range(1, m) : 
            a = m * m - n * n 
            b = 2 * m * n 
            c = m * m + n * n 
  
            # if c is greater than 
            # limit then break it 
            if c > limits : 
                break
            res.append((a,b,c)) 
        m = m + 1
    return len(res)
        
def simulation_generated_nums(n_step: int, show_table: bool):
    """
        For each subset of k numbers, we have 3^k different combination, for example
            * With 1, we obtain {-1, 0, 1}
            * With 2, we obtain {-1, 0, 1} +/- 3 = {-4,-3,...,3,4}
            * With 3, we need {-4,...,4} +/- 3^2 = {-13,12,...,12,13}
            * With 4, then {-13,..,13} +/- 3^3 = {-40,-39,...,39,40}
        ===============================================
        Example
        >> simulation_generated_nums(3, True)
            |  =============================================      Show process as table     =============================================   |
            | Step |  +/- ?? to.the.set.g.before  |                       Generated set                        
            |----- |-----------------------------------|------------------------------------------------------------------------------------|
            |  0   |                 0                  |-1,0,1                                                      
            |  1   |                 3                  |-4,-3,-2,2,3,4                                              
            |  2   |                 9                  |-13,-12,-11,-7,-6,-5,5,6,7,11,12,13                         
            |  3   |                 27                 |-40,-39,-38,-34,-33,-32,-22,-21,-20,-16,-15,-14,14,15,16,20,21,22,32,33,34,38,39,40
            =================================================================================================================================
        >> simulation_generated_nums(4, False)
            |=============================================Generating process within 4 steps=============================================|
            |* Initially (step 0), we consider `{-1, 0, 1}`
            |* At step 1, we will add 3 into the set generated before,
            |	then we obtain `-4,-3,-2,2,3,4`
            |* At step 2, we will add 9 into the set generated before,
            |	then we obtain `-13,-12,-11,-7,-6,-5,5,6,7,11,12,13`
            |* At step 3, we will add 27 into the set generated before,
            |	then we obtain `-40,-39,-38,-34,-33,-32,-22,-21,-20,-16,-15,-14,14,15,16,20,21,22,32,33,34,38,39,40`
            |* At step 4, we will add 81 into the set generated before,
            |	then we obtain `-121,-120,-119,-115,-114,-113,-103,-102,-101,-97,-96,-95,-67,-66,-65,-61,-60,-59,-49,-48,-47,-43,-42,-41,41,42,43,47,48,49,59,60,61,65,66,67,95,96,97,101,102,103,113,114,115,119,120,121`
            =================================================================================================================================            
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
                
def slope_of_tangent_of_curve(x, y):
    """
         Xác định hệ số góc (slope) của đường thẳng tiếp tuyến với 
                     f(x,y)=xy^2 - 2xy + x^2y-12 
         tại (x,y)=(1,4)
    """
    def diff_f_x(x, y):
        return (y**2 - 2*y + 2*x*y)
    def diff_f_y(x, y):
        return (2*x*y - 2*x + x**2)
    
    return f"{-diff_f_x(x, y)}/{diff_f_y(x, y)}"

#=============================== Algorithms
def algorithm_1():
    """
        List all the output in this following scripts
    """
    for num in range(10, 12):
        for k in range(9, num):
            print(num * k)
            
def algorithm_2():
    """
        List all the output in this following scripts
    """
    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    A=0
    B=2
    while B < 30:
        if is_prime(B):
            A = A + 81
            print(A, B)
        B = B+1
        
def algorithm_3():
    """
        Find the output of this algorithms
    """
    A = 167
    B = 91
    C = 0
    while A-2 > B:
        A = A-2
        C = C+1
    return C

def algorithm_4():
    """
        Find the output of this algorithms
    """
    def f(x):
        r = 1
        for i in range(x+1):
            r = r+1
        return r

    return f(f(f(3)))

def algorithm_5():
    """
        Find the output of this algorithms
    """
    def func(x, y):
        return x*y/(x+y)
    n = 10
    res = func(2**(n-1), 2**(n))
    for k in range(8, 0, -1):
        print(k)
        res = func(res, 2**k)
    
    return res

def check_algo_order(n=1e3):
    """
      Với cùng một bài toán, giả sử ta có các thuật toán với các độ phức tạp như sau
      Example
      >> check_algo_order()

            Với n = 1000.0, thứ tự độ phức tạp của các thuật toán được sắp xếp tăng dần như sau:
            
            |======|========================================|========================================|
            | STT  |            complexity.level            |        complexity with n=1000.0        |
            |======|========================================|========================================|
            |  1   |       complexity_O(log(log(n)))        |           1.9326447339160655           |
            |......|........................................|........................................|
            |  2   |       complexity_O(sqrt(log(n)))       |           2.628260884878466            |
            |......|........................................|........................................|
            |  3   |       complexity_O(log(sqrt(n)))       |           3.4538776394910684           |
            |......|........................................|........................................|
            |  4   |          complexity_O(log(n))          |           6.907755278982137            |
            |......|........................................|........................................|
            |  5   |         complexity_O(sqrt(n))          |           31.622776601683793           |
            |......|........................................|........................................|
            |  6   |            complexity_O(n)             |                 1000.0                 |
            |......|........................................|........................................|
            |  7   |           complexity_O(n^2)            |               1000000.0                |
            |......|........................................|........................................|
            |  8   |           complexity_O(n^3)            |              1000000000.0              |
            |......|........................................|........................................|      
    """
    from math import log
    #------------ Ở đây ta xét khi giá trị n đủ lớn, do đó nếu n < 1 thì phải nhập lại
    if n < 1:
        raise ValueError("please input the value of n greater enough, such as 1e3(or 1000), 1e4, 5000")
    else:
        pass
    # -----------------------------------------
    order_by_n = [n**3, n**2, n, n**0.5, log(n), log(log(n)), log(n**0.5), (log(n)**0.5)]
    order_name = ['n^3', 'n^2', 'n', 'sqrt(n)', 'log(n)', 'log(log(n))', 'log(sqrt(n))', 'sqrt(log(n))']
    algo_name = [f"complexity_O({k})" for k in order_name]

    l = [(algo_name[k], order_by_n[k]) for k, va in enumerate(order_name)]
    l = sorted(l, key = lambda x: x[1])
    print(f"Với n = {n}, thứ tự độ phức tạp của các thuật toán được sắp xếp tăng dần như sau:")
    print(f"|{6*'=': ^6}|{40*'=': ^40}|{40*'=': ^40}|")
    print(f"|{'STT': ^6}|{'complexity.level': ^40}|{f'complexity with n={n}': ^40}|")
    print(f"|{6*'=': ^6}|{40*'=': ^40}|{40*'=': ^40}|")    
    for idx, (name, val) in enumerate(l):
        print(f"|{str(idx+1): ^6}|{name: ^40}|{str(val): ^40}|")
        print(f"|{6*'.': ^6}|{40*'.': ^40}|{40*'.': ^40}|")

#=============================== Pure mathematics
def prob_random_triangle(a, b, c):
    """
        Cho 3 cạnh của một tam giác a,b,c
        Lấy x, y là các số thực có phân phối đều với 
            x ~ U[0, a]
            y ~ U[0, b]            
        Tìm xác suất p sao cho x+y < c
    """
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
    """
        Tính giai thừa n!
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

# Stats.2
def illustration_triangle_from_stick():
    """
        Mô phỏng minh họa cho bài toán bẻ 1 que thành nhiều đoạn
    """
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
    """
        Thí nghiệm mô phỏng bài toán tìm định thức tạo bởi các BNN có phân phối đều
            A = [[X1 X2], [X2 X3]]
        với X1,X2,X3 độc lập
    """
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
    """
        Mô phỏng thí nghiệm một người bị nhốt trong 1 hang động,
        hang có 3 lối đi
        - 1 lối thoát sẽ mất 3 hours
        - 1 lối đi lòng vòng mất 2hours rồi trở về vị trí cũ
        - 1 lối đi lòng vòng mất 1hour rồi trở về vị trí cũ        
        ...............
        Hang tối và giả sử phượt thủ này không thấy đường để xác định và đánh dấu lối nào mình đã vừa đi qua
    """
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
    """
        Dựa trên function đã được định nghĩa escape_cave_simulation
        Ta sẽ tính kỳ vọng về số thời gian trung bình để phượt thủ này thoát khỏi hang đó
    """
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
    """
        Mô phỏng thí nghiệm tung một đồng xu liên tiếp N lần
        thực nghiệm chỉ dừng khi đã xuất hiện liên tiếp 3 đồng xu là mặt sấp
    """
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
    """
        Tính kỳ vọng trung bình số lần gieo để được 3 mặt sấp liên tiếp
    """
    EX = 0
    for _ in range(n_samples):
        rs = tossing_3HEAD_simulation(50000)
        EX += len(rs) / n_samples
    return round(EX)

def inv_transform_rvs(f, f_inv, title, xmax=3):
    """
        Xác định phân phối của nghịch ảnh từ một BNN có phân phối đều
    """
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