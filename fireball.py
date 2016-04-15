from printer import Printer
from random import randint
import time                     #### IMPORTING LIBRARIES ######
import os

class Fireball:
 """ THIS CLASS CONTROLS THE MOVEMENT OF FIREBALLLS
           IT IS REPEATEDLY CALLED TO SPWAN NEW FIREBALLS AND
             CONTROL MOVEMENT OF PRE-EXISTING ONES. 
 """
 last_pos=[0,0,0,0,0,0,0,0]              ########## REMEMBERS THE ELEMENT MASKED BY FIREBALLS
 lor=[1,1,1,1,1,1,1,1]                   ### CONTROLS left or right MOVEMENT OF FIREBALL


 def __init__(self):

         pass

 def fire(self,a,f,coins,player_life,score,last_element,player_pos_i,player_pos_j,remedy) :
      p=Printer()
      i=0
      value=0
      while(i<16):          ############# MAIN LOOP THAT CONTROLS FIREBALLS ##################
       if f[i]=='X':
           break
       if f[i]<4 and f[i+1]<3 :
           f[i]=f[i]+1  
           f[i+1]+=1 
           i = i+2
           continue
       if f[i]==4 and f[i+1]==3:
          a[f[i]][f[i+1]]='O'
        
    ################ moving fireballs forward ###############################

       if a[f[i]+1][f[i+1]+1]=='X' or a[f[i]+1][f[i+1]-1]=='X' :
           value=self.check_collision(a,f,player_pos_i,player_pos_j,player_life,score,remedy)
           if value==1 :
                   return 
           a[f[i]][f[i+1]]=Fireball.last_pos[i/2]
           if Fireball.last_pos[i/2]=='P':## to remove P after collision
               a[f[i]][f[i+1]]=last_element ##
           f[i+1]=f[i+1]+Fireball.lor[i/2]
           Fireball.last_pos[i/2]=a[f[i]][f[i+1]]
           

             ###MARK ########
           if Fireball.last_pos[i/2]=='O':
               Fireball.last_pos[i/2]=0
           a[f[i]][f[i+1]]='O'

       if a[f[i]][f[i+1]+1]=='X' :  ################## collision with wall
           Fireball.lor[i/2]=-1
       if a[f[i]][f[i+1]-1]=='X' :  ################### collision with wall
           Fireball.lor[i/2]=1
       if a[f[i]+1][f[i+1]+1]=='H' and randint(0,2) :  ########################### fall from stairs
          
              a[f[i]+1][f[i+1]+1]='O'
              a[f[i]][f[i+1]]=Fireball.last_pos[i/2]
              Fireball.last_pos[i/2]='H'
              p.printer(a,coins,player_life,score)
              time.sleep(0.05)
              a[f[i]+5][f[i+1]+1]='O'
              a[f[i]+1][f[i+1]+1]='H'
              f[i]=f[i]+5
              f[i+1]=f[i+1]+1
              if randint(1,9)>=4:
                Fireball.lor[i/2]=1
              else :
                Fireball.lor[i/2]=-1
       if a[f[i]+1][f[i+1]+1]==0:      ############################### fall from empty structure
              a[f[i]+1][f[i+1]+1]='O'
              a[f[i]][f[i+1]]=Fireball.last_pos[i/2]
              Fireball.last_pos[i/2]=0
              p.printer(a,coins,player_life,score)
              time.sleep(0.05)
              a[f[i]+5][f[i+1]+1]='O'
              a[f[i]+1][f[i+1]+1]=0
              f[i]=f[i]+5
              f[i+1]=f[i+1]+1

              if randint(1,9)>=4:             
                Fireball.lor[i/2]=1
              else :
                Fireball.lor[i/2]=-1         
       i=i+2
      p.printer(a,coins,player_life,score) 
      time.sleep(0.1)
     
 
    #################################### IMPORTANT FUNCTION THAT CHECKS PLAYER POSITION AFTER EVERY MOVE ############
 
 def check_collision(self,a,f,player_pos_i,player_pos_j,player_life,score,remedy) :
     i=0
     flag=0
     p=Printer()
     while(i<12):
      
      if player_pos_i ==f[i] and player_pos_j ==f[i+1]:
       remedy[0]=remedy[0]-1
       remedy[1]=remedy[1]-25
       a[player_pos_i][player_pos_j]=0
       remedy[2]=29
       remedy[3]=1
       a[29][1]='P'
       flag=flag+1
       remedy[4]=1
      if f[i]==29 and f[i+1]==1:
          f[i]=4
          f[i+1]=3
          a[29][1]=0
      i=i+2
     if player_pos_i==2 and player_pos_j==26 :
         os.system('clear')
         print ("\v\v\v\v\v\v\t\t\t\t\t LEVEL 2")
         time.sleep(2)
         remedy[1]=remedy[1]+50
         f[12]=-200  ; f[13]=-201  ;f[14]= -300 ;f[15]=-301
         remedy[2]=29
         remedy[3]=1
         a[2][26]='H'
         a[29][1]='P'
         #p.printer(a,coins,player_life,score)
     return flag  
 
       
         
       


