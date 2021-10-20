# cook your dish here
t = int(input())
l = []
ans = 0
for _ in range(t):
    a = input().split()
    ans = a.count("1")
    if ans == 0:
        print("Beginner")
    elif ans == 1:
        print("Junior Developer")
    elif ans == 2:
        print("Middle Developer")
    elif ans == 3:
        print("Senior Developer")
    elif ans == 4:
        print("Hacker")
    else:
        print("Jeff Dean")