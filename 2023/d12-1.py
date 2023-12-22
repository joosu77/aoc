import sys,re
inp = open(sys.argv[1],"r")

text = inp.readlines()

g = set()

cols = set()
res=0

missing = 0
for l in range(len(text)):
    nums = text[l].split()[1].split(",")
    nums = list(map(int,nums))
    q = text[l].split()[0].count("?")
    r= 0
    for i in range(2**q):
        s = ""
        qq = 0
        for c in text[l].split()[0]:
            if c=='?':
                if i&(2**qq):
                    s+="#"
                else:
                    s+="."
                qq+=1
            else:
                s+=c
        running = 0
        cur = 0
        num = 0
        nope = 0
        for c in s:
            if c == '.':
                if running == 1:
                    if num == len(nums) or nums[num] != cur:
                        nope =1
                        break
                    num+=1
                running = 0
                cur = 0
            else:
                running = 1
                cur +=1
        if running:
            if num == len(nums) or nums[num] != cur:
                nope = 1
            num+=1
        if num<len(nums):
            nope=1
        if not nope:
            r+=1
    #print(r)
    res+=r
                

print(f"silver res: {res}")