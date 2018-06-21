from blokus.player import Player
from blokus.utils import encodeFourCode
from blokus.piece import Pieces

import numpy as num
import ok as oka
import piece as pie
#バグ理由：１回使ったピースの合法手も出している
#解決法：この関数で使ったピースを呼び出さないようにする
def Nokori(gouhou,pieces,count):
    gouhousyu=[]
    for i in range (21-count+1):
        if pieces[i]=='a':
            A=pie.Apie(gouhou)
            gouhousyu=gouhousyu+A
        if pieces[i]=='b':
            B=pie.Bpie(gouhou)
            gouhousyu=gouhousyu+B
        if pieces[i]=='c':
            C=pie.Cpie(gouhou)
            gouhousyu=gouhousyu+C
        if pieces[i]=='d':
            D=pie.Dpie(gouhou)
            gouhousyu=gouhousyu+D
        if pieces[i]=='e':
            E=pie.Epie(gouhou)
            gouhousyu=gouhousyu+E
        if pieces[i]=='f':
            F=pie.Fpie(gouhou)
            gouhousyu=gouhousyu+F
        if pieces[i]=='g':
            G=pie.Gpie(gouhou)
            gouhousyu=gouhousyu+G
        if pieces[i]=='h':
            H=pie.Hpie(gouhou)
            gouhousyu=gouhousyu+H
        if pieces[i]=='i':
            I=pie.Ipie(gouhou)
            gouhousyu=gouhousyu+I
        if pieces[i]=='j':
            J=pie.Jpie(gouhou)
            gouhousyu=gouhousyu+J
        if pieces[i]=='k':
            K=pie.Kpie(gouhou)
            gouhousyu=gouhousyu+K
        if pieces[i]=='l':
            L=pie.Lpie(gouhou)
            gouhousyu=gouhousyu+L
        if pieces[i]=='m':
            M=pie.Mpie(gouhou)
            gouhousyu=gouhousyu+M
        if pieces[i]=='n':
            N=pie.Npie(gouhou)
            gouhousyu=gouhousyu+N
        if pieces[i]=='o':
            O=pie.Opie(gouhou)
            gouhousyu=gouhousyu+O
        if pieces[i]=='p':
            P=pie.Ppie(gouhou)
            gouhousyu=gouhousyu+P
        if pieces[i]=='q':
            Q=pie.Qpie(gouhou)
            gouhousyu=gouhousyu+Q
        if pieces[i]=='r':
            R=pie.Rpie(gouhou)
            gouhousyu=gouhousyu+R
        if pieces[i]=='s':
            S=pie.Spie(gouhou)
            gouhousyu=gouhousyu+S
        if pieces[i]=='t':
            T=pie.Tpie(gouhou)
            gouhousyu=gouhousyu+T
        if pieces[i]=='u':
            U=pie.Upie(gouhou)
            gouhousyu=gouhousyu+U
        
    return gouhousyu


def Yusen(gouhou,pieces,count):
    gouhousyu=[]
    for i in range (21-count+1):
        if pieces[i]=='j':
            J=pie.Jpie(gouhou)
            gouhousyu=gouhousyu+J
        if pieces[i]=='k':
            K=pie.Kpie(gouhou)
            gouhousyu=gouhousyu+K
        if pieces[i]=='l':
            L=pie.Lpie(gouhou)
            gouhousyu=gouhousyu+L
        if pieces[i]=='m':
            M=pie.Mpie(gouhou)
            gouhousyu=gouhousyu+M
        if pieces[i]=='n':
            N=pie.Npie(gouhou)
            gouhousyu=gouhousyu+N
        if pieces[i]=='o':
            O=pie.Opie(gouhou)
            gouhousyu=gouhousyu+O
        if pieces[i]=='p':
            P=pie.Ppie(gouhou)
            gouhousyu=gouhousyu+P
        if pieces[i]=='q':
            Q=pie.Qpie(gouhou)
            gouhousyu=gouhousyu+Q
        if pieces[i]=='r':
            R=pie.Rpie(gouhou)
            gouhousyu=gouhousyu+R
        if pieces[i]=='s':
            S=pie.Spie(gouhou)
            gouhousyu=gouhousyu+S
        if pieces[i]=='t':
            T=pie.Tpie(gouhou)
            gouhousyu=gouhousyu+T
        if pieces[i]=='u':
            U=pie.Upie(gouhou)
            gouhousyu=gouhousyu+U
        
    return gouhousyu

    
    

    
