import sys,re
inp = open(sys.argv[1],"r")

sys.setrecursionlimit(int(1e8))

text = [l.strip() for l in inp.readlines()]

ll = text[0].split(",")

m = {}
mm = {}

res = 0
for l in ll:
    r = 0
    s = ""
    for c in l:
        if c == '=' or c == '-':
            break
        r = ((r+ord(c))*17)%256
        s+=c
    if c == '=':
        if r not in m:
            m[r] = []
            mm[r] = []
        if s in mm[r]:
            id = mm[r].index(s)
            m[r][id] = l
        else:
            m[r].append(l)
            mm[r].append(s)
    if c == '-':
        if r in m and s in mm[r]:
            id = mm[r].index(s)
            del mm[r][id]
            del m[r][id]

for k in m:
    for i in range(len(m[k])):
        num = int(m[k][i].split("=")[1])
        res+=(k+1)*(i+1)*num

print(f"gold res: {res}")