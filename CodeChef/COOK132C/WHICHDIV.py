def DI(): return int(input())
def DS(): return input()
def LI(): return list(MPI())
def MPI(): return map(int, DS().split(' '))
def SSL(): return DS().split()
def MPF(): return map(float, DS().split(' '))

n = DI()
for i in range(n):
    r = DI()
    if r >= 2000:
        print(1)
    elif r >= 1600 and r < 2000:
        print(2)
    else:
        print(3)