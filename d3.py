inp = open("inp3","r")


def f(arr, bitnr, oxy):
    print (arr)
    nums = [0,0,0,0,0,0,0,0,0,0,0,0]
    nums2 = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in arr:
        if i[bitnr]=='1':
            nums[bitnr]+=1
        else:
            nums2[bitnr]+=1
    res = []
    comm = "1" if nums[bitnr]>nums2[bitnr] else ("1" if nums[bitnr] == nums2[bitnr] else "0")
    for i in arr:
        if i[bitnr] == comm and oxy:
            res.append(i)
        elif i[bitnr] != comm and not oxy:
            res.append(i)
    return res


x = 0
y= 0
aim = 0
arr = []
nums = [0,0,0,0,0,0,0,0,0,0,0,0]
nums2 = [0,0,0,0,0,0,0,0,0,0,0,0]
for l in inp.readlines():
    arr.append(l.strip())

print("alustan ocy")
oxy = arr
bitnr =0
while len(oxy) > 1:
    oxy = f(oxy, bitnr, True)
    bitnr+=1
print(oxy)
print("alustan co2")
co2 = arr
bitnr = 0
while len(co2) > 1:
    co2 = f(co2, bitnr, False)
    bitnr+=1
print(co2)

print(int(oxy[0],2)*int(co2[0],2))