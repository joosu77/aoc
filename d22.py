import sys
inp = open("inp22","r")
inp = open("test22","r")


res=0

arr = []
for l in inp.readlines():
    ll = l.strip()
    t = [l.split()[0],ll.split()[1].split(",")]
    t[0] = 1 if t[0] == "on" else 0
    t = [t[0],t[1][0],t[1][1],t[1][2]]
    t[1] = list(map(int,(t[1].split("=")[1].split(".."))))
    t[2] = list(map(int,t[2].split("=")[1].split("..")))
    t[3] = list(map(int,t[3].split("=")[1].split("..")))
    arr.append(t)



def check(sq1,sq2,minus):
    if sq1[2]<sq2[2] and sq1[3]>sq2[3]:
        if sq1[0]<sq2[0] and sq1[1]>sq2[1]:
            return [[sq1[0],sq1[1],sq1[2],sq2[3]],[sq1[0],sq2[0],sq2[2],sq2[3]],[sq2[1],sq1[1],sq2[2],sq2[3]],[sq1[0],sq1[1],sq2[3],sq1[2]]] if minus else [sq1]
        elif sq1[1]>sq2[1]:
            return [[sq1[0],sq2[1],sq1[2],sq2[2]],[sq2[1],sq1[1],sq1[2],sq1[3]],[sq1[0],sq2[1],sq2[3],sq1[3]]] if minus else [sq1, [sq2[0],sq1[0],sq2[2],sq2[3]]]
        elif sq1[0]>sq2[0] and sq1[1]<sq2[1]:
            return [[sq1[0],sq1[1],sq1[2],sq2[2]],[sq1[0],sq1[1],sq2[3],sq1[3]]] if minus else [[sq1[0],sq1[1],sq1[2],sq2[2]],[sq1[0],sq1[1],sq2[3],sq1[3]],sq2]
    elif sq1[2]>sq2[2] and sq1[3]<sq2[3]:
        if sq2[0]<sq1[0] and sq2[1]>sq1[1]:
            return [] if minus else [sq2]
        elif sq2[1]>sq1[1]:
            return [[sq1[0],sq2[0],sq1[2],sq1[3]]] if minus else [sq2, [sq1[0],sq2[0],sq1[2],sq1[3]]]
    elif sq1[2]<sq2[2] and sq1[3]<sq2[3] and sq1[0]<sq2[0] and sq1[1]<sq2[1]:
        return [[sq1[0],sq1[1],sq1[2],sq2[2]],[sq1[0],sq2[0],sq2[2],sq1[3]]] if minus else [sq2, [sq1[0],sq1[1],sq1[2],sq2[2]],[sq1[0],sq2[0],sq2[2],sq1[3]]]
    return -1

def rot(sq):
    return [-sq[3],-sq[2],sq[0],sq[1]]

def addSq(sqs, sq, m=False):
    print(sqs,sq,m)
    for si in range(len(sqs)):
        sq1 = sq
        sq2 = sqs[si]
        ret = -1
        for turns in range(4):
            if ret == -1:
                ret = check(sq1,sq2,m)
                sq1 = rot(sq1)
                sq2 = rot(sq2)
            else:
                ret = [rot(r) for r in ret]
        if ret != -1:
            end = sqs[si+1:]
            if not end:
                return ret
            for ss in ret:
                end = addSq(end, ss)
            return sqs + end
    return sqs if m else sqs+[sq]
    
squares = {}

for i in arr:
    for x in range(i[1][0],i[1][1]+1):
        if not x in squares:
            squares[x] = []
        squares[x] = addSq(squares[x], [i[2][0],i[2][1],i[3][0],i[3][1]], i[0])
        
    
res = 0    
for sq in squares:
    res += (sq[1]-sq[0]+1)*(sq[3]-sq[2]+1)
print(res)
