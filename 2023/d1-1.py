import sys
inp = open(sys.argv[1],"r")

abc=["zero","one","two","three","four","five","six","seven","eight","nine"]

res=0
for l in inp.readlines():
    ll = l
    r = []
    for w in abc:
        #ll = str(abc.index(w)).join(ll.split(w))
        if ll.find(w)!=-1:
            r.append((ll.find(w),abc.index(w)))
            r.append((ll.rfind(w),abc.index(w)))
    for c in range(len(ll)):
        try:
            r.append((c, int(ll[c])))
            break
        except:
            pass
    for c in range(len(ll)):
        try:
            r.append((len(ll)-c-1, int(ll[-c-1])))
            break
        except:
            pass
    r.sort()
    res += r[0][1]*10+r[-1][1]
print(res)