x,y=map(int,input().split())
if (x+3>y and x<y) or (y+3>x and y<x):
    print("Yes")
else:
    print("No")