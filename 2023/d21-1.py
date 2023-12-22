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
q=set()
for l in range(len(text)):
    for c in range(len(text[0])):
        if text[l][c] == 'S':
            q.add((l,c))

for _ in range(64):
    qn = set()
    while q:
        n = q.pop()
        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            next = (n[0]+d[0],n[1]+d[1])
            if 0<=next[0]<len(text) and 0<=next[1]<len(text[0]) and text[next[0]][next[1]] != "#":
                qn.add(next)
    q = qn

    
print(f"silver res: {len(q)}")