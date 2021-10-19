t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    l = [a, b, c]
    a0 = l.count(0)
    b1 = l.count(1)
    if a0 >= 1 and b1 >= 1:
        print(1)
    else:
        print(0)