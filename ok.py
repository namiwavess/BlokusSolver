import numpy as num
def Gouhou(board):#Gouhouという関数名、（）内は他のところから引数を使うとき
    gouhou=num.zeros((28,28))
    copy=num.zeros((28,28))

    for x in range(20):
        for y in range(20):
            copy[x+4][y+4]=board[x][y]#28*28のボードに中２０＊２０部分に上書き

    copy[24][3]=1
    for i in range(3,25):
        gouhou[i][3]=8
        gouhou[i][24]=8
    for j in range(3,25):
        gouhou[3][j]=8
        gouhou[24][j]=8
    #print(copy)
    #print('kokokara,gouhou')
    for x in range(4,24):
        for y in range(4,24):
            if copy[x][y]!=0:     #真ん中判定（置けない9）
                gouhou[x][y]=9
            elif copy[x][y-1]==1 or copy[x][y+1]==1 or copy[x+1][y]==1 or copy[x-1][y]==1:#東西南北（置けない9）
                gouhou[x][y]=9
            elif copy[x+1][y-1]==1 or copy[x+1][y+1]==1 or copy[x-1][y-1]==1 or copy[x-1][y+1]==1:#北東、北西、南東、南西（置ける1）
                gouhou[x][y]=1
                
    #print(gouhou)

    return gouhou

def Ene(board,z,s,t):#敵の置ける場所を探す関数
    ene=num.zeros((28,28))
    copy=num.zeros((28,28))

    for x in range(20):
        for y in range(20):
            copy[x+4][y+4]=board[x][y]#28*28のボードに中２０＊２０部分に上書き

    copy[s][t]=z
    for i in range(3,25):
        ene[i][3]=8
        ene[i][24]=8
    for j in range(3,25):
        ene[3][j]=8
        ene[24][j]=8
    #print(copy)
    #print('kokokara,gouhou')
    for x in range(4,24):
        for y in range(4,24):
            if copy[x][y]!=0:     #真ん中判定（置けない9）
                ene[x][y]=9
            elif copy[x][y-1]==z or copy[x][y+1]==z or copy[x+1][y]==z or copy[x-1][y]==z:#東西南北（置けない9）
                ene[x][y]=9
            elif copy[x+1][y-1]==z or copy[x+1][y+1]==z or copy[x-1][y-1]==z or copy[x-1][y+1]==z:#北東、北西、南東、南西（置ける1）
                ene[x][y]=1
                
    #print(ene)

    return ene

    
