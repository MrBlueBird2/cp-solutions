def DI(): return int(input())
def DS(): return input()
def LI(): return list(MPI())
def MPI(): return map(int, DS().split(' '))
def SSL(): return DS().split()
def MPF(): return map(float, DS().split(' '))

a = DS()
b = "Hello,World!"
if a == b and len(a) == len(b):
    print("AC")
else:
    print("WA")