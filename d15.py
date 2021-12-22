inp = open("inp15","r")
#inp = open("test15","r")

dots = []
res=0
arr = []
m = {}

first = True
lst = ""

for l in inp.readlines():
    ll = l.strip()
    if first:
        first = False
        lst = ll
    else:
        if ll:
            m[ll.split(" -> ")[0]] = ll.split(" -> ")[1]

for i in arr:
    
    
print(res)