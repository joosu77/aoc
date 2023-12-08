import sys,re
inp = open(sys.argv[1],"r")

sss = []
d1 = True

text = inp.readlines()
cmds = text[0].strip()

g1 = {}
g2 = {}
cd = 0
starts = []
for l in text[2:]:
    src = l.split()[0]
    if src[-1] == 'A':
        starts.append(src)
    dst1 = l.split("(")[1].split(",")[0]
    dst2 = l.split()[-1][:-1]
    g1[src] = dst1
    g2[src] = dst2

print(cd)

sstarts = [i for i in starts]

ctr = "AAA"
c = 0
cycles = [-1 for i in starts]
zs = [[] for i in starts]

sets = [{i:0} for i in starts]

zz = [[] for i in starts]
for i in range(100000):
    cmd = cmds[c%len(cmds)]
    if cmd == "L":
        for i in range(len(starts)):
            starts[i] = g1[starts[i]]
    else:
        for i in range(len(starts)):
            starts[i] = g2[starts[i]]
    c+=1
    nope = 0

    for s in range(len(starts)):
        if starts[s] in sets[s] and cycles[s] == -1 and c%len(cmds)==0:
            cycles[s] = c
        if starts[s][-1] == 'Z' and cycles[s] == -1:
            zs[s].append(c)
        if cycles[s] == -1:
            sets[s][starts[s]] = c
        if starts[s][-1] == 'Z':
            zz[s].append(c)

    for s in starts:
        if s[-1] != 'Z':
            nope = 1
            break
    if not nope:
        print(c)
        break
print(cycles)
print(zs)
print(zz)