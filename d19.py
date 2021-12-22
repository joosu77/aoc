import sys
inp = open("inp19","r")
#inp = open("test19","r")

arr = []
for l in inp.readlines():
    ll = l.strip()
    if not ll:
        continue
    if ll[1] == '-':
        arr.append([])
        continue
    arr[-1].append(tuple(map(int,ll.split(","))))



def check(a,b):
    for f in [[1,1,1],[1,-1,1],[-1,-1,1],[-1,1,1],[1,1,-1],[1,-1,-1],[-1,-1,-1],[-1,1,-1]]:
        for r in [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,1,0],[2,0,1]]:
            scoploc = []
            for aa in range(len(a)):
                for bb in range(len(b)):
                    scoploc.append([a[aa][k]+b[bb][r[k]]*f[k] for k in range(3)])
            for i in range(len(scoploc)):
                scoploc[i] = tuple(scoploc[i])
            if len(set(scoploc))<len(scoploc)-10:
                print(scoploc)
                res = {}
                for s in scoploc:
                    if s not in res:
                        res[s] = 1
                    else:
                        res[s]+=1
                    if res[s] == 12:
                        center= [s[k] for k in range(3)]
                        return [[s[k] for k in range(3)],[tuple([center[k]-bb[r[k]]*f[k] for k in range(3)]) for bb in b]]
                        return [s[r[k]]*f[k] for k in range(3)]
                for k,v in res.items():
                    print(f"{k}: {v}")
    return 0

m = {}
ab = []
res=[i for i in arr[0]]
used = []
q = [0]
dd = []
while q:
    i = q.pop(0)
    for j in range(len(arr)):
        if i!=j and not j in used:
            v = check(arr[i],arr[j])
            if v:
                print("yarr")
                dd.append(v[0])
                if not i in m:
                    m[i] = {}
                m[i][j] = v[0]
                arr[j] = v[1]
                res+=v[1]
                used.append(i)
                q.append(j)
tot = []
for k,v in m.items():
    print(f"{k}: {v}")
                
larg=0
for a in dd:
    for b in dd:
        if sum([abs(a[k]-b[k]) for k in range(3)])>larg:
            larg=sum([abs(a[k]-b[k]) for k in range(3)])

print(sorted(res,key=lambda x: x[0])) 
print(len(set(res)))
print(larg)