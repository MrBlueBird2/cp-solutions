def LI(): return list(MPI())
def MPI(): return map(int, input().split())
def DS(): return input()
def DI(): return int(input())
def SSL(): return input.split()

x1 = float(input())
x1 = str(x1)
idx = x1.index(".")
x = x1[:idx]
y = x1[idx+1:]
x = int(x)
y = int(y)
if 0 <= y and y <= 2:
    print(str(x) + "-")
elif 3 <= y and y <= 6:
    print(x)
else:
    print(str(x) + "+")