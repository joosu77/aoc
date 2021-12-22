inp = open("inp18","r")
#inp = open("test18","r")

def decode(x):
    try:
        return int(x)
    except:
        ctr = 1
        num = 0
        while not (not num and x[ctr] == ","):
            if x[ctr] == '[':
                num+=1
            if x[ctr] == ']':
                num-=1
            ctr+=1
        return [decode(x[1:ctr]), decode(x[ctr+1:-1])]

def addl(x, num):
    if type(x) == type(1):
        return num+x
    else:
        return [addl(x[0],num), x[1]]

def addr(x, num):
    if type(x) == type(1):
        print(num,x)
        return num+x
    else:
        return [x[0], addr(x[1],num)]

def explode(x, tase):
    if type(x[0]) == type(1) or type(x[1]) == type(1):
        if type(x[0]) == type(1) and type(x[1]) == type(1):
            if tase > 3:
                return [0,x[0],x[1]]
            else:
                return x
        elif type(x[1]) == type(1):
            v = explode(x[0], tase+1)
            if len(v) > 2:
                return [[v[0],x[1]+v[2]], v[1], 0]
            else:
                return x
        else:
            v = explode(x[1], tase+1)
            if len(v) > 2:
                return [[x[0]+v[1], v[0]], 0, v[2]]
            else:
                return x
    else:
        v = explode(x[0],tase+1)
        if len(v) > 2:
            ret = addl(x[1], v[2])
            return  [[v[0],ret], v[1], 0]
        else:
            v = explode(x[1], tase+1)
            if len(v) > 2:
                ret = addr(x[0], v[1])
                return [[ret, v[0]], 0, v[2]]
            else:
                return x

def split(x):
    if type(x)==type(1):
        if x > 9:
            return [x//2, (x+1)//2]
        else:
            return x
    v1 = split(x[0])
    if v1 != x[0]:
        return [v1,x[1]]
    return [x[0], split(x[1])]

arr = []
for l in inp.readlines():
    ll = l.strip()
    val = decode(ll)
    arr.append(val)

print(arr)

sum = arr[0]
for i in range(1,len(arr)):
    sum = [sum,arr[i]]
    while True:
        print(sum)
        print()
        usum = explode(sum,0)
        if len(usum)>2:
            sum = usum[0]
            continue
        uusum = split(sum)
        if uusum != sum:
            sum = uusum
            continue
        break

print(sum)
def magn(x):
    if type(x) == type(1):
        return x
    else:
        return magn(x[0])*3+magn(x[1])*2
print(magn(sum))