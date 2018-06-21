from blokus.player import Player
from blokus.utils import encodeFourCode
from blokus.piece import Pieces

import numpy as num
import ok as oka
    
#def Pie(gouhou):
def Apie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                h.append(encodeFourCode(x-4,y-4,'a',0))
    #print(h)
    return h

def Bpie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1: 
                if gouhou[x+1][y]<=1:
                    h.append(encodeFourCode(x-4,y-4,'b',0))
                if gouhou[x][y+1]<=1:
                    h.append(encodeFourCode(x-4,y-4,'b',2))
                if gouhou[x-1][y]<=1:
                    h.append(encodeFourCode(x-4,y-4,'b',4))
                if gouhou[x][y-1]<=1:
                    h.append(encodeFourCode(x-4,y-4,'b',6))
    #print(h)
    return h
    
def Cpie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1: 
                if gouhou[x+1][y]<=1 and gouhou[x+2][y]<=1:
                    h.append(encodeFourCode(x-3,y-4,'c',0))
                if gouhou[x-1][y]<=1 and gouhou[x-2][y]<=1:
                    h.append(encodeFourCode(x-5,y-4,'c',0))
                if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1:
                    h.append(encodeFourCode(x-4,y-3,'c',2))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1:
                    h.append(encodeFourCode(x-4,y-5,'c',2))
    #print(h)
    return h
    
def Dpie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x+1][y]<=1:
                    if gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'d',0))
                    if gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'d',1))
                    if gouhou[x][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'d',3))
                    if gouhou[x][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'d',5))
                if gouhou[x][y+1]<=1:
                    if gouhou[x-1][y]<=1:
                        h.append(encodeFourCode(x-4,y-4,'d',0))
                    if gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'d',1))
                    if gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'d',3)) 
                if gouhou[x-1][y]<=1:
                    if gouhou[x][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'d',1))
                    if gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'d',3))
                    if gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'d',5))
                if gouhou[x][y-1]<=1:
                    if gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'d',0))
                    if gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'d',5))
    #print(h)
    return h

def Epie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x+1][y]<=1 and gouhou[x+2][y]<=1 and gouhou[x+3][y]<=1:
                     h.append(encodeFourCode(x-3,y-4,'e',0))
                if gouhou[x-1][y]<=1 and gouhou[x-2][y]<=1 and gouhou[x-3][y]<=1:
                     h.append(encodeFourCode(x-6,y-4,'e',0))
                if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1 and gouhou[x][y+3]<=1:
                     h.append(encodeFourCode(x-4,y-3,'e',2))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1 and gouhou[x][y-3]<=1:
                     h.append(encodeFourCode(x-4,y-6,'e',2))
    #print(h)
    return h

def Fpie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x+1][y]<=1 and gouhou[x+2][y]<=1:
                    if gouhou[x+2][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'f',0))
                    if gouhou[x][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'f',4))
                    if gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'f',1)) 
                    if gouhou[x][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'f',5))
                if gouhou[x-1][y]<=1 and gouhou[x-2][y]<=1:
                    if gouhou[x][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'f',0))
                    if gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'f',4))
                    if gouhou[x][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'f',1)) 
                    if gouhou[x-2][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'f',5))
                if gouhou[x][y+1]<=1: 
                    if gouhou[x-1][y+1]<=1 and gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-3,'f',0))
                    if gouhou[x+1][y+1]<=1 and gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-3,'f',5))
                if gouhou[x][y-1]<=1:
                    if gouhou[x+1][y-1]<=1 and gouhou[x+2][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-5,'f',4))
                    if gouhou[x-1][y-1]<=1 and gouhou[x-2][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-5,'f',1))
                if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1:
                    if gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'f',2))
                    if gouhou[x-1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'f',3))
                    if gouhou[x-1][y]<=1:
                        h.append(encodeFourCode(x-4,y-3,'f',6)) 
                    if gouhou[x+1][y]<=1:
                        h.append(encodeFourCode(x-4,y-3,'f',7))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1:
                    if gouhou[x+1][y]<=1:
                        h.append(encodeFourCode(x-4,y-5,'f',2))
                    if gouhou[x-1][y]<=1:
                        h.append(encodeFourCode(x-4,y-5,'f',3))
                    if gouhou[x-1][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-5,'f',6)) 
                    if gouhou[x+1][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-5,'f',7))
                if gouhou[x-1][y]<=1:
                    if gouhou[x-1][y-1]<=1 and gouhou[x-1][y-2]<=1:
                        h.append(encodeFourCode(x-5,y-5,'f',2))
                    if gouhou[x-1][y+1]<=1 and gouhou[x-1][y+2]<=1:
                        h.append(encodeFourCode(x-5,y-3,'f',7))
                if gouhou[x+1][y]<=1:
                    if gouhou[x+1][y-1]<=1 and gouhou[x+1][y-2]<=1:
                        h.append(encodeFourCode(x-3,y-5,'f',3))
                    if gouhou[x+1][y+1]<=1 and gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-3,y-3,'f',6))
    #print(h)
    return h

def Gpie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x+1][y]<=1 and gouhou[x+2][y]<=1: 
                    if gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'g',0))
                    if gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'g',4))
                if gouhou[x-1][y]<=1 and gouhou[x-2][y]<=1: 
                    if gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'g',0))
                    if gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'g',4))
                if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1: 
                    if gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'g',2))
                    if gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'g',6))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1: 
                    if gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'g',2))
                    if gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'g',6))
                if gouhou[x][y-1]<=1: 
                    if gouhou[x+1][y-1]<=1 and gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'g',0))
                if gouhou[x+1][y]<=1:
                    if gouhou[x+1][y-1]<=1 and gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'g',2))
                if gouhou[x][y+1]<=1: 
                    if gouhou[x-1][y+1]<=1 and gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'g',4))
                if gouhou[x-1][y]<=1: 
                    if gouhou[x-1][y-1]<=1 and gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'g',6))
    #print(h)
    return h

def Hpie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x-1][y]<=1 and gouhou[x-2][y]<=1: 
                    if gouhou[x][y+1]<=1 and gouhou[x+1][y]<=1 and gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'h',0))
                    if gouhou[x-1][y]<=1 and gouhou[x-1][y+1]<=1 and gouhou[x][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'h',2))
                    if gouhou[x][y-1]<=1 and gouhou[x-1][y]<=1 and gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'h',4))
                    if gouhou[x+1][y]<=1 and gouhou[x][y-1]<=1 and gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'h',6))
    #print(h)
    return h

def Ipie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x][y+1]<=1: 
                    if gouhou[x+1][y+1]<=1 and gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'i',0))
                    if gouhou[x-1][y]<=1 and gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'i',0))
                    if gouhou[x-1][y+1]<=1 and gouhou[x-1][y+2]<=1:
                        h.append(encodeFourCode(x-5,y-3,'i',1))
                    if gouhou[x+1][y]<=1 and gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'i',1))
                if gouhou[x+1][y]<=1: 
                    if gouhou[x+1][y-1]<=1 and gouhou[x+2][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-5,'i',2))
                    if gouhou[x][y+1]<=1 and gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'i',2))
                    if gouhou[x+1][y+1]<=1 and gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'i',3))
                    if gouhou[x][y-1]<=1 and gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'i',3))
                if gouhou[x][y-1]<=1: 
                    if gouhou[x+1][y]<=1 and gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'i',0))
                    if gouhou[x-1][y-1]<=1 and gouhou[x-1][y-2]<=1:
                        h.append(encodeFourCode(x-5,y-5,'i',0))
                    if gouhou[x-1][y]<=1 and gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'i',1))
                    if gouhou[x+1][y-1]<=1 and gouhou[x+1][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-5,'i',1))
                if gouhou[x-1][y]<=1: 
                    if gouhou[x][y-1]<=1 and gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'i',2))
                    if gouhou[x-1][y+1]<=1 and gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'i',2))
                    if gouhou[x][y+1]<=1 and gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'i',3))
                    if gouhou[x-1][y-1]<=1 and gouhou[x-2][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-5,'i',3))
    #print(h)
    return h

def Jpie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x+1][y]<=1 and gouhou[x+2][y]<=1 and gouhou[x+3][y]<=1 and gouhou[x+4][y]<=1:
                    h.append(encodeFourCode(x-2,y-4,'j',0))
                if gouhou[x-1][y]<=1 and gouhou[x-2][y]<=1 and gouhou[x-3][y]<=1 and gouhou[x-4][y]<=1:
                    h.append(encodeFourCode(x-6,y-4,'j',0))
                if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1 and gouhou[x][y+3]<=1 and gouhou[x][y+4]<=1:
                    h.append(encodeFourCode(x-4,y-2,'j',2))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1 and gouhou[x][y-3]<=1 and gouhou[x][y-4]<=1:
                    h.append(encodeFourCode(x-4,y-6,'j',2))
    #print(h)
    return h

def Kpie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x+1][y]<=1 and gouhou[x+2][y]<=1 and gouhou[x+3][y]<=1:
                    if gouhou[x+3][y-1]<=1:
                        h.append(encodeFourCode(x-2,y-4,'k',0))
                    if gouhou[x][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'k',4))
                    if gouhou[x+3][y+1]<=1:
                        h.append(encodeFourCode(x-2,y-4,'k',1))
                    if gouhou[x][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'k',5))
                if gouhou[x-1][y]<=1 and gouhou[x-2][y]<=1 and gouhou[x-3][y]<=1:
                    if gouhou[x][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'k',0))
                    if gouhou[x-3][y+1]<=1:
                        h.append(encodeFourCode(x-6,y-4,'k',4))
                    if gouhou[x][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'k',1))
                    if gouhou[x-3][y-1]<=1:
                        h.append(encodeFourCode(x-6,y-4,'k',5))
                if gouhou[x][y+1]<=1:
                    if gouhou[x-1][y+1]<=1 and gouhou[x-2][y+1]<=1 and gouhou[x-3][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-3,'k',0))
                    if gouhou[x+1][y+1]<=1 and gouhou[x+2][y+1]<=1 and gouhou[x+3][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-3,'k',5))
                if gouhou[x][y-1]<=1:
                    if gouhou[x+1][y-1]<=1 and gouhou[x+2][y-1]<=1 and gouhou[x+3][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-5,'k',4))
                    if gouhou[x-1][y-1]<=1 and gouhou[x-2][y-1]<=1 and gouhou[x-3][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-5,'k',1))
                if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1 and gouhou[x][y+3]<=1:
                    if gouhou[x+1][y+3]<=1:
                        h.append(encodeFourCode(x-4,y-2,'k',2))
                    if gouhou[x-1][y]<=1:
                        h.append(encodeFourCode(x-4,y-3,'k',6))
                    if gouhou[x-1][y+3]<=1:
                        h.append(encodeFourCode(x-4,y-2,'k',3))
                    if gouhou[x+1][y]<=1:
                        h.append(encodeFourCode(x-4,y-3,'k',7))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1 and gouhou[x][y-3]<=1:
                    if gouhou[x+1][y]<=1:
                        h.append(encodeFourCode(x-4,y-5,'k',2))
                    if gouhou[x-1][y-3]<=1:
                        h.append(encodeFourCode(x-4,y-6,'k',6))
                    if gouhou[x-1][y]<=1:
                        h.append(encodeFourCode(x-4,y-5,'k',3))
                    if gouhou[x+1][y-3]<=1:
                        h.append(encodeFourCode(x-4,y-6,'k',7))
                if gouhou[x-1][y]<=1:
                    if gouhou[x-1][y-1]<=1 and gouhou[x-1][y-2]<=1 and gouhou[x-1][y-3]<=1:
                        h.append(encodeFourCode(x-5,y-5,'k',2))
                    if gouhou[x-1][y+1]<=1 and gouhou[x-1][y+2]<=1 and gouhou[x-1][y+3]<=1:
                        h.append(encodeFourCode(x-5,y-3,'k',7))
                if gouhou[x+1][y]<=1:
                    if gouhou[x+1][y+1]<=1 and gouhou[x+1][y+2]<=1 and gouhou[x+1][y+3]<=1:
                        h.append(encodeFourCode(x-3,y-3,'k',6))
                    if gouhou[x+1][y-1]<=1 and gouhou[x+1][y-2]<=1 and gouhou[x+1][y-3]<=1:
                        h.append(encodeFourCode(x-3,y-5,'k',3))
    #print(h)
    return h

def Lpie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x+1][y]<=1 and gouhou[x+2][y]<=1:
                    if gouhou[x+2][y-1]<=1 and gouhou[x+3][y-1]<=1:
                        h.append(encodeFourCode(x-2,y-4,'l',0))
                    if gouhou[x][y+1]<=1 and gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'l',4))
                    if gouhou[x+2][y+1]<=1 and gouhou[x+3][y+1]<=1:
                        h.append(encodeFourCode(x-2,y-4,'l',1))
                    if gouhou[x][y-1]<=1 and gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'l',5))
                if gouhou[x-1][y]<=1 and gouhou[x-2][y]<=1:
                    if gouhou[x][y-1]<=1 and gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'l',0))
                    if gouhou[x-2][y+1]<=1 and gouhou[x-3][y+1]<=1:
                        h.append(encodeFourCode(x-6,y-4,'l',4))
                    if gouhou[x][y+1]<=1 and gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'l',1))
                    if gouhou[x-2][y-1]<=1 and gouhou[x-3][y-1]<=1:
                        h.append(encodeFourCode(x-6,y-4,'l',5))
                if gouhou[x+1][y]<=1:
                    if gouhou[x][y+1]<=1 and gouhou[x-1][y+1]<=1 and gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'l',0))
                    if gouhou[x+1][y-1]<=1 and gouhou[x+2][y-1]<=1 and gouhou[x+3][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-5,'l',4))
                    if gouhou[x][y-1]<=1 and gouhou[x-1][y-1]<=1 and gouhou[x-2][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'l',1))
                    if gouhou[x+1][y+1]<=1 and gouhou[x+2][y+2]<=1 and gouhou[x+3][y+3]<=1:
                        h.append(encodeFourCode(x-3,y-3,'l',5))
                if gouhou[x-1][y]<=1:
                    if gouhou[x-1][y+1]<=1 and gouhou[x-2][y+1]<=1 and gouhou[x-3][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-3,'l',0))
                    if gouhou[x][y-1]<=1 and gouhou[x+1][y-1]<=1 and gouhou[x+2][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'l',4))
                    if gouhou[x-1][y-1]<=1 and gouhou[x-2][y-1]<=1 and gouhou[x-3][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-5,'l',1))
                    if gouhou[x][y+1]<=1 and gouhou[x+1][y+1]<=1 and gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'l',5))
                if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1:
                    if gouhou[x+1][y+2]<=1 and gouhou[x+1][y+3]<=1:
                        h.append(encodeFourCode(x-4,y-2,'l',2))
                    if gouhou[x-1][y]<=1 and gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'l',6))
                    if gouhou[x-1][y+2]<=1 and gouhou[x-1][y+3]<=1:
                        h.append(encodeFourCode(x-4,y-2,'l',3))
                    if gouhou[x+1][y]<=1 and gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'l',7))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1:
                    if gouhou[x+1][y]<=1 and gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'l',2))
                    if gouhou[x-1][y-2]<=1 and gouhou[x-1][y-3]<=1:
                        h.append(encodeFourCode(x-4,y-6,'l',6))
                    if gouhou[x-1][y]<=1 and gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-4,'l',3))
                    if gouhou[x+1][y-2]<=1 and gouhou[x+1][y-3]<=1:
                        h.append(encodeFourCode(x-4,y-6,'l',7))
                if gouhou[x][y+1]<=1:
                    if gouhou[x-1][y]<=1 and gouhou[x-1][y-1]<=1 and gouhou[x-1][y-2]<=1:
                        h.append(encodeFourCode(x-5,y-4,'l',2))
                    if gouhou[x+1][y+1]<=1 and gouhou[x+1][y+2]<=1 and gouhou[x+1][y+3]<=1:
                        h.append(encodeFourCode(x-3,y-3,'l',6))
                    if gouhou[x+1][y]<=1 and gouhou[x+1][y-1]<=1 and gouhou[x+1][y-2]<=1:
                        h.append(encodeFourCode(x-3,y-4,'l',3))
                    if gouhou[x-1][y+1]<=1 and gouhou[x-1][y+2]<=1 and gouhou[x-1][y+3]<=1:
                        h.append(encodeFourCode(x-5,y-3,'l',7))
                if gouhou[x][y-1]<=1:
                    if gouhou[x-1][y-1]<=1 and gouhou[x-1][y-2]<=1 and gouhou[x-1][y-3]<=1:
                        h.append(encodeFourCode(x-5,y-5,'l',2))
                    if gouhou[x+1][y]<=1 and gouhou[x+1][y+1]<=1 and gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-3,y-4,'l',6))
                    if gouhou[x+1][y-1]<=1 and gouhou[x+1][y-2]<=1 and gouhou[x+1][y-3]<=1:
                        h.append(encodeFourCode(x-3,y-5,'l',3))
                    if gouhou[x-1][y]<=1 and gouhou[x-1][y+1]<=1 and gouhou[x-1][y+2]<=1:
                        h.append(encodeFourCode(x-5,y-4,'l',7))
    #print(h)
    return h

def Mpie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x+1][y]<=1 and gouhou[x][y-1]<=1 and gouhou[x+1][y-1]<=1:
                    if gouhou[x][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-5,'m',2))
                    if gouhou[x+2][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-5,'m',4))
                    if gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'m',6))
                    if gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'m',1))
                    if gouhou[x+1][y-2]<=1:
                        h.append(encodeFourCode(x-3,y-5,'m',3))
                    if gouhou[x+2][y]<=1:
                        h.append(encodeFourCode(x-3,y-4,'m',5))
                if gouhou[x+1][y]<=1 and gouhou[x][y+1]<=1 and gouhou[x+1][y+1]<=1:
                    if gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'m',0))
                    if gouhou[x+2][y]<=1:
                        h.append(encodeFourCode(x-3,y-4,'m',4))
                    if gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-3,y-3,'m',6))
                    if gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'m',3))
                    if gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-3,'m',5))
                    if gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'m',7))
                if gouhou[x][y-1]<=1 and gouhou[x-1][y]<=1 and gouhou[x-1][y-1]<=1:
                    if gouhou[x-2][y]<=1:
                        h.append(encodeFourCode(x-5,y-4,'m',0))
                    if gouhou[x-1][y-2]<=1:
                        h.append(encodeFourCode(x-5,y-5,'m',2))
                    if gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'m',4))
                    if gouhou[x-2][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-5,'m',1))
                    if gouhou[x][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-5,'m',3))
                    if gouhou[x][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'m',7))
                if gouhou[x-1][y]<=1 and gouhou[x][y+1]<=1 and gouhou[x-1][y+1]<=1:
                    if gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-3,'m',0))
                    if gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'m',2))
                    if gouhou[x][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'m',6))
                    if gouhou[x-2][y]<=1:
                        h.append(encodeFourCode(x-5,y-4,'m',1))
                    if gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'m',5))
                    if gouhou[x-1][y+2]<=1:
                        h.append(encodeFourCode(x-5,y-3,'m',7))
                if gouhou[x+1][y]<=1 and gouhou[x+2][y]<=1:
                    if gouhou[x+1][y-1]<=1 and gouhou[x+2][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'m',0))
                    if gouhou[x+1][y+1]<=1 and gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'m',1))
                if gouhou[x-1][y]<=1 and gouhou[x-2][y]<=1:
                    if gouhou[x-1][y+1]<=1 and gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'m',4))
                    if gouhou[x-1][y-1]<=1 and gouhou[x-2][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'m',5))
                if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1:
                    if gouhou[x+1][y+1]<=1 and gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'m',2))
                    if gouhou[x-1][y+1]<=1 and gouhou[x-1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'m',3))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1:
                    if gouhou[x-1][y-1]<=1 and gouhou[x-1][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-5,'m',6))
                    if gouhou[x+1][y-1]<=1 and gouhou[x+1][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-5,'m',7))
    #print(h)
    return h

def Npie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x+2][y]<=1:
                    if gouhou[x][y+1]<=1 and gouhou[x+1][y+1]<=1 and gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-3,'n',0))
                    if gouhou[x][y-1]<=1 and gouhou[x+1][y-1]<=1 and gouhou[x+2][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-5,'n',4))
                if gouhou[x+1][y]<=1 and gouhou[x+2][y]<=1:
                    if gouhou[x][y-1]<=1 and gouhou[x+2][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'n',0))
                    if gouhou[x][y+1]<=1 and gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'n',4))
                if gouhou[x-1][y]<=1 and gouhou[x-2][y]<=1:
                    if gouhou[x][y-1]<=1 and gouhou[x-2][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'n',0))
                    if gouhou[x][y+1]<=1 and gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'n',4))
                if gouhou[x-2][y]<=1:
                    if gouhou[x][y+1]<=1 and gouhou[x-1][y+1]<=1 and gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-3,'n',0))
                    if gouhou[x][y-1]<=1 and gouhou[x-1][y-1]<=1 and gouhou[x-2][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-5,'n',4))
                if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1:
                    if gouhou[x+1][y]<=1 and gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'n',2))
                    if gouhou[x-1][y]<=1 and gouhou[x-1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'n',6))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1:
                    if gouhou[x+1][y]<=1 and gouhou[x+1][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-5,'n',2))
                    if gouhou[x-1][y]<=1 and gouhou[x-1][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-5,'n',6))
                if gouhou[x][y+2]<=1:
                    if gouhou[x-1][y]<=1 and gouhou[x-1][y+1]<=1 and gouhou[x-1][y+2]<=1:
                        h.append(encodeFourCode(x-5,y-3,'n',2))
                    if gouhou[x+1][y]<=1 and gouhou[x+1][y+1]<=1 and gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-3,y-3,'n',6))
                if gouhou[x][y-2]<=1:
                    if gouhou[x-1][y]<=1 and gouhou[x-1][y-1]<=1 and gouhou[x-1][y-2]<=1:
                        h.append(encodeFourCode(x-5,y-5,'n',2))
                    if gouhou[x+1][y]<=1 and gouhou[x+1][y-1]<=1 and gouhou[x+1][y-2]<=1:
                        h.append(encodeFourCode(x-3,y-5,'n',6))
    #print(h)
    return h

def Opie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x+1][y]<=1 and gouhou[x+2][y]<=1 and gouhou[x+3][y]<=1:
                    if gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'o',0))
                    if gouhou[x+2][y-1]<=1:
                        h.append(encodeFourCode(x-2,y-4,'o',4))
                    if gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'o',1))
                    if gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-2,y-4,'o',5))
                if gouhou[x][y+1]<=1:
                    if gouhou[x+1][y+1]<=1 and gouhou[x-1][y+1]<=1 and gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'o',4))
                    if gouhou[x+1][y+1]<=1 and gouhou[x+2][y+1]<=1 and gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'o',1))
                if gouhou[x][y-1]<=1:
                    if gouhou[x-1][y-1]<=1 and gouhou[x+1][y-1]<=1 and gouhou[x+2][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'o',0))
                    if gouhou[x-1][y-1]<=1 and gouhou[x-2][y-1]<=1 and gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'o',5))
                if gouhou[x-1][y]<=1 and gouhou[x-2][y]<=1 and gouhou[x-3][y]<=1:
                    if gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-6,y-4,'o',0))
                    if gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'o',4))
                    if gouhou[x-2][y-1]<=1:
                        h.append(encodeFourCode(x-6,y-4,'o',1))
                    if gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'o',5))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1 and gouhou[x][y-3]<=1:
                    if gouhou[x-1][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-6,'o',2))
                    if gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'o',6))
                    if gouhou[x+1][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-6,'o',3))
                    if gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'o',7))
                if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1 and gouhou[x][y+3]<=1:
                    if gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'o',2))
                    if gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-2,'o',6))
                    if gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'o',3))
                    if gouhou[x-1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-2,'o',7))
                if gouhou[x-1][y]<=1:
                    if gouhou[x-1][y+1]<=1 and gouhou[x-1][y-1]<=1 and gouhou[x-1][y-2]<=1:
                        h.append(encodeFourCode(x-5,y-4,'o',6))
                    if gouhou[x-1][y+1]<=1 and gouhou[x-1][y+2]<-1 and gouhou[x-1][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'o',3))
                if gouhou[x+1][y]<=1:
                    if gouhou[x+1][y+1]<=1 and gouhou[x+1][y+2]<=1 and gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'o',2))
                    if gouhou[x+1][y+1]<=1 and gouhou[x+1][y-1]<=1 and gouhou[x+1][y-2]<=1:
                        h.append(encodeFourCode(x-3,y-4,'o',7))
    #print(h)
    return h

def Ppie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1:
                    if gouhou[x-1][y+1]<=1 and gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-3,'p',0))
                    if gouhou[x-1][y+2]<=1 and gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'p',2))
                    if gouhou[x+1][y+1]<=1 and gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-3,'p',4))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1:
                    if gouhou[x-1][y-1]<=1 and gouhou[x-2][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-5,'p',0))
                    if gouhou[x+1][y-1]<=1 and gouhou[x+2][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-5,'p',4))
                    if gouhou[x+1][y-2]<=1 and gouhou[x-1][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-5,'p',6))
                if gouhou[x-1][y]<=1 and gouhou[x-2][y]<=1:
                    if gouhou[x-1][y-1]<=1 and gouhou[x-1][y-2]<=1:
                        h.append(encodeFourCode(x-5,y-5,'p',2))
                    if gouhou[x-2][y-1]<=1 and gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'p',4))
                    if gouhou[x-1][y+1]<=1 and gouhou[x-1][y+2]<=1:
                        h.append(encodeFourCode(x-5,y-3,'p',6))
                if gouhou[x+1][y]<=1 and gouhou[x+2][y]<=1:
                    if gouhou[x+2][y-1]<=1 and gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'p',0))
                    if gouhou[x+1][y-1]<=1 and gouhou[x+1][y-2]<=1:
                        h.append(encodeFourCode(x-3,y-5,'p',2))
                    if gouhou[x+1][y+1]<=1 and gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-3,y-3,'p',6))
    #print(h)
    return h

def Qpie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x-1][y]<=1 and gouhou[x-2][y]<=1:
                    if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-4,'q',0))
                    if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-4,'q',2))
                    if gouhou[x-2][y-1]<=1 and gouhou[x-2][y-2]<=1:
                        h.append(encodeFourCode(x-6,y-4,'q',4))
                    if gouhou[x-2][y+1]<=1 and gouhou[x-2][y+2]<=1:
                        h.append(encodeFourCode(x-6,y-4,'q',6))
                if gouhou[x+1][y]<=1 and gouhou[x+2][y]<=1:
                    if gouhou[x+2][y+1]<=1 and gouhou[x+2][y+2]<=1:
                        h.append(encodeFourCode(x-2,y-4,'q',0))
                    if gouhou[x+2][y-1]<=1 and gouhou[x+2][y-2]<=1:
                        h.append(encodeFourCode(x-2,y-4,'q',2))
                    if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-4,'q',4))
                    if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-4,'q',6))
                if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1:
                    if gouhou[x-1][y+2]<=1 and gouhou[x-2][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-2,'q',2))
                    if gouhou[x+1][y+1]<=1 and gouhou[x+2][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-2,'q',4))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1:
                    if gouhou[x-1][y-2]<=1 and gouhou[x-2][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-6,'q',0))
                    if gouhou[x+1][y-2]<=1 and gouhou[x+2][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-6,'q',6))
    #print(h)
    return h

def Rpie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x][y+1]<=1 and gouhou[x+1][y+1]<=1 and gouhou[x+1][y+2]<=1 and gouhou[x+2][y+2]<=1:
                    h.append(encodeFourCode(x-3,y-3,'r',0))
                if gouhou[x][y-1]<=1 and gouhou[x+1][y]<=1 and gouhou[x+1][y+1]<=1 and gouhou[x+2][y+1]<=1:
                    h.append(encodeFourCode(x-3,y-4,'r',0))
                if gouhou[x-1][y-2]<=1 and gouhou[x-1][y-1]<=1 and gouhou[x][y-1]<=1 and gouhou[x+1][y]<=1:
                    h.append(encodeFourCode(x-4,y-5,'r',0))
                if gouhou[x-1][y-1]<=1 and gouhou[x-1][y]<=1 and gouhou[x][y+1]<=1 and gouhou[x+1][y+1]<=1:
                    h.append(encodeFourCode(x-4,y-4,'r',0))
                if gouhou[x-2][y-2]<=1 and gouhou[x-2][y-1]<=1 and gouhou[x-1][y-1]<=1 and gouhou[x-1][y]<=1:
                    h.append(encodeFourCode(x-5,y-5,'r',0))
                if gouhou[x+1][y-1]<=1 and gouhou[x][y-1]<=1 and gouhou[x-1][y]<=1 and gouhou[x-1][y+1]<=1:
                    h.append(encodeFourCode(x-4,y-4,'r',2))
                if gouhou[x][y+1]<=1 and gouhou[x+1][y]<=1 and gouhou[x+1][y-1]<=1 and gouhou[x+2][y-1]<=1:
                    h.append(encodeFourCode(x-5,y-4,'r',2))
                if gouhou[x][y-1]<=1 and gouhou[x+1][y-1]<=1 and gouhou[x+1][y-2]<=1 and gouhou[x+2][y-2]<=1:
                    h.append(encodeFourCode(x-3,y-5,'r',2))
                if gouhou[x-1][y]<=1 and gouhou[x-1][y+1]<=1 and gouhou[x-2][y+1]<=1 and gouhou[x-2][y+2]<=1:
                    h.append(encodeFourCode(x-5,y-3,'r',2))
                if gouhou[x+1][y]<=1 and gouhou[x][y+1]<=1 and gouhou[x-1][y+1]<=1 and gouhou[x-1][y+2]<=1:
                    h.append(encodeFourCode(x-4,y-3,'r',2))
                if gouhou[x-1][y-1]<=1 and gouhou[x][y-1]<=1 and gouhou[x+1][y]<=1 and gouhou[x+1][y+1]<=1:
                    h.append(encodeFourCode(x-4,y-4,'r',4))
                if gouhou[x-1][y]<=1 and gouhou[x][y+1]<=1 and gouhou[x+1][y+1]<=1 and gouhou[x+1][y+2]<=1:
                    h.append(encodeFourCode(x-4,y-3,'r',4))
                if gouhou[x][y+1]<=1 and gouhou[x-1][y]<=1 and gouhou[x-1][y-1]<=1 and gouhou[x-2][y-1]<=1:
                    h.append(encodeFourCode(x-5,y-4,'r',4))
                if gouhou[x+1][y]<=1 and gouhou[x+1][y+1]<=1 and gouhou[x+2][y+1]<=1 and gouhou[x+2][y+2]<=1:
                    h.append(encodeFourCode(x-3,y-3,'r',4))
                if gouhou[x][y-1]<=1 and gouhou[x-1][y-1]<=1 and gouhou[x-1][y-2]<=1 and gouhou[x-2][y-2]<=1:
                    h.append(encodeFourCode(x-5,y-5,'r',4))
                if gouhou[x][y+1]<=1 and gouhou[x-1][y+1]<=1 and gouhou[x-1][y+2]<=1 and gouhou[x-2][y+2]<=1:
                    h.append(encodeFourCode(x-5,y-3,'r',6))
                if gouhou[x][y-1]<=1 and gouhou[x-1][y]<=1 and gouhou[x-1][y+1]<=1 and gouhou[x-2][y+1]<=1:
                    h.append(encodeFourCode(x-5,y-4,'r',6))
                if gouhou[x+1][y-1]<=1 and gouhou[x+1][y]<=1 and gouhou[x][y+1]<=1 and gouhou[x-1][y+1]<=1:
                    h.append(encodeFourCode(x-4,y-4,'r',6))
                if gouhou[x+1][y-2]<=1 and gouhou[x+1][y-1]<=1 and gouhou[x][y-1]<=1 and gouhou[x-1][y]<=1:
                    h.append(encodeFourCode(x-4,y-5,'r',6))
                if gouhou[x+1][y]<=1 and gouhou[x+1][y-1]<=1 and gouhou[x+2][y-1]<=1 and gouhou[x+2][y-2]<=1:
                    h.append(encodeFourCode(x-3,y-5,'r',6))
    #print(h)
    return h

def Spie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x+1][y]<=1:
                    if gouhou[x+1][y+1]<=1 and gouhou[x+1][y+2]<=1 and gouhou[x+2][y+2]<=1:
                        h.append(encodeFourCode(x-3,y-3,'s',0))
                    if gouhou[x+1][y-1]<=1 and gouhou[x+1][y-2]<=1 and gouhou[x+2][y-2]<=1:
                        h.append(encodeFourCode(x-3,y-5,'s',1))
                if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1:
                    if gouhou[x-1][y]<=1 and gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'s',0))
                    if gouhou[x+1][y]<=1 and gouhou[x-1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'s',1))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1:
                    if gouhou[x+1][y]<=1 and gouhou[x-1][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-5,'s',0))
                    if gouhou[x+1][y-2]<=1 and gouhou[x-1][y]<=1:
                        h.append(encodeFourCode(x-4,y-5,'s',1))
                if gouhou[x-1][y]<=1:
                    if gouhou[x-1][y-1]<=1 and gouhou[x-1][y-2]<=1 and gouhou[x-2][y-2]<=1:
                        h.append(encodeFourCode(x-5,y-5,'s',0))
                    if gouhou[x-1][y+1]<=1 and gouhou[x-1][y+2]<=1 and gouhou[x-2][y+2]<=1:
                        h.append(encodeFourCode(x-5,y-3,'s',1))
                if gouhou[x][y+1]<=1:
                    if gouhou[x+1][y+1]<=1 and gouhou[x+2][y+1]<=1 and gouhou[x+2][y+2]<=1:
                        h.append(encodeFourCode(x-3,y-3,'s',3))
                    if gouhou[x-1][y+1]<=1 and gouhou[x-2][y+1]<=1 and gouhou[x-2][y+2]<=1:
                        h.append(encodeFourCode(x-5,y-3,'s',2))
                if gouhou[x+1][y]<=1 and gouhou[x+2][y]<=1:
                    if gouhou[x][y-1]<=1 and gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'s',3))
                    if gouhou[x][y+1]<=1 and gouhou[x+2][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'s',2))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1:
                    if gouhou[x][y+1]<=1 and gouhou[x-2][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'s',3))
                    if gouhou[x][y-1]<=1 and gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'s',2))
                if gouhou[x][y-1]<=1:
                    if gouhou[x-1][y-1]<=1 and gouhou[x-2][y-1]<=1 and gouhou[x-2][y-2]<=1:
                        h.append(encodeFourCode(x-5,y-5,'s',3))
                    if gouhou[x+1][y-1]<=1 and gouhou[x+2][y-1]<=1 and gouhou[x+2][y-2]<=1:
                        h.append(encodeFourCode(x-3,y-5,'s',2))
    #print(h)
    return h

def Tpie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x+1][y]<=1:
                    if gouhou[x+1][y+1]<=1 and gouhou[x+2][y+1]<=1 and gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-3,y-3,'t',0))
                    if gouhou[x+1][y-1]<=1 and gouhou[x+1][y+1]<=1 and gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'t',4))
                    if gouhou[x+1][y-1]<=1 and gouhou[x+2][y-1]<=1 and gouhou[x+1][y-2]<=1:
                        h.append(encodeFourCode(x-3,y-5,'t',1))
                    if gouhou[x+1][y+1]<=1 and gouhou[x+2][y-1]<=1 and gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'t',5))
                if gouhou[x][y+1]<=1 and gouhou[x][y+2]<=1:
                    if gouhou[x-1][y]<=1 and gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'t',0))
                    if gouhou[x-1][y+1]<=1 and gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'t',4))
                    if gouhou[x-1][y+2]<=1 and gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-4,y-3,'t',1))
                    if gouhou[x-1][y+1]<=1 and gouhou[x+1][y]<=1:
                        h.append(encodeFourCode(x-4,y-3,'t',5))
                if gouhou[x-1][y]<=1:
                    if gouhou[x-1][y+1]<=1 and gouhou[x-1][y-1]<=1 and gouhou[x-2][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'t',0))
                    if gouhou[x-1][y-1]<=1 and gouhou[x-2][y-1]<=1 and gouhou[x-1][y-2]<=1:
                        h.append(encodeFourCode(x-5,y-5,'t',4))
                    if gouhou[x-1][y-1]<=1 and gouhou[x-1][y+1]<=1 and gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'t',1))
                    if gouhou[x-1][y+1]<=1 and gouhou[x-2][y+1]<=1 and gouhou[x-1][y+2]<=1:
                        h.append(encodeFourCode(x-5,y-3,'t',5))
                if gouhou[x][y-1]<=1 and gouhou[x][y-2]<=1:
                    if gouhou[x-1][y-2]<=1 and gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'t',0))
                    if gouhou[x-1][y-1]<=1 and gouhou[x+1][y]<=1:
                        h.append(encodeFourCode(x-4,y-5,'t',4))
                    if gouhou[x-1][y]<=1 and gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'t',1))
                    if gouhou[x-1][y-1]<=1 and gouhou[x+1][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-5,'t',5))
                if gouhou[x][y+1]<=1:
                    if gouhou[x-1][y+1]<=1 and gouhou[x-1][y+2]<=1 and gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-3,'t',2))
                    if gouhou[x-1][y+1]<=1 and gouhou[x+1][y+1]<=1 and gouhou[x-1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'t',6))
                    if gouhou[x+1][y+1]<=1 and gouhou[x+1][y+2]<=1 and gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-3,'t',3))
                    if gouhou[x-1][y+1]<=1 and gouhou[x+1][y+1]<=1 and gouhou[x+1][y+2]<=1:
                        h.append(encodeFourCode(x-4,y-3,'t',7))
                if gouhou[x-1][y]<=1 and gouhou[x-2][y]<=1:
                    if gouhou[x][y-1]<=1 and gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'t',2))
                    if gouhou[x-1][y-1]<=1 and gouhou[x-2][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'t',6))
                    if gouhou[x-2][y-1]<=1 and gouhou[x-1][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'t',3))
                    if gouhou[x-1][y-1]<=1 and gouhou[x][y+1]<=1:
                        h.append(encodeFourCode(x-5,y-4,'t',7))
                if gouhou[x][y-1]<=1:
                    if gouhou[x-1][y-1]<=1 and gouhou[x+1][y-1]<=1 and gouhou[x+1][y-2]<=1:
                        h.append(encodeFourCode(x-4,y-5,'t',2))
                    if gouhou[x+1][y-1]<=1 and gouhou[x+1][y-2]<=1 and gouhou[x+2][y-1]<=1:
                        h.append(encodeFourCode(x-3,y-5,'t',6))
                    if gouhou[x-1][y-1]<=1 and gouhou[x-1][y-2]<=1 and gouhou[x+1][y-1]<=1:
                        h.append(encodeFourCode(x-4,y-5,'t',3))
                    if gouhou[x-1][y-1]<=1 and gouhou[x-1][y-2]<=1 and gouhou[x-2][y-1]<=1:
                        h.append(encodeFourCode(x-5,y-5,'t',7))
                if gouhou[x+1][y]<=1 and gouhou[x+2][y]<=1:
                    if gouhou[x+2][y-1]<=1 and gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'t',2))
                    if gouhou[x+1][y-1]<=1 and gouhou[x][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'t',6))
                    if gouhou[x][y-1]<=1 and gouhou[x+1][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'t',3))
                    if gouhou[x+1][y-1]<=1 and gouhou[x+2][y+1]<=1:
                        h.append(encodeFourCode(x-3,y-4,'t',7))
    #print(h)
    return h

def Upie(gouhou):
    h=[]
    for x in range(4,24):
        for y in range(4,24):
            if gouhou[x][y]==1:
                if gouhou[x-1][y+1]<=1 and gouhou[x][y+1]<=1 and gouhou[x+1][y+1]<=1 and gouhou[x][y+2]<=1:
                    h.append(encodeFourCode(x-4,y-3,'u',0))
                if gouhou[x+1][y-1]<=1 and gouhou[x+1][y]<=1 and gouhou[x+1][y+1]<=1 and gouhou[x+2][y]<=1:
                    h.append(encodeFourCode(x-3,y-4,'u',0))
                if gouhou[x-1][y-1]<=1 and gouhou[x-1][y]<=1 and gouhou[x-1][y+1]<=1 and gouhou[x-2][y]<=1:
                    h.append(encodeFourCode(x-5,y-4,'u',0))
                if gouhou[x-1][y-1]<=1 and gouhou[x][y-1]<=1 and gouhou[x+1][y-1]<=1 and gouhou[x][y-2]<=1:
                    h.append(encodeFourCode(x-4,y-5,'u',0))
    #print(h)
    return h
