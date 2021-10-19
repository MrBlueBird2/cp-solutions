t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    l = [a, b, c]
    l.sort()
    print(l[1] + l[2])