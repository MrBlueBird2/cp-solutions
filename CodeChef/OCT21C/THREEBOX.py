def DI(): return int(input())
def DS(): return input()
def LI(): return list(MPI())
def SSI(): return DS().split()
def MPI(): return map(int, input().split())
def FI(): return float(input())

t = DI()
for i in range(t):
    a, b, c, d = MPI()
    if a + b + c <= d:
        print(1)
    elif a + b <= d:
        print(2)
    else:
        print(3)