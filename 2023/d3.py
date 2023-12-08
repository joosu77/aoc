import sys,re

text = open(sys.argv[1],"r").read()
w = text.find("\n")

numbs = re.findall(r"\d+",text)
symbs = re.findall(r"[^0-9.]",text)
for n in numbs:
    if 


res = 0
added = set()
symbs = {}
numbing = 0
for ctr in range(len(text)):
    if text[ctr].isnumeral():
        if not numbing:
            numbing = 1
            added