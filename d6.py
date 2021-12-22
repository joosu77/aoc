inp = open("inp6","r")

nums = list(map(int,inp.readline().split(",")))

arr =[]
for i in range(280):
    arr.append(0)


num = len(nums)
for i in nums:
    arr[i]+=1

for i in range(256):
    arr[i+7] += arr[i]
    arr[i+9] += arr[i]
    num += arr[i]

print(num)


