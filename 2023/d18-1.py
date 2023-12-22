import sys,re
inp = open(sys.argv[1],"r")

sys.setrecursionlimit(int(1e8))

text = [l.strip() for l in inp.readlines()]

res=0
nr = 0

ctr = (0,0)
di_old = 0
for l in text:
    #print(ctr)
    d,num,hex=l.split()
    num = int(num)
    num = int(hex[2:-2],16)
    print(num)
    di = "URDL".index(d)
    di = int(hex[-2])
    if (di-di_old)%4==1:
        delta = [(-1,0),(0,1),(1,0),(0,-1)][di_old]
        next = (ctr[0]+delta[0],ctr[1]+delta[1])
        res += (ctr[1]+next[1])*(ctr[0]-next[0])
        ctr = next
    elif (di-di_old)%4==3:
        num-=1
    delta = [(-num,0),(0,num),(num,0),(0,-num)][di]
    next = (ctr[0]+delta[0],ctr[1]+delta[1])
    res += (ctr[1]+next[1])*(ctr[0]-next[0])
    nr+=num
    ctr=next
    di_old=di
delta = [(-1,0),(1,0),(0,-1),(0,1)][di_old]
next = (ctr[0]+delta[0],ctr[1]+delta[1])
res += (ctr[1]+next[1])*(ctr[0]-next[0])
ctr = next

print(ctr)


print(f"silver res: {res/2}")