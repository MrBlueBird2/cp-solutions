# cook your dish here
t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    india = 0
    england = 0
    draw = 0
    for j in a:
        if j == 1:
            india += 1
        elif j == 2:
            england += 1
        else:
            draw += 1
    if india == england:
        print("DRAW")
    elif england > india:
        print("ENGLAND")
    else:
        print("INDIA")