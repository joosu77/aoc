inp = open("inp10","r")
res=0
arr = []

broke = False

def check(s, ctr, num):
    global res
    global broke
    print(ctr,num)
    c = 0
    sq = 0
    n = 0
    r = 0
    i = ctr
    while i<len(s):
        if s[i] == "(":
            i = check(s,i+1,0)
        elif s[i] == ")":
            if num == 0:
                return i+1
            else:
                broke = True
                #res += 3
                return 10000000
        elif s[i] == "[":
            i = check(s, i+1, 1)
        elif s[i] == "]":
            print([i,num,ctr])
            if num == 1:
                return i+1
            else:
                broke = True
                #res += 57
                return 10000000
        elif s[i] == "{":
            i = check(s, i+1, 2)
        elif s[i] == "}":
            if num == 2:
                return i+1
            else:
                broke = True
                #res += 1197
                return 10000000
        elif s[i] == "<":
            i = check(s, i+1, 3)
        elif s[i] == ">":
            if num == 3:
                return i+1
            else:
                broke = True
                #res += 25137
                return 10000000
        #i+=1
    print([')',']','}','>'][num])
    res=res*5+num+1
    return 10000000

def isCor(s):
    num = 0
    for c in s:
        if c == "(" or c == "[" or c == "<" or c == "{":
            num+=1
#        e


ress = []
for l in inp.readlines():
    broke = False
    res=0
    check(l.strip(),0,-1)
    res/=5
    if not broke:
        ress.append(res)
        print(l)
        print(res)
ress.sort()
print(ress[len(ress)//2])     