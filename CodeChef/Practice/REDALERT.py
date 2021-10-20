t = int(input())
for i in range(t):
    n, d, h = map(int, input().split())
    a = list(map(int, input().split()))
    x = 0
    flag = 0
    for i in range(len(a)):
        if a[i] > 0:
            x+=a[i]
        else:
            if x<d:
                x = 0
            else:
                x -= d
        if x > h:
            flag += 1
            break
    if flag == 1:
        print("YES")
    else:
        print("NO")