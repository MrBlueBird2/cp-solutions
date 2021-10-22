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
'''

c = input()
ans = ""
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