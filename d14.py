inp = open("inp14","r")
#inp = open("test14","r")

dots = []
res=0
arr = []
m = {}

first = True
lst = ""

for l in inp.readlines():
    ll = l.strip()
    if first:
        first = False
        lst = ll
    else:
        if ll:
            m[ll.split(" -> ")[0]] = ll.split(" -> ")[1]
    
print(m)

lstm = {}

for i in range(1,len(lst)):
    st = "".join(lst[i-1:i+1])
    if st in lstm:
        lstm[st] += 1
    else:
        lstm[st] = 1

for j in range(40):
    print(lstm)
    newm = {}
    for k,v in lstm.items():
        if k in m:
            tba1 = k[0]+m[k]
            if tba1 in newm:
                newm[tba1] +=v
            else:
                newm[tba1] = v
            tba2 = m[k]+k[1]
            if tba2 in newm:
                newm[tba2] +=v
            else:
                newm[tba2] = v
        else:
            if k in newm:
                newm[k] += v
            else:
                newm[k] = v
    lstm = newm.copy()
                
            
    
elems = {}
for k,v in lstm.items():
    for c in k:
        if c in elems:
            elems[c] += v
        else:
            elems[c] = v


ax = 0
axn = ""
mmin = -1

for k,v in elems.items():
    if v > ax:
        ax = v
    if v < mmin or mmin == -1:
        mmin = v
print((ax+1)//2-(mmin+1)//2)
print(elems)