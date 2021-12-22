inp = open("inp1","r")
res = 0
arr  = []
for l in inp.readlines():
    arr.append(int(l))


last = arr[0]+arr[1]+arr[2]
window = arr[3]+arr[1]+arr[2]

for i in range(4,len(arr)):
    if window > last:
        res+=1
    last = window
    window -= arr[i-3]
    window += arr[i]
if window > last:
    res += 1
print(res)