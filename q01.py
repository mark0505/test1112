from modu import triangle_zhonxin

# 輸入三點座標
input_a = input("請輸入頂點 a 的坐標 (x, y): ")
input_b = input("請輸入頂點 b 的坐標 (x, y): ")
input_c = input("請輸入頂點 c 的坐標 (x, y): ")

# 將輸入字串轉為 tuple
a = tuple(map(int, input_a.split(',')))
b = tuple(map(int, input_b.split(',')))
c = tuple(map(int, input_c.split(',')))

# 求重心
G = triangle_zhonxin(a, b, c)

# 顯示結果
print(f"此三角形的重心為:{G}")