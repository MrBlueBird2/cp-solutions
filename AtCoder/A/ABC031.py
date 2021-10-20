# 31
a, b = map(int, input().split())
x = (a + 1) * b
y = a * (b + 1)
print(max(x, y))