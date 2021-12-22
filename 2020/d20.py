f = open("inp20","r")

def rot1(img):
    new = []
    for l in img:
        new.append(l.copy())
    for y in range(len(img)):
        for x in range(len(img)):
            new[x][len(img)-y-1] = img[y][x]
    return new

def rot(img, num):
    res = rot1(img)
    for i in range(num-1):
        res = rot1(res)
    return res

def flip(img):
    res = []
    for l in img:
        res.append(list(reversed(l)))
    return res

def match(img1, img2, sideOn1):
    # sideOn1:
    
    # img1 | img2 -> 0
    
    # img1
    # ---- -> 1
    # img2
    if sideOn1:
        return img1[-1] == img2[0]
    else:
        return rot(img1,3)[0] == list(reversed(rot1(img2)[0]))

tiles = {}
tilenum = 0
tile = []
tedges = {}
for l in f.readlines():
    if not l.strip():
        if tilenum:
            tiles[tilenum] = tile
        tilenum = 0
        tile = []
    elif l[0] == "T":
        tilenum = int(l.strip().split()[1][:-1])
    else:
        lin = [1 if c == "#" else 0 for c in l.strip()]
        tile.append(lin)

edges = {}
for i,t in tiles.items():
    tedges[i] = []
    for j in range(4):
        try:
            edges[tuple(t[0])]+=1
        except:
            edges[tuple(t[0])]=1
        tedges[i].append(t[0])
        t = rot1(t)

tilecons = {}

for i,es in tedges.items():
    tilecons[i] = []
    for j in range(4):
        tilecons[i].append(0)
        rev = list(reversed(es[j]))
        print(tuple(rev))
        for u,num in edges.items():
            if u == tuple(rev) or u == tuple(list(es[j])):
                tilecons[i][-1]+=num

print(edges)
print(len(edges))
print(len(tiles))
print(tilecons)
for k,v in tilecons.items():
    if sum(v) == 6:
        print(k)

final = [[]]
final[0].append(flip(rot(tiles[1663],2)))
usedk = [1663]
for y in range(12):
    for x in range(12):
        print()
        print(usedk)
        print(len(final))
        print(len(final[0]))
        print(len(final[-1]))
        print(x)
        print(y)
        if x == 0:
            if y != 0:
                final.append([])
                for num,tile in tiles.items():
                    if num not in usedk:
                        for j in range(4):
                            if match(final[y-1][x],rot(tile,j+1), 1):
                                final[y].append(rot(tile,j+1))
                                usedk.append(num)
                            elif match(final[y-1][x],flip(rot(tile,j+1)), 1):
                                final[y].append(flip(rot(tile,j+1)))
                                usedk.append(num)
   
        else:
            for num,tile in tiles.items():
                if num not in usedk:
                    for j in range(4):
                        if match(final[y][x-1],rot(tile,j+1), 0):
                            final[y].append(rot(tile,j+1))
                            usedk.append(num)
                        elif match(final[y][x-1],flip(rot(tile,j+1)), 0):
                            final[y].append(flip(rot(tile,j+1)))
                            usedk.append(num)

for y in range(12):
    for x in range(12):
        final[y][x].pop(0)
        final[y][x].pop(-1)
        for z in range(len(final[y][x])):
            final[y][x][z].pop(0)
            final[y][x][z].pop(-1)
fin = []
for i in range(12*8):
    fin.append([])
for y in range(12):
    for x in range(12):
        for y2 in range(8):
            fin[y*8+y2] += final[y][x][y2]
for f in fin:
    print (f)

def f():
    snake = [[1 if c == "#" else 0 for c in s] for s in ["                  # ","#    ##    ##    ###"," #  #  #  #  #  #   "]]
    snakes=0
    for y in range(len(fin)-3):
        for x in range(len(fin)-len(snake[0])):
            broke = False
            for dy in range(3):
                for dx in range(len(snake[0])):
                    if snake[dy][dx] == 1 and fin[y+dy][x+dx] == 0:
                        broke = True
            if not broke:
                snakes+=1
                for dy in range(3):
                    for dx in range(len(snake[0])):
                        if snake[dy][dx] == 1:
                            fin[y+dy][x+dx] = 2

    res =0
    for y in fin:
        for x in y:
            if x == 1:
                res+=1
    print(res)
    print(snakes)


for j in range(4):
    fin = rot1(fin)
    f()
    print()
    fin = flip(fin)
    f()
    print()