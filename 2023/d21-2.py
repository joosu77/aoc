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

N= 26501365
N=1000
s=0
ss=0
for i in range(N):
    qn = set()
    while q:
        n = q.pop()
        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            next = (n[0]+d[0],n[1]+d[1])
            if text[next[0]%len(text)][next[1]%len(text[0])] != "#":
                qn.add(next)
    if i%131==64:
        print(f"{i+1}: {len(qn)} {len(qn)-s} {len(qn)-s-ss}")
        ss=len(qn)-s
        s = len(qn)
    q = qn

    
print(f"silver res: {len(q)}")