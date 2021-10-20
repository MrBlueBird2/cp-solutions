# cook your dish here
t = int(input())
for i in range(t):
    s = input().upper()
    if s == "B":
        print("BattleShip")
    elif s == "C":
        print("Cruiser")
    elif s == "D":
        print("Destroyer")
    else:
        print("Frigate")