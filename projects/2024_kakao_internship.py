def solution(dice):
    import itertools as i

    adice=list(i.combinations(dice,int(len(dice)/2)))
    win=[]
    for comb in range(len(adice)):
        bdice=dice.copy()
        for i in adice[comb]:
            bdice.remove(i)
        sum=0
        if len(dice)==2:
            for a1 in range(6):
                for b1 in range(6):
                    if int(adice[comb][0][a1])>int(bdice[0][b1]):
                        sum+=1
            win.append(sum)
        elif len(dice)==4:
            for a1 in range(6):
                for a2 in range(6):
                    for b1 in range(6):
                        for b2 in range(6):
                            if int(adice[comb][0][a1])+int(adice[comb][1][a2])>int(bdice[0][b1])+int(bdice[1][b2]):
                                sum+=1
            win.append(sum)
        elif len(dice)==6:
            for a1 in range(6):
                for a2 in range(6):
                    for a3 in range(6):
                        for b1 in range(6):
                            for b2 in range(6):
                                for b3 in range(6):
                                    if int(adice[comb][0][a1])+int(adice[comb][1][a2])+int(adice[comb][2][a3])>int(bdice[0][b1])+int(bdice[1][b2])+int(bdice[2][b3]):
                                        sum+=1
            win.append(sum)
        elif len(dice)==8:
            for a1 in range(6):
                for a2 in range(6):
                    for a3 in range(6):
                        for a4 in range(6):
                            for b1 in range(6):
                                for b2 in range(6):
                                    for b3 in range(6):
                                        for b4 in range(6):
                                            if int(adice[comb][0][a1])+int(adice[comb][1][a2])+int(adice[comb][2][a3])+int(adice[comb][3][a4])>int(bdice[0][b1])+int(bdice[1][b2])+int(bdice[2][b3])+int(bdice[3][b4]):
                                                sum+=1
            win.append(sum)
        elif len(dice)==10:
            for a1 in range(6):
                for a2 in range(6):
                    for a3 in range(6):
                        for a4 in range(6):
                            for a5 in range(6):
                                for b1 in range(6):
                                    for b2 in range(6):
                                        for b3 in range(6):
                                            for b4 in range(6):
                                                for b5 in range(6):
                                                    if int(adice[comb][0][a1])+int(adice[comb][1][a2])+int(adice[comb][2][a3])+int(adice[comb][3][a4])+int(adice[comb][4][a5])>int(bdice[0][b1])+int(bdice[1][b2])+int(bdice[2][b3])+int(bdice[3][b4])+int(bdice[4][b5]):
                                                        sum+=1
            win.append(sum)
    answer=[]
    for i in range(len(dice)):
        for n in range(int(len(dice)/2)):
            if dice[i]==adice[win.index(max(win))][n]:
                answer.append(i+1)
    return answer