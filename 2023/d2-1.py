import sys,re
inp = open(sys.argv[1],"r")

abc=["zero","one","two","three","four","five","six","seven","eight","nine"]

nn = [12,13,14]

res=0
for l in inp.readlines():
    broke=0
    ll = l.split(":")
    num = re.findall(r"(?=\d)",ll[0])
    minn = [0,0,0]
    for game in ll[1].split(";"):
        nr = re.findall(r"\d* red",game)
        try:
            if int(nr[0].split(" ")[0]) > minn[0]:
                minn[0] = int(nr[0].split(" ")[0])
        except:
            pass
        nr = re.findall(r"\d* green",game)
        try:
            if int(nr[0].split(" ")[0]) > minn[1]:
                minn[1] = int(nr[0].split(" ")[0])
        except:
            pass
        try:
            nr = re.findall(r"\d* blue",game)
            if int(nr[0].split(" ")[0]) > minn[2]:
                minn[2] = int(nr[0].split(" ")[0])
        except:
            pass
    if not broke:
        #res+=int(ll[0].split(" ")[1])
        res+=minn[0]*minn[1]*minn[2]
print(res)