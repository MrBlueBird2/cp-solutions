t = int(input())
s = input().split()
lst1 = []
lst2 = []
for ele in s:
    ele = int(ele)
    if ele%2 == 0:
        lst1.append(ele)
    else:
        lst2.append(ele)
if len(lst1) > len(lst2):
    print("READY FOR BATTLE")
else:
    print("NOT READY")