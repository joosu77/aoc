import sys,re
inp = open(sys.argv[1],"r")


muls = []

res=0
for l in inp.readlines():
    ll = l.split(":")[1].split("|")
    win = set(ll[0].split())
    mine = ll[1].split()
    ctr = 0
    if len(muls):
        mul = muls[0]
        del muls[0]
    else:
        mul = 0
    res+=mul+1
    for m in mine:
        if m in win:
            if len(muls)==ctr:
                muls.append(0)
            muls[ctr]+=mul+1
            ctr+=1
print(res)