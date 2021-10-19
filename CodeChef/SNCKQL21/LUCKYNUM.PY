t = int(input())
for i in range(t):
    a, b, c = input().split()
    ans = a + b + c
    print("YES" if "7" in ans else "NO")