import sys,re
inp = open(sys.argv[1],"r")


nn = [12,13,14]

lins = [i.strip() for i in inp.readlines()]+[""]

seeds = list(map(int,lins[0].split(":")[1].split()))

ctr = 3
m = []
for mm in range(7):
    m.append([])
    while lins[ctr]:
        a,b,c = list(map(int,lins[ctr].split()))
        ctr+=1
        m[-1].append((b,a,c))
    ctr+=2

last= set(seeds)
for mm in range(7):
    print(last)
    next = set()
    for s in last:
        found = 0
        for p in m[mm]:
            if p[0]<=s<p[0]+p[2]:
                if s == 82:
                    print(p[1]+s-p[0])
                next.add(p[1]+s-p[0])
                found = 1
        if not found:
            next.add(s)
    last = next

print(sorted(list(last))[0])
