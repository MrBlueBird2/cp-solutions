# cook your dish here
t = int(input())
for i in range(t):
    s = input()
    print("wins" if s[::-1] == s else "loses")