inp = open("inp11","r")

arr = []
for l in inp.readlines():
    arr.append(list(map(int,list(l.strip()))))

H = len(arr)
W = len(arr[0])



res =0

def flash(x,y):
    global res
    global arr
    res +=1
    for dx in range(0,3):
        for dy in range(0,3):
            try:
                if y+dy-1 != -1 and x+dx-1 != -1:
                    arr[y+dy-1][x+dx-1]+=1
                    if arr[y+dy-1][x+dx-1] == 10:
                        flash(x+dx-1,y+dy-1)
            except:
                pass

for i in range (1000):
    for y in range(H):
        for x in range(W):
            arr[y][x]+=1
            if arr[y][x] == 10:
                flash(x,y)
    for y in range(H):
        for x in range(W):
            if arr[y][x] > 9:
                arr[y][x] = 0
    for y in range(H):
        for x in range(W):
            print(arr[y][x],end="")
        print()
    print()
    if sum([sum(l) for l in arr]) == 0:
        print (i)
        break

print(res)     
print(arr)