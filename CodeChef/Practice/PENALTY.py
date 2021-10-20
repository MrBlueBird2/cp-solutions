t = int(input())
for lines in range(t):
    team = list(map(int, input().split()))
    a = 0
    b = 0
    x = 0
    for i in range(len(team)):
        x += 1
        if x % 2 != 0:
            a += team[i]
        else:
            b += team[i]
    if a > b:
        print(1)
    elif a == b:
        print(0)
    else:
        print(2)