import sys,re
inp = open(sys.argv[1],"r")

sys.setrecursionlimit(int(1e8))

text = inp.readlines()

res=0
mat = []
#for l in range(len(text)):
for ll in text:
    l = ll.strip()
    if l:
        mat.append(l)
    else:
        dun=0
        mistakes=0
        for cent in range(1,len(mat)):
            bork = 0
            for i in range(0,len(mat)):
                if cent-i-1>= 0 and cent+i<len(mat) and mat[cent+i] != mat[cent-i-1]:
                    bork = 1
            if not bork:
                res+=cent*100
                dun=1
                #break
        #if not dun:
        mat = list(map(list,zip(*mat)))
        for cent in range(1,len(mat)):
            bork = 0
            for i in range(0,len(mat)):
                if cent-i-1>= 0 and cent+i<len(mat) and mat[cent+i] != mat[cent-i-1]:
                    bork = 1
            if not bork:
                res+=cent
                dun=1
                #break
        if not dun:
            print("\n".join(["".join(l) for l in mat]))
            print()
        mat = []
   

print(f"silver res: {res}")