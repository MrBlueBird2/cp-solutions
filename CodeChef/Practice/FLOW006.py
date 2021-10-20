# cook your dish here
t = int(input())
for _ in range(t):
    s = input()
    ans = 0
    for ele in s:
        ans += int(ele)
    print(ans)