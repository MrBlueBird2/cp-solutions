# 24
a,b,c,k=map(int,input().split())
s,t=map(int,input().split())
d=0
if k<=s+t:
    d=c*(s+t)
print(s*a+t*b-d)