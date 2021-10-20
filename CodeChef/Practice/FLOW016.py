# cook your dish here
from math import gcd
t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    def lcm(a,b):
        return (a // gcd(a,b))* b
    print(gcd(a, b), lcm(a, b))