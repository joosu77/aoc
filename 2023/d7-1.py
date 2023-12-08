import sys,re
inp = open(sys.argv[1],"r")

sss = []
d1 = True

for l in inp.readlines():
    cardss, bid = l.split()
    cards = list(cardss)
    m = {}
    mm = {}
    m["J"] = 0
    for c in cards:
        if c not in m:
            m[c] = 0
        if not d1:
            m[c]+=1
        if c != "J" or d1:
            if c not in mm:
                mm[c] = 0
            mm[c]+=1
    
    if len(mm):
        mv = max(mm.values())
    else:
        mv = 0
    
    if mv+m["J"] == 5:
        type=0
    elif mv+m["J"] == 4:
        type=1
    elif len(mm) == 2:
        type=2
    elif mv+m["J"] == 3:
        type=3
    elif len(mm) == 3:
        type=4
    elif len(mm) == 4:
        type = 5
    else:
        type=6
    sss.append((-type,[int(i) if i.isnumeric() else {"T":10,"J":11 if d1 else 1,"Q":12,"K":13,"A":14}[i] for i in cardss],bid))
        
sss.sort()
res = 0
for c in range(len(sss)):
    res += (c+1)*int(sss[c][2])
print(res)