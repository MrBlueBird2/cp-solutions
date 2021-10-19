# cook your dish here
t = int(input())
for i in range(t):
    a, b, c = map(int,input().split())
    s = (a + 1)%c
    if b%c == 0 or b%c == s:
        print("YES")
    else:
        print("NO")