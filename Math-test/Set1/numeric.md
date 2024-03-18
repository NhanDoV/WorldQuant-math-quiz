### 1. Chỉ sử dụng 2 phép toán là +, -. Hỏi ta cần ít nhất bao nhiêu số nguyên (mỗi số chỉ được xuất hiện một lần trong phép tính) để tạo ra các số từ 1-40.

**Giải**

```
    >> from solution import *
    >> simulation_generated_nums(3, show_table=True)        
```

Một cách tổng quát, để tạo ra các số nguyên từ $1$ đến $k$ thì ta cần ít nhất $m + 3$ số nguyên thỏa

$$ 2k+1 \leq \text{argmin}_{m} 3^{m+1} \Leftrightarrow m = \text{ceil}(\log_3 (2k+1)) - 1$$

Ví dụ, 
- $(1, 40)$ thì $k=40$ và $$ m = \text{ceil}(\log_3 (2*40 + 1)) - 1 = \text{ceil}(\log_3 (81)) - 1 = 3 $$ và ta cần $m+3=6$ số nguyên tất cả, bao gồm $$\lbrace 0, \pm 1, 3, 3^2, 3^3 \rbrace$$ 

- $(1, 90)$ thì $k=90$ và $$m = \text{ceil}(\log_3 (2*90 + 1)) - 1 = \log_3 (181) - 1 = 4$$ và ta cần $m+3=7$ số nguyên tất cả, bao gồm $$\lbrace 0, \pm 1, 3, 3^2, 3^3, 3^4 \rbrace$$ 

### 2. Hỏi có bao nhiêu tam giác vuông có cạnh nguyên bé hơn 2000?

**Giải**

Sử dụng ý tưởng sau (đã được viết lại bởi function `right_triangle_triplets` trong `solution.py`) $\forall a,b,c \in \mathbb{N} \text{ then } \exists m, n \in \mathbb{N} \text{ such that}$

$$ \begin{array}{ccl} a &=& m^2 - n^2 \\ b &=& 2mn \\ c &=& m^2 + n^2 \end{array}  $$

ý tưởng này đồng nghĩa với giả định rằng $m > n$ và $c$ là cạnh huyền

```
    >> from solution import *
    >> right_triangle_triplets(2000)
    
     526
```
Như vậy có 526 tam giác vuông có cạnh nguyên bé hơn 2000.

### 3. Xác định hệ số góc (slope) của đường thẳng tiếp tuyến với $f(x,y)=xy^2 - 2xy + x^2y-12$ tại $(1,4)$.

**Giải**
- Ta có:

$ \qquad \diamond f'_x (x,y) = y^2-2y + 2xy$ và

$ \qquad \diamond f'_y (x,y) = 2xy - 2x + x^2$

- Đầu tiên, dễ kiểm tra rằng $f(1,4)=0$ và $f'_y(1,4) \neq 0$ nên ta sẽ sử dụng định lý hàm ẩn để tìm `slope`

$$ s = \dfrac{-f'_x(1,4)}{f'_y(1,4)} = \dfrac{-16}{7} $$

```
    >> from solution import *
    >> slope_of_tangent_of_curve(1, 4)
        '-16/7'
```