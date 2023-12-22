import sys,re
inp = open(sys.argv[1],"r")

sys.setrecursionlimit(int(1e8))

text = [list(l.strip()) for l in inp.readlines()]

res=0
mat = []
#for l in range(len(text)):

for i in range(len(text)):
    for j in range(len(text[0])):
        if text[i][j] == 'O':
            ctr = i
            text[i][j] = '.'
            while ctr>=0 and text[ctr][j] == '.':
                ctr-=1
            ctr+=1
            text[ctr][j] = 'O'

ctr=0
for ll in text[::-1]:
    res+=ll.count("O")*(ctr+1)
    ctr+=1
    

print(f"silver res: {res}")