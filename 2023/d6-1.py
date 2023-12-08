import sys,re
inp = open(sys.argv[1],"r")


t = 40828492
v = 233101111101487
#t = 71530
#v = 940200
res= 1
ch = lambda x: (t-x)*x<v
j = 1
while ch(j):
    j*=2 

small = j//2
big = j
B = big
while big-small>1:
    mid = (small+big)//2
    if ch(mid):
        small = mid
    else:
        big = mid

lowbound = big

j = B
while not ch(j):
    j*=2
small = j//2
big = j
B = big
while big-small>1:
    mid = (small+big)//2
    if not ch(mid):
        small = mid
    else:
        big = mid



print(big-lowbound)