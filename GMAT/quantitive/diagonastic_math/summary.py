import math

# numeric
def prime_prod_add_1(n):
    """
    """
    def factorial(n):
        """
        """
        if n <= 1:
            return 1
        else:
            return n*factorial(n-1)
    return factorial(n) + 1

def count_n_exactly_m_digits(n_digits, m_digits, start_with=7):
    """
        Tìm các số nguyên có n chữ số, số bé nhất bắt đầu bởi k sao cho chỉ có đúng m chữ số bằng nhau.
        - Ví dụ n=2, m=2, số bé nhất bắt đầu bởi 2 (tức là tối thiểu 20) thì ta có
            count([22, 33, 44, 55, 66, 77, 88, 99])
        - n=3, m=2 và số bé nhất bắt đầu bởi 9 thì ta có    
            # Nếu 2 số lặp lại là 9 thì nó sẽ có dạng "9?9" hoặc "99?"
                * 909, 919, ..., 989 (ta không tính 999 vì nó có 3 số giống nhau)
                * 991, 992, ..., 998
            # Nếu 2 số lặp lại khác nhau và được bắt đầu bởi 9 thì sẽ có dạng 9xx với x khác 9
                * 900, 911, ..., 988
            Do đó ta được 27 trường hợp
        - n=3, m=2 và số bé nhất bắt đầu bởi 7, thì
            từ 900-999 đã có 27 cases, tương tự cho 800-899 và 700-799 có 27 cases cho mỗi range này, do đó ta có 81 cases
        =========================================================
        Constraints:
            1 < n < 5
            1 < m < 4
            1 <= k <= 9
        =========================================================
        Hãy thiết lập một program tối ưu nhất
        ========================================================
        Example
        >> res = count_n_exactly_m_digits(3, 2, 7)
            Có 81 số nguyên thỏa điều kiện số nguyên 3 chữ số có đúng 2 chữ số bằng nhau và bắt đầu bởi số bé nhất là 7
            The first 10 values found is:
            ['700', '707', '711', '717', '722', '727', '733', '737', '744', '747']
        >> res = count_n_exactly_m_digits(2, 2, 7)
            Có 9 số nguyên thỏa điều kiện số nguyên 2 chữ số có đúng 2 chữ số bằng nhau và bắt đầu bởi số bé nhất là 1
            The first 10 values found is:
            ['11', '22', '33', '44', '55', '66', '77', '88', '99']
        >> res = count_n_exactly_m_digits(2, 4, 7)
            ---------------------------------------------------------------------------
            ValueError                                Traceback (most recent call last)
            Cell In[44], line 1
            ----> 1 res = count_n_exactly_m_digits(2, 4, 1)

            Cell In[43], line 37, in count_n_exactly_m_digits(n_digits, m_digits, start_with)
                35     b = 10**n_digits
                36 else:
            ---> 37     raise ValueError("m_digits phải bé hơn hoặc bằng n_digits")
                39 # Initialize the list of results
                40 passed_list = []

            ValueError: m_digits phải bé hơn hoặc bằng n_digits        
        >> res = count_n_exactly_m_digits(5, 4, 7)
            Có 55890 số nguyên thỏa điều kiện số nguyên 5 chữ số có đúng 4 chữ số bằng nhau và bắt đầu bởi số bé nhất là 1
            The first 10 values found is:
            ['10001', '10010', '10011', '10012', '10013', '10014', '10015', '10016', '10017', '10018']        
    """
    if m_digits < n_digits:
        a = start_with * 10**m_digits
        b = 10**n_digits
    elif m_digits == n_digits:
        a = start_with * 10**(m_digits - 1)
        b = 10**n_digits
    else:
        raise ValueError("m_digits phải bé hơn hoặc bằng n_digits")
    
    # Initialize the list of results
    passed_list = []
    cnt = 0
    #==================================================
    from collections import Counter
    
    for x in range(a, b):
        str_num = str(x)
        count_list = Counter([n for n in str_num])
        vals = list(count_list.values())
        if 2 in vals:
            passed_list.append(str_num)
            cnt += 1
    print(f"Có {cnt} số nguyên thỏa điều kiện số nguyên {n_digits} chữ số có đúng {m_digits} chữ số bằng nhau và bắt đầu bởi số bé nhất là {start_with}")
    print("The first 10 values found is:\n", passed_list[:10])

    return cnt

#============================================================================================
def find_all_triangle_2given_edges(a, b, min_level, max_level, n_examples=1):
    """
        Tìm tất cả các cạnh nguyên của một tam giác, biết rằng
            * 2 cạnh được biết là a, b
            * cạnh c là một số nguyên nằm trong [min_level, max_level]
        output:
            đếm số các cạnh c thỏa điều kiện trên
            in ra một số ví dụ của nó (ít nhất n_examples ví dụ)
        >> find_all_triangle_2given_edges(6, 9, 11, 16, 5)
            Có 4 tam giác có các cạnh nguyên (6, 9) và cạnh còn lại thuộc đoạn [11, 16] 
            Minh họa với n_examples : 5
            [(6, 9, 11), (6, 9, 12), (6, 9, 13), (6, 9, 14)]
        >> find_all_triangle_2given_edges(69, 96, 110, 160, 8)
            Có 51 tam giác có các cạnh nguyên (69, 96) và cạnh còn lại thuộc đoạn [110, 160] 
            Minh họa với n_examples : 8
            [(69, 96, 110), (69, 96, 111), (69, 96, 112), (69, 96, 113), (69, 96, 114), (69, 96, 115), (69, 96, 116), (69, 96, 117)]
    """
    triag_list = []
    for c in range(min_level, max_level+1):
        if (c > abs(a-b)) * (c < a+b):
            triag_list.append((a, b, c))
    triag_list.sort(key=lambda a: a[2])
    print(f"Có {len(triag_list)} tam giác có các cạnh nguyên ({a}, {b}) và cạnh còn lại thuộc đoạn [{min_level}, {max_level}] ")
    print(f"Minh họa với n_examples : {n_examples}")
    print(triag_list[:n_examples])
    
    return len(triag_list)

#============================================================================================
def find_sum_cubed(n):
    """
        n: n_digits
        >> f(3)
        For 3 digits, we have these following numbers satisfied sum of power-3 each digits = whole number
            153
            370
            371
            407
        >> find_sum_cubed(4)
        For 4 digits, we have these following numbers satisfied sum of power-4 each digits = whole number
            1634
            8208
            9474
        >> find_sum_cubed(5)
        For 5 digits, we have these following numbers satisfied sum of power-5 each digits = whole number
            54748
            92727
            93084        
    """
    n_start = 10**(n - 1) 
    n_ended = 10**n - 1
    print(f"For {n} digits, we have these following numbers satisfied sum of power-{n} each digits = whole number")
    for num in range(n_start, n_ended):
        num_str = str(num)
        S = 0
        for k in num_str:
            S += int(k)**n
        if S == num:
            print(num)

#============================================================================================