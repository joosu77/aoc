import sys
sys.setrecursionlimit(999999999)
for l in open(sys.argv[1],"r").readlines():
    print(l)
    print((lambda f: f(f,l,ord(l[0]),0,0)*10+f(f,l[::-1],ord(l[-1]),0,1))(lambda f,x,h,c,m: int(x[c]) if x[c].isnumeric() else {h%256**3:{h%256**4:{h:f(f,x,(h*256+ord(x[c+1]))%256**5,c+1,m),499968533861 if m else 435493693556:3, 495623497070 if m else 474148660595:7,435560081524 if m else 499967813989:8}[h], 1718580594 if m else 1920298854:4, 1718187621 if m else 1702259046:5, 1852403301 if m else 1701734766:9}[h%256**4],7302757 if m else 6647407:1,7632751 if m else 7305076:2,7563640 if m else 7891315:6}[h%256**3]))
print(sum([(lambda f: f(f,l,ord(l[0]),0,0)*10+f(f,l[::-1],ord(l[-1]),0,1))(lambda f,x,h,c,m: int(x[c]) if x[c].isnumeric() else {h%256**3:{h%256**4:{h:f(f,x,(h*256+ord(x[c+1]))%256**5,c+1,m),499968533861 if m else 435493693556:3, 495623497070 if m else 474148660595:7,435560081524 if m else 499967813989:8}[h], 1718580594 if m else 1920298854:4, 1718187621 if m else 1702259046:5, 1852403301 if m else 1701734766:9}[h%256**4],7302757 if m else 6647407:1,7632751 if m else 7305076:2,7563640 if m else 7891315:6}[h%256**3]) for l in open(sys.argv[1],"r").readlines()]))
