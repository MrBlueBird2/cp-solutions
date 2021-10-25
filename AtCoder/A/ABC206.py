n = int(input())
ans = (1.08*n)
if int(ans) < 206:
    print("Yay!")
elif int(ans) == 206:
    print("so-so")
else:
    print(":(")