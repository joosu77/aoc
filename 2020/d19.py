import re

def replace(a,b):
    for k,v in rules.items():
        s = ""
        for i in v.split(" "):
            if i == a:
                s += b
            else:
                s += i
            s += " "
        rules[k] = s.strip()

f = open("inp19", "r")

rules = {}
strs = []
ruls = True
for l in f.readlines():
    if not l.strip():
        ruls = False
        pass
    if ruls:
        rules[l.split(": ")[0]] = l.split(": ")[1].strip()
    else:
        strs.append(l.strip())

tbr = []

for k,v in rules.items():
    if not (k == "0" or k == "8" or k == "11" or ("|" in v)):
        replace(k,v)
        tbr.append(k)
for t in tbr:
    del rules[t]
tbr = []

for k,v in rules.items():
    if not (k == "0" or k == "8" or k == "11"):
        replace(k,"( "+v+" )")
        tbr.append(k)
for t in tbr:
    del rules[t]

for k,v in rules.items():
    vc = "".join("".join(v.split(" ")).split('"'))
    print(f"{k}: {vc}")

n = "".join("".join(rules["0"].split(" ")).split('"'))
k = "".join("".join(rules["8"].split(" ")).split('"'))
y = "".join("".join(rules["11"].split(" ")).split('"'))
y1,y2 = y.split("11")

k = k[:-1]

r = re.compile("^("+k+")+"+y1+y2+"$")
rs = []
for i in range(1,20):
    rs.append(re.compile("^("+k+")+"+y1*i+y2*i+"$"))
res = 0
for s in strs:
    for rr in rs:
        if rr.match(s):
            res+=1
            break
print(res)