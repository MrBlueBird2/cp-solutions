# cook your dish here
a,b,c=map(int,input().split())
ans=""
if(a == b or a == c or b==c):
    ans="YES"
else:
    ans="NO"
print(ans)
