import sys,re
import time
inp = open(sys.argv[1],"r")

sys.setrecursionlimit(int(1e8))

text = [l.strip() for l in inp.readlines()]


res=0
nr = 0
phase2 = 0
m={}
states = {}
m2={}
inps = {}
for l in text:
    m[l[1:].split(" -> ")[0]] = l[1:].split(" -> ")[1].split(", ")
    if l[0] == '%':
        states[l[1:].split(" -> ")[0]] = 0
    elif l[0] == "&":
        inps[l[1:].split(" -> ")[0]] = {}
    else:
        m[l.split(" -> ")[0]] = l.split(" -> ")[1].split(", ")

for k in m.keys():
    for kk in m[k]:
        if kk in inps:
            inps[kk][k]=0

res = [0,0]
for i in range(1000000000000):
    q = [("broadcaster",0,"broadcaster")]
    good=0
    while q:
        n,b,p = q[0]
        if n=='rx' and b==0:
            good+=1
            print(i)
        del q[0]
        if n not in m:
            continue
        if n in states:
            if b:
                continue
            states[n] = int(not states[n])
            for ch in m[n]:
                res[int(states[n])]+=1
                q.append((ch,states[n],n))
        elif n in inps:
            inps[n][p] = b
            if n=='bq' and sum(inps[n].values()):
                print(f"{i+1}: {inps[n].values()}")
            r=1
            if sum(inps[n].values())==len(inps[n].values()):
                r=0
            for ch in m[n]:
                res[r]+=1
                q.append((ch,r,n))
        else:
            for ch in m[n]:
                res[b]+=1
                q.append((ch,b,n))
    if good==1:
        print(i+1)
    #print(list(states.values()))
    time.sleep(0.0001)
    
print(f"silver res: {res}")