def dfs(cur, done):
    done.append(cur)
    print(done)
    for i in m[cur]:
        if i not in done:
            dfs(i,done)
    done.pop(-1)

m = {'a':['b','c'],'b':['a','c','d'],'c':['b','c','d'],'d':['b','c']}
dfs('a',[])