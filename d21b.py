dp = []

for q in range(10):
    dp.append([])
    for w in range(10):
        dp[-1].append([])
        for e in range(21):
            dp[-1][-1].append([])
            for r in range(21):
                dp[-1][-1][-1].append([0,0])


dp[2][3][0][0][0] = 1
                
aw = 0
bw  = 0

for sca in range(21):
    for scb in range(21):
        for a in range(10):
            for b in range(10):
                for sc1 in range(1,4):
                    for sc2 in range(1,4):
                        for sc3 in range(1,4):
                            sc = sc1+sc2+sc3
                            if scb+(b+sc)%10+1 < 21:
                                dp[a][(b+sc)%10][sca][scb+(b+sc)%10+1][0] += dp[a][b][sca][scb][1]
                            else:
                                bw+=dp[a][b][sca][scb][1]
                            
                            if sca+(a+sc)%10+1 < 21:
                                dp[(a+sc)%10][b][sca+(a+sc)%10+1][scb][1] += dp[a][b][sca][scb][0]
                            else:
                                aw+=dp[a][b][sca][scb][0]
print(aw)
print(bw)