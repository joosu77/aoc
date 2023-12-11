import sys,re
inp = open(sys.argv[1],"r")

text = inp.readlines()

g={}

for l in range(len(text)):
    for i in range(len(text[l])):
        node = text[l][i]
        if node == 'S':
            start = (i,l)
            g[(i,l)] = [(i-1,l),(i+1,l),(i,l-1),(i,l+1)]
        elif node == '|':
            g[(i,l)] = [(i,l+1),(i,l-1)]
        elif node == '-':
            g[(i,l)] = [(i-1,l),(i+1,l)]
        elif node == 'L':
            g[(i,l)] = [(i+1,l),(i,l-1)]
        elif node == 'J':
            g[(i,l)] = [(i,l-1),(i-1,l)]
        elif node == '7':
            g[(i,l)] = [(i-1,l),(i,l+1)]
        elif node == 'F':
            g[(i,l)] = [(i+1,l),(i,l+1)]

ng = {}

for n in g:
    for node in g[n]:
        if node in g and n in g[node]:
            if n not in  ng:
                ng[n] = []
            if node not in ng:
                ng[node] = []
            ng[n].append(node)
            ng[node].append(n)

ctr = start
dists = {start:0}
seen = set()
q = [ctr]
lareas = []
rareas = []
dif = lambda a,b: (a[0]-b[0],a[1]-b[1])
add = lambda a,b: (a[0]+b[0],a[1]+b[1])
u = (0,-1)
d = (0,1)
l = (-1,0)
r = (1,0)
loop = set()
while q:
    node = q[-1]
    del q[-1]
    loop.add(node)
    for n in ng[node]:
        if not n in seen:
            dists[n] = dists[node]+1
            seen.add(n)
            q.append(n)
            delta = dif(n,node)
            if delta == u:
                lareas.append(add(node,l))
                lareas.append(add(n,l))
                rareas.append(add(node,r))
                rareas.append(add(n,r))
            elif delta == d:
                lareas.append(add(node,r))
                lareas.append(add(n,r))
                rareas.append(add(node,l))
                rareas.append(add(n,l))
            elif delta == l:
                lareas.append(add(node,d))
                lareas.append(add(n,d))
                rareas.append(add(node,u))
                rareas.append(add(n,u))
            elif delta == u:
                lareas.append(add(node,u))
                lareas.append(add(n,u))
                rareas.append(add(node,d))
                rareas.append(add(n,d))

def draw(s):
    for l in range(len(text)):
        for ll in range(len(text[0])):
            if (ll,l) in s:
                print('M', end="")
            else:
                print('.', end="")
        print()


for areas in (lareas,rareas):
    togo = set()
    seen = set()
    for node in areas:
        if node not in loop and 0<=node[1]<len(text) and 0<=node[0]<len(text[0]):
            togo.add(node)

    nope=0
    while togo:
        #draw(togo)
        node = togo.pop()
        seen.add(node)
        for delta in (u,d,l,r):
            n = add(node,delta)
            if not (0<=n[1]<len(text) and 0<=n[0]<len(text[0])):
                nope = 1
                break
            if n not in seen and n not in loop:
                togo.add(n)
        if nope:
            break
    if not nope:
        print(f"gold res: {len(seen)}")
print(f"silver res: {max(dists.values())}")