from printer import Printer
from random import randint
import time
class Board:
 """ THIS CLASS SPAWNS THE ENTIRE BOARD WHEN CALLED
          LADDERS , BOUNDRIES , STRUCTURES, PRINCESS ETC ARE CREATED 
 """
 def __init__(self):
  pass

 def structure(self,a) :
    a[29][1]='P' #Spawn P
    i=5
    #X in middle
    while (i<30):
       for j in range (80):
             if (((i/5)%2)==1 and j>55) or (((i/5)%2)==0 and j<20):
                 continue
             a[i][j]='X'    
       i=i+5
   
    #X of Boundry
    for i in range (31):
      for j in range (80):
        if (i==0 or j==0 or i==30 or j==79):
               a[i][j]='X'
    # COIN
    i=5
    while(i<31):
         p=randint(1,78)
         r=0
         while(r<6):
            if a[i][p]=='X':
                a[i-1][p]='C'
            r=r+1
            p=randint(3,77)
         i=i+5
     #princess
    a[2][24]='X'
    a[2][25]='X'
    a[2][26]='X'
    a[2][27]='X'
    a[2][28]='X'
    a[1][26]='Q'
     ###LADDER####
    self.ladder_maker(4,26,a)
    self.ladder_maker(9,50,a)
    self.ladder_maker(14,40,a)
    self.ladder_maker(19,53,a)
    self.ladder_maker(24,22,a)
    self.ladder_maker(29,30,a)
     ###Broken Ladders###
    self.ladder_maker(14,23,a)
    self.ladder_maker(24,32,a)
    a[12][23]=0
    a[13][23]=0
    a[22][32]=0
    a[23][32]=0
 def ladder_maker(self,i,j,a) :
           k=0
           while k<5:
              if i==4 and k>1 :
                    break
              a[i-k][j]='H'
              k=k+1
  
################################# THIS SPECIAL CLASSS CONTROLS               ##############################################
################################# THE EFFECTS WHEN GAME STARTS              ##############################################
################################# i.e SLOW LOADING OF LADDERS, BLOCKS ETC  ##############################################
 
from printer import Printer_first
class Board_first:
 def __init__(self):
  pass

 def structure(self,a,coins,player_life,score) :
    pp=Printer_first()
    i=0

    #X of Boundry
    for i in range (31):
      for j in range (80):
        if (i==0 or j==0 or i==30 or j==79):
               a[i][j]='X'
    pp.printer(a,coins,player_life,score,0)
    time.sleep(0.7)
    i=5
    
    #X in middle
    while (i<30):
       for j in range (80):
             if (((i/5)%2)==1 and j>55) or (((i/5)%2)==0 and j<20):
                 continue
             a[i][j]='X'    
       i=i+5
   
    pp.printer(a,coins,player_life,score,0)
    time.sleep(0.7)
    # COIN
    i=5
    while(i<31):
         p=randint(1,78)
         r=0
         while(r<6):
            if a[i][p]=='X':
                a[i-1][p]='C'
            r=r+1
            p=randint(3,77)
         i=i+5
    pp.printer(a,coins,player_life,score,0)
    time.sleep(0.7)
    a[29][1]='P' #Spawn P
    pp.printer(a,coins,player_life,score,0)
    time.sleep(0.7)
    #princess
    a[2][24]='X'
    a[2][25]='X'
    a[2][26]='X'
    a[2][27]='X'
    a[2][28]='X'
    a[1][26]='Q'
    pp.printer(a,coins,player_life,score,0)
    time.sleep(0.7)
     ###LADDER####
    self.ladder_maker(4,26,a)
    self.ladder_maker(9,50,a)
    self.ladder_maker(14,40,a)
    self.ladder_maker(19,53,a)
    self.ladder_maker(24,22,a)
    self.ladder_maker(29,30,a)
     ###Broken Ladders###
    self.ladder_maker(14,23,a)
    self.ladder_maker(24,32,a)
    a[12][23]=0
    a[13][23]=0
    a[22][32]=0
    a[23][32]=0
    pp.printer(a,coins,player_life,score,0)
    time.sleep(0.7)
    pp.printer(a,coins,player_life,score,1)

 def ladder_maker(self,i,j,a) :
           k=0
           while k<5:
              if i==4 and k>1 :
                    break
              a[i-k][j]='H'
              k=k+1
  


