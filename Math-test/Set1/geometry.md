### Câu 1. Imagine four bugs situated at each vertex of a unit square. Suddenly, each bug begins to chase its counterclockwise neighbour. If the bugs travel at 1 unit per minute, how long will it take for the four bugs to crash into one another?

**Solve**

- Do hình vuông đối xứng nên tại mỗi đỉnh của hình vuông nếu mỗi con bọ bắt đầu đuổi theo con bên cạnh theo chiều ngược chiều kim đồng hồ, khi đó các con bọ di chuyển về phía trung tâm theo đường xoắn ốc và hình vuông sẽ thu hẹp lại và tâm của hình vuông vẫn không đổi.

![image](https://github.com/NhanDoV/WorldQuant-math-quiz/assets/60571509/99de0cb3-bdcc-4dbd-8102-870bcaf8f16e)

- Các đường chéo của hình vuông luôn gặp nhau tại tâm của hình vuông đơn vị (cạnh bằng 1) và vận tốc hướng tâm của con bọ là hình chiếu của vectơ vận tốc của con bọ dọc theo đường chéo đi qua vị trí của con bọ. Ta có
>- Vectơ vận tốc của một con bọ luôn hướng đến con bọ tiếp theo và do đó nằm dọc theo một cạnh của hình vuông. Góc giữa cạnh đó và đường chéo là 45°
>- Do đó vận tốc hướng tâm là $1/\sqrt{2}$ mỗi phút


### Câu 2. Suppose a stick of length 1 is broken in five places, each chosen uniformly at random along the length of the stick. Find the probability that the six resulting pieces can be arranged as the edges of a tetrahedron (triangular based pyramid).

**Solve**

Đặt các đoạn thẳng của hình tứ diện là $x,y,z, d_1, d_2, d_3$, xem minh họa bên dưới

![image](https://github.com/NhanDoV/WorldQuant-math-quiz/assets/60571509/cb59230e-4054-4b66-b61a-79a0bad6295f)

Từ hệ này, ta được tập các giá trị mà nó thỏa một tứ diện sẽ là thể tích của hình được giới hạn bởi

$$ \left\lbrace x,y,z \in \left( 0, \dfrac{1}{3} \right), x+y+z \geq \dfrac{1}{3} \right\rbrace $$

trong khi đó, không gian mẫu của chúng ta là thể tích của hình giới hạn bởi

$$ \left\lbrace x,y,z \in \left( 0, 1 \right), x+y+z \leq 1 \right\rbrace $$

### Câu 3. Start with a cube (let us denote it by A). Put a point at the center of its faces and create a polyhedron (denoted by B). Put a point at the center of the faces of this polyhedron and create a second polyhedron (denoted by C) with these new points as vertices. What is the volume of A if C has a volume of 1?

**Solve**
- Khối đa diện $B$ được tạo thành bởi cách nối các center tại các mặt (6 mặt) của chúng lại với nhau, như vậy ta được một khối bát diện (octahedron) với 8 mặt, 6 đỉnh như sau:
 
![image](https://github.com/NhanDoV/WorldQuant-math-quiz/assets/60571509/b54bd44e-043f-4665-b52b-694b5fb93820)

- Tiếp tục, giả sử cạnh của hình lập phương là $2a$ thì chiều cao của nửa trên khối bát diện này (khối kim tự tháp) sẽ là $a$ với độ dài cạnh đáy của pyramid này sẽ là $a\sqrt{2}$

![image](https://github.com/NhanDoV/WorldQuant-math-quiz/assets/60571509/a3458d73-32b7-42dc-b4e1-66004db30d66)

- Thể tích của một pyramid sẽ là

$$\dfrac{1}{3}S*h = \dfrac{1}{3} (a \sqrt{2})^2 a = \dfrac{2}{3}a^3 $$

và thể tích của $B$ sẽ bằng 2 lần thể tích khối pyramid này, và khi đó

$$ \dfrac{V_B}{V_A} = \dfrac{\frac{4}{3}a^3}{(2a)^3} = \dfrac{1}{6} $$  

- Tương tự, ta xét tỷ lệ thể tích của $B$ và $C$, với $C$, với $C$ lúc này lại trở về một hình lập phương (bởi cách nối các trọng tâm của 8 mặt trong khối ban đầu, với cạnh $c = \dfrac{1}{3} * (2a) = \dfrac{2 a}{3}$ (trong đó ta đang giả sử $A$ có cạnh $2a$ và kết hợp với giả thiết trọng tâm của các mặt trên khối bát diện này là trọng tâm của 8 tam giác, khi đó đoạn nối các cạnh của hình lập phương $C$ sẽ song song và bằng $\dfrac{1}{3}$ độ dài các đường chéo trên mặt đáy của khối pyrmaid)

![image](https://github.com/NhanDoV/WorldQuant-math-quiz/assets/60571509/a4e11c9f-f9d6-422a-b9c3-5e6c19e4fc7c)

Như vậy, thể tích của $C$ bằng $1$ tức là

$$ \left( \frac{2}{3}a \right)^3 = 1 \Leftrightarrow (2a)^3 = 27 $$

### Câu 4. Triangle ABC has sides of length 45, 60 and 75. Please point D randomly and informally in side the triangle. What is the expected value of the sum of perpendicular distance from point D to triangle's three sides?

**Solve**

- Đặt các khoảng cách đó là $x, y$ và $z$, trong đó $z$ là khoảng cách đến cạnh dài nhất $AB$
- Ta thấy rằng $ABC$ là một tam giác vuông (tại $C$) và $D$ được chọn ngẫu nhiên bên trong tam giác. 

![image](https://github.com/NhanDoV/WorldQuant-math-quiz/assets/60571509/6dc90f0f-bedb-4727-87df-d169d491b105)

- Vì $ABC$ vuông tại $C$ cho nên

$$ CH = \dfrac{CA * CB}{AB} = \dfrac{45*60}{75} = 36 $$

- Ta cần xác định $\mathbb{E}(x+y+z)$ với $z$ là khoảng cách đến $AB$ thì nó có thể được viết theo $x$ và $y$ bằng cách coi diện tích của các tam giác thành phần bằng tổng diện tích.

- Ta có $3x + 4y + 5z = 180$ với $x \in (0, 60), y \in (0, 45)$ và $z \in (0, 36)$ do đó

$$ \mathbb{E}(x+y+z) = 47 $$