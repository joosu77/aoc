import sys,re
inp = open(sys.argv[1],"r")

sys.setrecursionlimit(int(1e8))

text = [l.strip() for l in inp.readlines()]

res=0


done = {}
sqs = set()
paths = {(0,0,0):[]}

res = 1e9
#x,y,num straight, sum, last dir
q = [(0,0,-1,0,-1,[])]
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

def add(a,b,c):
    if a < 0 or a >= len(text) or b < 0 or b >= len(text[0]) or ((a,b,c) in done):
        return
    done.add((a,b,c))
    sqs.add((a,b))
    q.append((a,b,c))

while q:
    #node = q.pop()
    node = q[0]
    del q[0]
    #print(node)
    
    for d in dirs:
        di = dirs.index(d)
        next = (node[0]+d[0],node[1]+d[1],node[2]+1 if node[4] == di else 0,di)
        if next[0] <0 or next[0] >= len(text[0]) or next[1]<0 or next[1]>=len(text) or next[2] >2 or (di==(node[4]+2)%4 and node[4]!=-1):
            continue
        val = int(text[next[0]][next[1]])
        if tuple(next[:2]) == (len(text)-1,len(text[0])-1):
            res = min(res,node[3]+val)
            if res == node[3]+val:
                path = node[-1]
        if next not in done or done[next]>node[3]+val:
            done[next] = node[3]+val
            q.append((next[0],next[1],next[2],node[3]+val,di,node[-1]+[tuple(next[:2])]))
            if node[:3] not in paths:
                paths[node[:3]] = []
            paths[next[:3]] = paths[node[:3]]+[tuple(next[:2])]
            
           
for ii in range(3):
    r=0
    for i in range(len(text)):
        for j in range(len(text[0])):
            #if (i,j) in paths[(len(text)-1,len(text[0])-1,ii)]:
            if (i,j) in path:
                print(text[i][j],end="")
                r+=int(text[i][j])
            else:
                print(".",end="")
        print() 

    print(r)
print(len(paths[(len(text)-1,len(text[0])-1,0)]))
print(f"silver res: {res}")