inp = open("inp2","r")

x = 0
y= 0
aim = 0
for l in inp.readlines():
    if l.split()[0] == "forward":
        x+= int(l.split()[1])
        y+= aim*int(l.split()[1])
    elif l.split()[0] == "up":
        aim-= int(l.split()[1])
    elif l.split()[0] == "down":
        aim+= int(l.split()[1])

print(x*y)