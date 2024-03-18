### Câu 1-4. Tương ứng với các function `algorithm_k` với k từ 1-4 trong `solution.py`
Đây là những câu cơ bản nên tôi sẽ không giải thích
```
    >> from solution import *
    >> algorithm_1()
```


### Câu 5. Kiểm tra kết quả của thuật toán bên dưới và giải thích
Với `x @ y = f(x, y)` xác định bởi
$$ f(x,y) = \dfrac{x*y}{x + y} $$
nên với mọi $k \in \mathbb{N}$ thì
$$ f(2^k, 2^{k-1}) = \dfrac{2^k * 2^{k-1}}{2^k + 2^{k-1}} = \dfrac{2^k * 2^{k-1}}{3*2^{k-1}} = \dfrac{2^k}{2^2 - 1}$$
do đó, 
$$ f\left( f(2^k, 2^{k-1}), 2^{k-2} \right) = \dfrac{2}{2^2-1} f\left(2^{k-1}, 2^{k-2} \right) = \dfrac{2^k}{2^3 - 1}$$
Bằng quy nạp, ta được kết quả cuối cùng là $\dfrac{2^{10}}{2^{10} - 1}$