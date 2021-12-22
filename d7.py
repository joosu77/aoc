inp = open("inp7","r")

nums = list(map(int,inp.readline().split(",")))

def pasc(x):
    return x*(x+1)/2

print(pasc(16-5))

s = sum(nums)
l = len(nums)
mid = s//l

print(mid)

res = sum([pasc(abs(i-mid)) for i in nums])

while  res > sum([pasc(abs(i-mid-1)) for i in nums]):
    mid+=1
    res = min(res, sum([pasc(abs(i-mid)) for i in nums]))
while  res > sum([pasc(abs(i-mid+1)) for i in nums]):
    mid-=1
    res = min(res, sum([pasc(abs(i-mid)) for i in nums]))

print(res)


