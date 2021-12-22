f = open("inp21", "r")

arr = []
for l in f.readlines():
    ings = l.split("(contains")[0].strip().split()
    alls = l.split("(contains")[1].strip()[:-1].split(", ")
    arr.append([alls,set(ings)])

alls = {}
allings = set()
for i in arr:
    allings = allings | i[1]
    for all in i[0]:
        if all not in alls:
            alls[all] = i[1]
        else:
            alls[all] = alls[all] & i[1]

ress = []

for k,v in alls.items():
    if k != "fish":
        alls[k]-=alls["fish"]
    if k != "fish" and k != "sesame":
        alls[k]-=alls["sesame"]
    if k != "fish" and k!= "sesame" and k!= "shellfish":
        alls[k]-=alls["shellfish"]
    if k != "fish" and k!= "sesame" and k!= "shellfish" and k!="peanuts":
        alls[k]-=alls["peanuts"]
    if k != "fish" and k!= "sesame" and k!= "shellfish" and k!="peanuts" and k!="nuts":
        alls[k]-=alls["nuts"]
    print(f"{k}: {v}")
    allings -= v
    ress.append([k,v.pop()])
ress.sort()
print(",".join([i[1] for i in ress]))
    


res=0
for i in arr:
    for j in i[1]:
        if j in allings:
            res+=1
print(res)