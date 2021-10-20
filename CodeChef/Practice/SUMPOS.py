# cook your dish here
t = int(input())
for i in range(t):
    x, y, z = map(int,input().split())
    l = [x, y, z]
    list.sort(l)
    if(l[0] + l[1] == l[2]):
        print("YES")
    else:
        print("NO")