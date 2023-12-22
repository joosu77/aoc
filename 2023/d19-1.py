import sys,re
inp = open(sys.argv[1],"r")

sys.setrecursionlimit(int(1e8))

text = [l.strip() for l in inp.readlines()]


res=0
nr = 0
phase2 = 0
m={}
for l in text:
    if not l:
        phase2 = 1
        continue
    if not phase2:
        name, stuff = l.split("{")
        stuffl = stuff[:-1].split(",")
        m[name] = []
        for s in stuffl[:-1]:
            m[name].append((s[0],s[1]=='>',int(s.split(":")[0][2:]),s.split(":")[1]))
        m[name].append(stuffl[-1])
    else:
        vals = l[1:-1].split(",")
        valsl = {i[0]:int(i[2:]) for i in vals}
        ctr = "in"
        while ctr != "R" and ctr != "A":
            fjkdlgbn=0
            for u in m[ctr][:-1]:
                if u[1] and valsl[u[0]] > u[2] or not u[1] and valsl[u[0]] < u[2]:
                    ctr = u[3]
                    fjkdlgbn=1
                    break
            if fjkdlgbn == 0:
                ctr=m[ctr][-1]
        if ctr == "A":
            res+=sum(valsl.values())

print(f"silver res: {res}")