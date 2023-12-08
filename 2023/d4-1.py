import sys,re
inp = open(sys.argv[1],"r")


nn = [12,13,14]

res=0
for l in inp.readlines():
    ll = l.split(":")[1].split("|")
    win = set(ll[0].split())
    mine = ll[1].split()
    score = 1
    for m in mine:
        if m in win:
            score*=2
    if score > 1:
        res+=score/2
print(res)