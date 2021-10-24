n = int(input())
s = input()
ans = ""
for i in range(n):
  if i == (n - 1) and s[i] == "x":
    ans = "No"
  else:
    ans = "Yes"
print(ans)