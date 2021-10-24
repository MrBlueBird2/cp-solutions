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
'''

a,b,c = input().split()
ans = a[0] + b[0] + c[0]
print(ans.upper())