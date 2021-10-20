# cook your dish here
'''
a = int(input())
if(a % 2 == 0):
    print("Mahmoud")
else:
    print("Ehab")

n = int(input())
i = int(n // 111)
if n % 111 != 0:
    i += 1
print(i * 111)

N, K = map(int,input().split())
n = K * 2 - 1
if(n <= N):
    print("YES")
else:
    print("NO")

c = input()
ans = str()
if(c == "a"):
    ans = "vowel"
elif(c == "e"):
    ans = "vowel"
elif(c == "i"):
    ans = "vowel"
elif(c == "o"):
    ans = "vowel"
elif(c == "u"):
    ans = "vowel"
else:
    ans = "consonant"
print(ans)

a, b = map(int,input().split())
ans = ""
if(a % 3 == 0):
    ans = "Possible"
elif(b % 3 == 0):
    ans = "Possible"
elif((a + b) % 3 == 0):
    ans = "Possible"
else:
    ans = "Impossible"
print(ans)

a, b = map(int,input().split())
ans = (a + b) / 2 + 0.5
print(int(ans))

A, B, C = map(int,input().split())
ans = max(10 * A + B + C , A + 10 * B + C , A + B + 10 * C )
print(ans)

A, D = map(int,input().split())
ans = min((A + 1) * D, A * (D + 1))
print(ans)

N = int(input())
ans = N + 1
if(ans > 12):
    print(ans - 12)
else:
    print(ans)

N = int(input())
print(N - 1)

N = input()
ans=list(N)
while(ans and N[-1]=="0"):
    N.pop()
if N==N[::-1]:
    print("Yes")
else:
    print("No")

a,b,c = input().split()
ans = a[0] + b[0] + c[0]
print(ans.upper())

name = input()
print("YES" if name[::-1] == name else "NO")

A, B = map(int,input().split())
ans = max(A, B)
print(ans)

s = input()
ans = s[0] + str(len(s) - 2) + s[-1]
print(ans)

def isSame(var):
    if(var[0] == var[1] and var[1] == var[2] and var[2] == var[3]):
        return "SAME"
    else:
        return "DIFFERENT"
n = input()
print(isSame(n))

m = int(input())
print(48 - m)

N  = int(input())
print((N - 2) * 180)

s = input()
cnt = 0
for i in range(len(s)):
    if(s[i] == 'x'):
        cnt += 1
print("YES" if cnt <= 7 else "NO")

r = int(input())
result = (3 * r)**2
print(result)

s = input()
print(s.count("1"))

a,b = map(int,input().split())
ab = (a - 1) * (b - 1)
print(ab)

s = input()
if ( s [0]== s [1] and s [1]== s [2]):
    print("Yes")
elif ( s [1]== s [2] and s [2]== s [3]):
    print("Yes")
else:
    print("No")

x, a, b = map(int,input().split())
da = abs(a - x)
db = abs(b - x)
if(da < db):
    print("A")
else:
    print("B")

a = int(input())
b = int(input())
c = input()
if(c == "/"):
    print(a // b)
elif(c == "+"):
    print(a + b)
elif(c == "-"):
    print(a - b)
else:
    print(a * b)

c = input()
if(c == "A"):
    print("Vowel")
elif(c == "E"):
    print("Vowel")
elif(c == "I"):
    print("Vowel")
elif(c == "O"):
    print("Vowel")
elif(c == "U"):
    print("Vowel")
else:
    print("Consonant")
'''

t = int(input())
for i in range(t):
    a, b, c = map(int,input().split())
    ans = a + b + c
    if(ans == 180):
        print("YES")
    else:
        print("NO")