import sys,re
inp = open(sys.argv[1],"r")

text = inp.readlines()

g = set()

cols = set()
res=0

dp = {}

def solvew(running,cur,num,s):
    if (running,cur,num,s) in dp:
        return dp[(running,cur,num,s)]
    res = solve(running,cur,num,s)
    dp[(running,cur,num,s)] =res
    return res

def solve(running, cur, num, s):
    if s:
        c = s[0]
        if c == '.':
            if running == 1:
                if num == len(nums) or nums[num] != cur:
                    return 0
                num+=1
            return solvew(0,0,num,s[1:])
        elif c == '#':
            return solvew(1,cur+1,num,s[1:])
        else:
            r = solvew(1,cur+1,num,s[1:])
            if running:
                if num != len(nums) and nums[num] == cur:
                    r += solvew(0,0,num+1,s[1:])
            else:
                r+= solvew(0,0,num,s[1:])
            return r
    if running:
        if num == len(nums) or nums[num] != cur:
            return 0
        num+=1
    if num<len(nums):
        return 0
    return 1


missing = 0
for l in range(len(text)):
    dp = {}
    nums = text[l].split()[1].split(",")
    nums = list(map(int,nums))
    ll = text[l].split()[0]
    print((r:=solvew(0,0,0,ll)))
    res+=r
   

print(f"silver res: {res}")