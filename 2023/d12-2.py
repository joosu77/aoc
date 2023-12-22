import sys,re
inp = open(sys.argv[1],"r")

sys.setrecursionlimit(int(1e8))

text = inp.readlines()

res=0

dp = {}

def solvew(running,cur,num,s):
    if (running,cur,num,s) in dp:
        return dp[(running,cur,num,s)]
    res = solve(running,cur,num,s)
    dp[(running,cur,num,s)] =res
    return res

def solve(running, cur, num, s):
    #if len(s) < sum(nums[num+1:])+len(nums[num+1:])-1 or len(s)-s.count(".") < sum(nums[num+1:]):
    #    return 0
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


for l in range(len(text)):
    dp = {}
    nums = text[l].split()[1].split(",")*5
    nums = list(map(int,nums))
    ll = ((text[l].split()[0]+"?")*5)[:-1]
    res+=solvew(0,0,0,ll)
   

print(f"gold res: {res}")