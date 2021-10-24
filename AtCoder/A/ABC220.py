def DI(): return int(input())
def DS(): return input()
def LI(): return list(MPI())
def SSI(): return DS().split()
def MPI(): return map(int, input().split())
def FI(): return float(input())

a, b, c = MPI()
y = b // c * c
if a <= y:
    print(y)
else:
    print(-1)