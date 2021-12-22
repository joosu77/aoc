inp = open("inp12","r")
#inp = open("test12","r")
#inp = open("test12-","r")

arr = []
res=0

m = {}

for l in inp.readlines():
    arr.append(l.strip())
    a,b = l.strip().split("-")
    if a in m:
        m[a].append(b)
    else:
        m[a] = [b]
    if b in m:
        m[b].append(a)
    else:
        m[b] = [a]

paths = set()

def DFS(cur, done,n, used):
    global m
    global res
    done.append(cur)
    
    if cur == "end":
        res+=1
        if res%100==0:
            print([res,n])
        return
    for i in m[cur]:
    #    print(cur,done)
        if (i not in done or i.upper() == i or (i in done and not used)) and not i == "start":
            donet = done.copy()
            if done.count(i) >0 and i.lower() == i:
                DFS(i,donet,n+1, True)
            else:
                DFS(i,donet,n+1, used)
            
    done.pop(-1)
    
DFS("start",[],1,False)

print (m)
print(res)     
