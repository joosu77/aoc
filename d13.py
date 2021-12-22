inp = open("inp13","r")
#inp = open("test13","r")

dots = []
res=0
arr = []
for i in range(2000):
    arr.append([])
    for j in range(2000):
        arr[-1].append(0)
m = {}

isdot = True
first = False

for l in inp.readlines():
    ll = l.strip()
    if not ll:
        isdot = False
        continue
    if isdot:
        dots.append(list(map(int,ll.split(","))))
        
        arr[dots[-1][1]][dots[-1][0]] = 1
    else:
        telg = ll.split("=")[0][-1]
        n = int(ll.split("=")[1])
        for i in range(n+1,2000):
            for j in range(2000):
                if telg == "y":
                    if arr[i][j]:
                        arr[2*n-i][j] = 1
                        arr[i][j] = 0
                if telg == "x":
                    if arr[j][i]:
                        arr[j][2*n-i] = 1
                        arr[j][i] = 0
        if not first:
            first = True
for i in range(2000):
    for j in range(2000):
        res+=arr[i][j]
        if i<20 and j<100:
            if arr[i][j]:
                print("#",end="")
            else:
                print(" ",end="")
    if i<20:
        print()


print(res)     
