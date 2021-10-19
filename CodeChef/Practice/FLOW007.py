t=int(input())
while t>0:
    n=int(input())
    c=0
    while n>0:
        r=n%10
        c=c*10+r
        n=n//10
    print(c)
    t=t-1
        