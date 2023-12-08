import re,sys
print(sum([(lambda x,f: f(x[0])*10+f(x[-1]))(re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))",l), lambda w: int(w) if w.isnumeric() else {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}[w]) for l in open(sys.argv[1],"r").readlines()]))
