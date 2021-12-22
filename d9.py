inp = open("inp9","r")
res=0
arr = []
basin = []
for l in inp.readlines():
    arr.append(l.strip())

def findBasin(y,x):
    basin[y][x] = 1
    res = 1
    v = arr[y][x]
    if y>0 and basin[y-1][x] == 0 and arr[y-1][x]>v:
        res += findBasin(y-1,x)
    if x>0 and basin[y][x-1] == 0 and arr[y][x-1]>v:
        res += findBasin(y,x-1)
    if y<len(arr)-1 and basin[y+1][x] == 0 and arr[y+1][x]>v:
        res += findBasin(y+1,x)
    if x<len(arr[y])-1 and basin[y][x+1] == 0 and arr[y][x+1]>v:
        res += findBasin(y,x+1)
    return res


sizes = []
for y in range(len(arr)):
    for x in range(len(arr[y])):
        v = arr[y][x]
        if (y==0 or arr[y-1][x]>v) and (x==0 or arr[y][x-1]>v) and (y==len(arr)-1 or arr[y+1][x]>v) and (x==len(arr[y])-1 or arr[y][x+1]>v):
            res+=int(arr[y][x])+1
            basin = []
            for i in range(len(arr)):
                basin.append([])
                for j in arr[i]:
                    if j == '9':
                        basin[i].append(1)
                    else:
                        basin[i].append(0)
            size = findBasin(y,x)
            sizes.append(size)
sizes.sort()

print(sizes[-1]*sizes[-2]*sizes[-3])