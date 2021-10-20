t = int(input())
for _ in range(t):
    l = [2010, 2015, 2016, 2017, 2019]
    n = int(input())
    if n in l:
        ans = "HOSTED"
    else:
        ans = "NOT HOSTED"
    print(ans)