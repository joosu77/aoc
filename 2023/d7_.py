import sys
print((lambda ctr: sum(map(lambda x: x[0]*x[1], [(l,(ctr:=ctr+1)) for l in open(sys.argv[1],"r").read()])))(0))
[(lambda x: [(,x,int(l.split()[1])) for cc in set(x)])(["J23456789TQK".index(c) for c in l.split()[0]]) for l in open(sys.argv[1],"r")]