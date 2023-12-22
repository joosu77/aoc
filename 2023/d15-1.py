import sys,re
inp = open(sys.argv[1],"r")

sys.setrecursionlimit(int(1e8))

text = [l.strip() for l in inp.readlines()]

ll = text[0].split(",")

res = 0
for l in ll:
    r = 0
    for c in l:
        r = ((r+ord(c))*17)%256
    res+=r

print(f"silver res: {res}")