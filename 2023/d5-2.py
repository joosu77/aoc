import sys,re
inp = open(sys.argv[1],"r")

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

last= []
for i in range(len(seeds)//2):
    last.append((seeds[2*i],seeds[2*i]+seeds[2*i+1]))

for mm in range(7):
    next = []
    seggs = list(last)
    for p in m[mm]:
        pbeg = p[0]
        pend = p[0]+p[2]
        seggs_con = []
        for seg in seggs:
            if pbeg<=seg[0] and seg[1]<=pend:
                next.append((seg[0]+p[1]-p[0], seg[1]+p[1]-p[0]))
            elif pbeg >= seg[1] or pend <= seg[0]:
                seggs_con.append(seg)
            elif pbeg >= seg[0] and pend <= seg[1]:
                seggs_con.append((seg[0],pbeg))
                next.append((p[1],p[1]+p[2]))
                seggs_con.append((pend,seg[1]))
            elif pbeg <= seg[0]:
                next.append((seg[0]+p[1]-p[0], p[1]+p[2]))
                seggs_con.append((pend, seg[1]))
            else:
                seggs_con.append((seg[0],pbeg))
                next.append((p[1], seg[1]+p[1]-p[0]))
        seggs = seggs_con
    for seg in seggs:
        next.append(seg)
    last = set(next)

print(sorted(list(last))[0][0])
