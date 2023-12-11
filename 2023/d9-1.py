import sys,re
inp = open(sys.argv[1],"r")

sss = []
d1 = True

text = inp.readlines()
res=0

for l in text:
    ll = list(map(int,l.split()))
    mat = [ll]
    for _ in range(len(ll)-1):
        mat.append([mat[-1][i+1]-mat[-1][i] for i in range(len(mat[-1])-1)])
    res+=sum(mat[i][-1] for i in range(len(mat)))
print(res)