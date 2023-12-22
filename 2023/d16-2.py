import sys,re
inp = open(sys.argv[1],"r")

sys.setrecursionlimit(int(1e8))

text = [l.strip() for l in inp.readlines()]

res = 0
lins = [(-1,i,2) for i in range(len(text[0]))]
lins += [(len(text),i,0) for i in range(len(text[0]))]
lins += [(i,-1,1) for i in range(len(text))]
lins += [(i,len(text[0]),3) for i in range(len(text))]
for ii in lins:
    done = set()
    sqs = set()
    q = [ii]
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]

    def add(a,b,c):
        if a < 0 or a >= len(text) or b < 0 or b >= len(text[0]) or ((a,b,c) in done):
            return
        done.add((a,b,c))
        sqs.add((a,b))
        q.append((a,b,c))

    while q:
        node = q.pop()
        next = (node[0]+dirs[node[2]][0],node[1]+dirs[node[2]][1])
        try:
            nc = text[next[0]][next[1]]
        except:
            continue
        if nc == '.':
            add(next[0],next[1],node[2])
        elif nc == '-':
            add(next[0],next[1],1)
            add(next[0],next[1],3)
        elif nc == '|':
            add(next[0],next[1],2)
            add(next[0],next[1],0)
        elif nc == '/':
            ndir = {0:1,1:0,3:2,2:3}[node[2]]
            add(next[0],next[1],ndir)
        elif nc == '\\':
            ndir = {0:3,3:0,1:2,2:1}[node[2]]
            add(next[0],next[1],ndir)
    if res<len(sqs):
        res=len(sqs)
'''           
for i in range(len(text)):
    for j in range(len(text[0])):
        if (i,j) in sqs:
            print("#",end="")
        else:
            print(".",end="")
    print() 
'''
print(f"silver res: {res}")