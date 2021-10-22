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

t = int(input())
for i in range(t):
    a, b, c = map(int,input().split())
    ans = a + b + c
    if(ans == 180):
        print("YES")
    else:
        print("NO")

s = input()
print(s.count("1"))

n = int(input())
a = int(input())
if(n % 500 <= a):
    print("Yes")
else:
    print("No")

a = input()
b = input()
ans = len(a) * len(b)
print(ans)

W, H = map(int,input().split())
if(3*W == 4*H):
    print("4:3")
else:
    print("16:9")

s1, e1 = map(int,input().split())
s2, e2 = map(int,input().split())
s3, e3 = map(int,input().split())
ans = (s1 * e1 + s2 * e2 + s3 * e3) // 10
print(ans)

l1, l2, l3 = map(int,input().split())
if(l1 == l2):
    print(l3)
elif(l2 == l3):
    print(l1)
else:
    print(l2)

def dstring(s):
    return s  + s
s = input()

print(dstring(s))
a = [0 , 1 , 3 , 1 , 2 , 1 , 2 , 1 , 1 , 2 , 1 , 2 , 1]
x, y = map(int,input().split())
print("Yes" if a[x] == a[y] else "No")

A = int(input())
print(7 - A)

N, K = map(int,input().split())
if(N % K == 0):
    print(0)
else:
    print(1)

A1, A2, A3 =  map(int,input().split())
ans = max(A1, A2, A3) - min(A1, A2, A3)
print(ans)

a,b,c,d = map(int,input().split())
if abs(c-a) <= d:
    print("Yes")
elif abs(b-a) <= d and abs(c-b) <= d:
    print("Yes")
else:
    print("No")

a,b,x = map(int,input().split())
o = x >= a and x <= a + b
if(o):
    print("YES")
else:
    print("NO")

N = int(input())
print(N//3)

def square(var):
    return var**2
def cube(var):
    return var**3
def root(var):
    return var**0.5
print(root(2))

def bubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
l=[3,2,1,8,4]
bubbleSort(l)
print(l)

t = int(input())
for i in range(t):
    case = int(input())
    if(case % 4 == 0):
        print("Even")
    elif(case % 2 == 0 and case % 4 != 0):
        print("Same")
    else:
        print("Odd")

K, X = map(int,input().split())
if(500*K >= X):
    print("Yes")
else:
    print("No")

ac, test = map(int,input().split())
if(ac == test):
    print("Yes")
else:
    print("No")

def main():
    a, b = input().split()
    if(a < b):
        print("<")
    elif(a == b):
        print("=")
    else:
        print(">")
if __name__ == "__main__":
    main()

N = int(input())
print(N * 800 - (N // 15) * 200)

x, a, b = map(int,input().split())
if(-a + b <= 0):
    print("delicious")
elif(-a + b <= x ):
    print("safe")
else:
    print("dangerous")
'''
a, b, c = map(int,input().split())
if(a == (b+c) or b==(c+a) or c==(b+a)):
    print("Yes")
else:
    print("No")