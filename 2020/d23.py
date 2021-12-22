arr = list(map(int,list("487912365")))
#arr = list(map(int,list("389125467")))
cur = 0
for i in range(100):
    print(i)
    print(arr)
    curn = arr[cur]
    pickup  = []
    pcur = (cur+1)%9
    pc = pcur
    for j in range(3):
        pickup.append(arr[pcur])
        pcur = (pcur+1)%9
    newloc = ((arr[cur]-1)-1)%9+1
    while newloc in pickup:
        newloc = ((newloc-1)-1)%9+1
    for j in range(3):
        try:
            arr.pop(pc)
        except:
            arr.pop(0)
    newlocc = arr.index(newloc)
    arr.insert(newlocc+1, pickup.pop(-1))
    arr.insert(newlocc+1, pickup.pop(-1))
    arr.insert(newlocc+1, pickup.pop(-1))
    while arr[cur] != curn:
        arr.append(arr.pop(0))
    cur = (cur+1)%9

print(arr)