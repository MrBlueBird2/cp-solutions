def DI(): return int(input())
def DS(): return input()
def LI(): return list(MPI())
def SSI(): return DS().split()
def MPI(): return map(int, input().split())
def FI(): return float(input())

t = DI()
for i in range(t):
    a, b = MPI()
    if a > 0 and b > 0:
        print("Solution")
    elif b == 0:
        print("Solid")
    else:
        print("Liquid")