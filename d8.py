inp = open("inp8","r")
res=0
for l in inp.readlines():
    sis,out = l.split(" | ")
    
    sislst = sis.split()
    m = {}
    for s in sislst:
        if len(s) == 2:
            m[1] = set(s)
        if len(s) == 3:
            m[7] = set(s)
        if len(s) == 4:
            m[4] = set(s)
        if len(s) == 7:
            m[8] = set(s)
    for s in sislst:
        if len(s) == 6: #0,6,9
            if not ((set(s) & m[1]) == m[1]):
                m[6] = set(s)
            elif (set(s) & m[4]) == m[4]:
                m[9] = set(s)
            else:
                m[0] = set(s)
        if len(s) == 5: #2,3,5
            print(set(s))
            print(m[1])
            print(set(s) & m[1])
            if (set(s) & m[1]) == m[1]:
                m[3] = set(s)
            elif len(set(s) & m[4]) == 3:
                m[5] = set(s)
            else:
                m[2] = set(s)
    
    num = 0
    lst = out.split()
    print(type(m))
    for i in lst:
        for k,v in m.items():
            if set(i) == v:
                num = num*10+k
    res+=num
    print(num)

print(res)