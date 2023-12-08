import re,sys
print(sum([int(re.findall(r"Game (\d*)",l)[0]) for l in open(sys.argv[1],"r").readlines() if max([int(i) for i in re.findall(r"(\d*) red",l)]+[0])<13 and max([int(i) for i in re.findall(r"(\d*) green",l)]+[0])<14 and max([int(i) for i in re.findall(r"(\d*) blue",l)]+[0])<15]))
print(sum([max(max([int(i) for i in re.findall(r"(\d*) red",l)],[0]))*max(max([int(i) for i in re.findall(r"(\d*) blue",l)],[0]))*max(max([int(i) for i in re.findall(r"(\d*) green",l)],[0])) for l in open(sys.argv[1],"r").readlines()]))
