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
        break
    name, stuff = l.split("{")
    stuffl = stuff[:-1].split(",")
    m[name] = []
    for s in stuffl[:-1]:
        m[name].append((s[0],s[1]=='>',int(s.split(":")[0][2:]),s.split(":")[1]))
    m[name].append(stuffl[-1])
    
q = [("in",{"x":(1,4000),"m":(1,4000),"a":(1,4000),"s":(1,4000)})]
while q:
    node = q[0]
    del q[0]
    vs = node[1]
    if node[0] == "A":
        p=1
        for v in vs.values():
            p*=v[1]-v[0]+1
        res+=p
        continue
    if node[0] == 'R':
        continue
    fin=0
    for u in m[node[0]][:-1]:
        if vs[u[0]][0] >= u[2] and u[1] or vs[u[0]][1] <= u[2] and not u[1]:
            continue
        if vs[u[0]][1] < u[2] and u[1] or vs[u[0]][0] > u[2] and not u[1]:
            q.append((u[3],vs))
            fin = 1
            break
        if u[1]:
            c = vs.copy()
            vs[u[0]] = (vs[u[0]][0],u[2])
            c[u[0]] = (u[2]+1, c[u[0]][1])
            q.append((u[3],c))
        else:
            c = vs.copy()
            vs[u[0]] = (u[2],vs[u[0]][1])
            c[u[0]] = (c[u[0]][0], u[2]-1)
            q.append((u[3],c))
    if not fin:
        q.append((m[node[0]][-1],vs))
        
            
print(f"gold res: {res}")