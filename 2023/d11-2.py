import sys,re
inp = open(sys.argv[1],"r")

text = inp.readlines()

g = set()

cols = set()

missing = 0
for l in range(len(text)):
    if text[l].count("#") == 0:
        missing+=1000000-1
        continue
    for c in range(len(text[l])):
        if text[l][c] == '#':
            g.add((l+missing,c))
            cols.add(c)

coladd = []
missing = 0

for col in range(len(text[0])):
    if not col in cols:
        missing +=1000000-1
    coladd.append(missing)

res = {}

for p1 in g:
    for p2 in g:
        res[tuple(sorted((p1,p2)))] = abs(p1[0]-p2[0])+abs(p1[1]+coladd[p1[1]]-p2[1]-coladd[p2[1]])

print(g)
print(f"silver res: {sum(res.values())}")