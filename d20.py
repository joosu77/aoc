import sys
inp = open("inp20","r")
#inp = open("test20","r")

s = []
arr = []
first = True
n=100
for i in range(100):
    arr.append([0 for i in range(n+200)])

for l in inp.readlines():
    ll = l.strip()
    if not ll:
        continue
    if  first:
        s = [1 if i == "#" else 0 for i in ll]
        first = False
        continue
    arr.append([1 if i == "#" else 0 for i in ll])
    for i in range(100):
        arr[-1] = [0]+arr[-1]+[0]

for i in range(100):
    arr.append([0 for i in range(n+200)])
print(arr)

for w in range (50):
    newarr = []
    for y in range(len(arr)):
        newarr.append([])
        for x in range(len(arr[0])):
            newarr[-1].append(0)
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            binnum = 0
            for dy in range(3):
                for dx in range(3):
                    #if 0<=y+dy-1<n+16 and 0<=x+dx-1<n+16:
                    try:
                        binnum = binnum*2+arr[y+dy-1][x+dx-1]
                    except:
                        if w%2:
                            binnum = 2*binnum+1
                        else:
                            binnum = 2*binnum
            newarr[y][x] = s[binnum]
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            arr[y][x] = newarr[y][x]

    for y in range(len(arr)):
        for x in range(len(arr[0])):
            print("#" if arr[y][x] else " ",end="")
        print()
    print()

#arr.pop(-1)
#arr = [l[:-1] for l in arr]
for y in range(len(arr)):
    for x in range(len(arr[0])):
        print("#" if arr[y][x] else " ",end="")
    print()
print()

print(len(arr))
print(len(arr[0]))


#reS =0
#for y in range(0,100):
#    for x in range(0,100):
#        reS+=arr[y][x]
#print(reS)
print(sum([sum(l) for l in arr]))
print(len(arr))