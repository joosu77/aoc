#import sys
#inp = open("inp21","r")
#inp = open("test210","r")

die = 0

t = 1

def d():
    global die, t
    t+=1
    die=(die)%100+1
    return die

aw = 0
bw = 0

q = []
q.append(((4,8,0,0,0),()))

#def g(a,b,sca,scb,turn):
ga = {}
gb = {}

while q:
    qp, l = q.pop(-1)
    a,b,sca,scb,turn = qp
    print(qp)
    if sca>=21:
        aw +=1
        for i in l:
            if i not in ga:
                ga[i] = 1
            else:
                ga[i] +=1
        continue
    elif scb>=21:
        bw +=1
        for i in l:
            if i not in gb:
                gb[i] = 1
            else:
                gb[i] += 1
        continue
    if turn:
        for _ in range(3):
            b = b%10+1
            inp = (a,b,sca,scb+b,(turn+1)%2)
            if inp not in ga:
                q.append((inp,l+(inp,)))
            else:
                aw += ga[inp]
    else:
        for _ in range(3):
            a = a%10+1
            inp = (a,b,sca+a,scb,(turn+1)%2)
            if inp not in gb:
                q.append((inp,l+(inp,)))
            else:
                bw += gb[inp]

#g(4,8,0,0,0)
print(aw,bw)

'''
a = 3
b = 4
sca = 0
scb = 0
turn = 0
while sca<1000 and scb<1000:
    if turn:
        for i in range(3):
            b = (b+d()-1)%10+1
        scb +=b
    else:
        for i in range(3):
            a = (a+d()-1)%10+1
        sca +=a
    turn = (turn+1)%2
    print(sca,scb)
print(sca,scb,t)
'''