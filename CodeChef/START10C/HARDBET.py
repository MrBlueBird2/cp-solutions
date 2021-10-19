def LI(): return list(MPI())
def MPI(): return map(DI(), input().split())
def DS(): return input()
def DI(): return int(input())
def SSL(): return input.split()

t = DI()
for i in range(t):
    a, b, c = map(int, input().split())
    mn = min(a, b, c)
    if mn == a:
        print("Draw")
    elif mn == b:
        print("Bob")
    else:
        print("Alice")