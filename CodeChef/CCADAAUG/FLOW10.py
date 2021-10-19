t = int(input())
for i in range(t):
    s = input().lower()
    if s == "b":
        print("BattleShip")
    elif s == "c":
        print("Cruiser")
    elif s == "d":
        print("Destroyer")
    else:
        print("Frigate")