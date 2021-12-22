f = open("inp22","r")

p1 = []
p2 = []
bp1 = True
for l in f.readlines():
    if l.strip() == "Player 2:":
        bp1 = False
    elif l.strip().isalnum():
        if bp1:
            p1.append(int(l.strip()))
        else:
            p2.append(int(l.strip()))

def combat(d1, d2):
    states = []
    while d1 and d2 and [d1,d2] not in states:
        #print(d1)
        print(d2)
        print()
        states.append([d1.copy(),d2.copy()])
        if d1[0]<len(d1) and d2[0]<len(d2):
            winner = combat(d1[1:d1[0]+1], d2[1:d2[0]+1])
        else:
            winner = 1 if d2[0]> d1[0] else 0
        if not winner:
            d1.append(d1.pop(0))
            d1.append(d2.pop(0))
        else:
            d2.append(d2.pop(0))
            d2.append(d1.pop(0))
    print("===========================")
    print(d1)
    print(d2)
    print(states)
    if d1:
        return 0
    else:
        return 1

winner = combat(p1, p2)
print(winner)

res=0
for i in range(len([p1,p2][winner])):
    res += (i+1)*([p1,p2][winner])[-i-1]
print(res)