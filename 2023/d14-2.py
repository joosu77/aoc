import sys,re
inp = open(sys.argv[1],"r")

sys.setrecursionlimit(int(1e8))

text = [list(l.strip()) for l in inp.readlines()]

res=0
mat = []
mats = {}
th = tuple([tuple(l) for l in text])
#mats[th] = 0
#for l in range(len(text)):

for ii in range(4*3000):
    
    
    if ii%4 == 0 and 0:
        th = tuple([tuple(l) for l in text])
        if th in mats:
            print("jou")
            print(ii)
            print(mats[th])
            while 1:
                pass
        mats[th] = ii
    
    ctr=0
    res=0
    if ii%28==24 and 0:
        for ll in text[::1]:
            print("".join(ll))
    for ll in text[::-1]:
        res+=ll.count("O")*(ctr+1)
        ctr+=1
    if ii%(552-376) == 128:
        print(res)
    #if (ii)%(40-12) == 24:
    #    print(res)
    
    
    
    for i in range(len(text)):
        for j in range(len(text[0])):
            if text[i][j] == 'O':
                ctr = i
                text[i][j] = '.'
                while ctr>=0 and text[ctr][j] == '.':
                    ctr-=1
                ctr+=1
                text[ctr][j] = 'O'
    
    text = [list(l)[::-1] for l in zip(*text)]
    #text = list(map(list, zip(*l)))
    
    #while ii==504:
    #    pass    
    
print(f"silver res: {res}")