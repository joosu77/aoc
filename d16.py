inp = open("inp16","r")
#inp = open("test16","r")

res=0
l = inp.read().strip()
bits= []
for c in l:
    d = bin(int(c,16))[2:]
    while len(d)<4:
        d = '0'+d
    for cc in d:
        if cc=="1":
            bits.append(1)
        else:
            bits.append(0)


ctr=0
vsum = 0

def evall(l, type):
    if type == 0:
        return sum(l)
    elif type == 1:
        r = 1
        for i in l:
            r*=i
        return r
    elif type == 2:
        return min(l)
    elif type == 3:
        return max(l)
    elif type == 5:
        return 1 if l[0] > l[1] else 0
    elif type == 6:
        return 1 if l[0] < l[1] else 0
    elif type == 7:
        return 1 if l[0] == l[1] else 0
    print(type)
    print("error")

def h2d(x):
    return int("".join(map(str,x)),2)

def parse (bits, pacleft=-1):
    global vsum

    print(bits)

    ret = []
    ctr=0
    while 1:
        try:
            #print(bits[:ctr]+['M']+bits[ctr+1:])
            ver = bits[ctr:ctr+3]
            vsum += h2d(ver)
            ctr+=3
            type = h2d(bits[ctr:ctr+3])
            print(f"type: {type}")
            ctr+=3
            if type == 4:
                lit = 0
                while bits[ctr]:
                    lit*=16
                    lit += h2d(bits[ctr+1:ctr+5])
                    ctr+=5
                lit*=16
                lit += h2d(bits[ctr+1:ctr+5])
                ctr+=5
                #while ctr%4:
                #    ctr+=1
                ret.append( lit)
            elif not bits[ctr]:
                leng = h2d(bits[ctr+1:ctr+16])
                ctr += 16
                ret.append(evall(parse(bits[ctr:ctr+leng]), type))
                ctr += leng
            else:
                pacnum = h2d(bits[ctr+1:ctr+12])
                ctr +=12
                r = parse(bits[ctr:],pacnum)
                ctr += r.pop(-1)
                ret.append(evall(r,type))
            pacleft-=1
            print(ret)
            if ctr==len(bits) or pacleft==0:
                if pacleft ==0:
                    ret.append(ctr)
                return ret
        except:
            return ret
    
res = parse(bits)
    
print(res)
print(vsum)