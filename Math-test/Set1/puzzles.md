### Câu 1. Cho một hình lập phương `4x4x4`, được tạo thành từ 64 hình lập phương `1x1x1`. Giả sử ta tô màu toàn bộ hình lập phương lớn `4x4x4`, hỏi có bao nhiêu hình lập phương có ít nhất một mặt được tô màu?

**Giải**

- Dễ thấy rằng chỉ có lớp ngoài cùng của hình lập phương là được tô nên chỉ có khối `2x2x2` ở trong cùng là không được tô đến.
- Trong khối `2x2x2` có 8 hình lập phương nhỏ `1x1x1`, như vậy ta có $64 - 8 = 56$ hình lập phương không được tô màu.


### Câu 2. Anna có 2023 đồng xu, Bob có 2011. Tính xác suất để số mặt sấp của Anna ít nhất gấp đôi của Bob.

**Giải**

Đầu tiên, tôi phân loại nhóm câu này vào chủ đề câu đố bởi đây là một mẹo nhỏ, không cần quá nhiều kiến thức xác suất.

Đặt 
- $\alpha = P(A > 2B)$ tức là xác suất mà số mặt `H` của Anna nhiều hơn gấp đôi của Bob
- $\beta = P(A < 2B)$ tức là xác suất mà số mặt `H` của Anna ít hơn gấp đôi của Bob, và
- $\gamma = P(A = 2B)$ tức là xác suất mà số mặt `H` của Anna bằng đúng 2 lần của Bob.

Khi đó $\alpha, \beta, \gamma$ tạo thành một hệ các biến cố đầy đủ và

$$ \alpha + \beta + \gamma = 1 $$

Lưu ý rằng khi Anna có 2022 đồng xu thì ta có $\alpha = \beta$ do đối xứng, như vậy

$$ 2\alpha + \gamma = 1 $$

hay $\alpha + \frac{1}{2} \gamma = 0.5$

Cuối cùng, vì Anna có 2023 đồng, khi đó xác suất để số mặt `H` của Anna ít nhất gấp đôi của Bob bằng
$$ P (\text{Đồng 2023'th là `T` hay `H` không quan trọng nếu Anna > 2 Bob với 2022 đồng trước}) + P(\text{Đồng 2023'th là `H` nếu Anna = 2 Bob với 2022 đồng trước}) $$

Mà

$ P (\text{Đồng 2023'th là `T` hay `H` không quan trọng nếu Anna > 2 Bob với 2022 đồng trước}) = \alpha $

và 

$ P(\text{Đồng 2023'th là `H` nếu Anna = 2 Bob với 2022 đồng trước}) = \dfrac{1}{2} \gamma $

Do đó, câu trả lời cuối cùng là $\dfrac{1}{2}$

### Câu 3. `In a town N, every person is either a truth-teller, who always tells the truth, or a liar, who always lies. Every person in town N took part in a survey. "Is winter your favorite season?" was answered "yes" by 40% of respondents. A similar question about spring had 30% of affirmative answers, about summer had 50%, and about autumn had 0%. What percent of the town's population actually has winter as a favorite season?`

**Giải**

- Đặt $x$ là số phần trăm số người sẽ nói sự thật tại thị trấn N, hiển nhiên mấy thằng nói dối sẽ là $1 - x$.

- Với tổng số phần trăm trong các khảo sát ở 4 mùa, ta được 
$$ 1 - x = (40 + 30 + 50 + 0) - 100 = 20 $$
tức là $x=80\%$

- Như vậy, số người thật sự thích mùa đông sẽ là
$$ 40 * 0.8 = 32\% $$
vì trong số $40\%$ những người được khảo sát thích mùa đông có đến $20\%$ là mấy thằng xạo chó.

### Câu 4. Vào lúc `3:15pm`, kim giờ và kim phút của đồng hồ cách nhau bao nhiêu độ?

**Giải**

- Có $12$ giờ trên đồng hồ nên giữa 2 giờ liên tiếp sẽ cách nhau $30^0$
- Vào `3:15` thì nó nằm giữa $3$ và $4$ nên góc này là một mảnh nhỏ của $30^0$
- Tiếp theo, $15$ phút bằng một phần bốn của toàn bộ góc tạo bởi $3$ và $4$ giờ nên $3:15$ xấp xỉ $\frac{30^0}{4} = 7.5^0$

### Câu 6. We call a place on Earth "nice" if you ga 1 mile `North`, 1 mile `West`, 1 mile `South` and 1 mile `East` then you end up at exactly the same place you started, but you did not visit any location more than twice, What is the minimum number of circumferences covering all nice places on Earth