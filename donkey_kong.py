
#### THIS IS THE MAIN FILE WHICH CONTROLS THE MOVEMENT ########
 
     ####### THE MODULE handler() IS THE MAIN CONTROLLING PART WHICH CALLS OTHER THINGS ACCORDINGLY #########

           ######## IT ALSO CONTAINS THE MAIN ARRAY WHICH CONTAINS ALL ENTITIES ##############

import time
import os
import pyxhook
import sys
from random import randint




######### THE FILES IMPORTED HAVE THE CLASSES WHICH DO FOLLOWING----  
  ###########    jumper --- CONTROLS JUMP MOVEMENTS ###############
   ###########   printer ---- PRINTS THE ARRAY , SCORE, LIFE & COINS ###############
    ###########  board ----- CONSTRUCTS LADDERS , BOUNDRIES , BROKEN LADDERS ETC ##############
     ########### fireball ---- SPAWNS AND MOVES FIREBALLS .... HAS IMPORTANT MODULE check_collision() #################
      ########## person ------ HAS INFO AND MOVEMENTS OF DONKEY #####################################




from jumper import Jumper
from printer import Printer
from fireball import Fireball  
from board import Board
from board import Board_first
from person import Donkey

################ CREATING OBJECTS OF RELEVANT CLASSES  ############################
p = Printer()
fb = Fireball()
b=Board()
b1=Board_first()
jp=Jumper()
d=Donkey(4,3)

##################### VARIOUS DATA STRUCTURES USED IN THE PROGRAM ##################

score=0                 ##### SCORE
key=0                   ####VALUE OF CURRENT KEY PRESS
player_pos_i=29         ####PLAYER POSITION
player_pos_j=1          ####PLAYER POSITION
a=[[0 for x in range(80)] for x in range (31)] ###### THE MAIN ARRAY
last_key=0              ####VALUE OF LAST KEY
last_element=0          ####VALUE OF LAST ARRAY ELEMENT
coins=0                 #### COINS COLLECTED 
f=[4,3,-15,-16,-45,-46,-75,-76,-90,-91,-100,-101,'X','X','X','X'] ### FIREBALL POSITIONS ('X' indicates dormant fireballs)
player_life=3           ###### LIFES THAT PLAYER HAS
remedy=[0,0,0,0,0,0]    
exit=[0,0]


###INPUT HANDLER##


def kbevent( event ):
    global key
    key=event.Ascii

## KEYBOARD HANDLER ##
hookman = pyxhook.HookManager()
hookman.KeyDown = kbevent
hookman.HookKeyboard()
hookman.start()


      ################################## MAIN HANDLER ######################################################   
def handler():
     os.system('clear')
     print('\v\v\v\v\v\v\v\v\t\t\t\t LEVEL 1  LIFE 3 ')
     time.sleep(2)
     b1.structure(a,coins,player_life,score)
     #b.structure(a)
     os.system('stty -echo')


     ##################### main loop ##############


     while True :
           global key , player_pos_i , player_pos_j , last_key , last_element ,coins , score,a,exit,player_life
           
           if key==0:             ###  NO INPUT #####
             remedy[1]=score ;remedy[2]=player_pos_i;remedy[3]=player_pos_j; remedy[0]=player_life
             remedy[4]=exit[1];remedy[5]=exit[0]             
             fb.fire(a,f,coins,player_life,score,last_element,player_pos_i,player_pos_j,remedy)
             score=remedy[1] ;player_pos_i=remedy[2];player_pos_j=remedy[3];player_life=remedy[0]
             exit[1]=remedy[4];exit[0]=remedy[5]
                            
             if randint(1,3)==2:
              d.move_donkey(a)
             continue
           if exit[1]==1:
                last_element=0
                exit[1]=0
           if player_life==0:         ### WHEN LIFES =0 
                    os.system('clear')
                    print '\v\v\v\v\v\t\t\t SCORE ' , score
                    time.sleep(2)
                    key=113 
           if last_element=='H' and key ==115:      ########### STAIR CONTROL
                      key=0
                      continue  
           if key==100 and a[player_pos_i + 1][player_pos_j + 1]==0: ### FALL WHEN STRUCTURE ENDS ##3
             
               a[player_pos_i][player_pos_j]=last_element
               player_pos_i=player_pos_i +5
               player_pos_j=player_pos_j +1
               a[player_pos_i][player_pos_j]='P'
               last_element=0
                
           if key==97 and a[player_pos_i + 1][player_pos_j - 1]==0:  ### FALL WHEN STRUCTURE ENDS (BACKWARDS) ##3
         
               a[player_pos_i][player_pos_j]=last_element
               player_pos_i=player_pos_i +5
               player_pos_j=player_pos_j -1
               a[player_pos_i][player_pos_j]='P'
               last_element=0
               
           if key==100:                                           ### MOVE FORWARD ###3
                                                       
             if a[player_pos_i][player_pos_j+1]=='X':
                 key=0 
                 continue
             a[player_pos_i][player_pos_j]=last_element
             last_element=a[player_pos_i][player_pos_j + 1]
             a[player_pos_i][player_pos_j + 1]='P'
             player_pos_j = player_pos_j +1
             key=0
             last_key=100
             ##
             if last_element=='C':
              coins=coins+1
              score=score+5
              last_element=0
           if key==97:                                                     ### MOVE BACK ####
                                                 
             if a[player_pos_i][player_pos_j-1]=='X':
                  key=0
                  continue
             a[player_pos_i][player_pos_j]=last_element
             last_element=a[player_pos_i][player_pos_j - 1]
             a[player_pos_i][player_pos_j - 1]='P'
             player_pos_j = player_pos_j -1
             key=0
             last_key=97
             ##
             if last_element=='C':
              coins=coins+1
              score=score+5
              last_element=0 


           if key==32 and last_key==100 :
                                        ## JUMP FORWARD ##
               player_pos=[0,0]
               player_pos[0]=player_pos_i
               player_pos[1]=player_pos_j
               xyz=last_element
               last_element=jp.jumper(a,3,player_pos,coins,player_life,score,xyz,f)
               key=last_key
               player_pos_i=player_pos[0]
               player_pos_j=player_pos[1]
               
           if key==32 and last_key==97 :
                                          ## JUMP BACKWARD ##
               player_pos=[0,0]
               player_pos[0]=player_pos_i
               player_pos[1]=player_pos_j
               xyz=last_element
               last_element=jp.jumper(a,-3,player_pos,coins,player_life,score,xyz,f)
               key=last_key
               player_pos_i=player_pos[0]
               player_pos_j=player_pos[1]
               
           if key==119 and last_element=='H' :  ###  CLIMB STAIRS
            
               if (player_pos_i == 14 and player_pos_j == 23) or (player_pos_i == 24 and player_pos_j == 32): 
                           key=0
                           continue
               a[player_pos_i][player_pos_j]=last_element
               last_element=a[player_pos_i-1][player_pos_j]
               a[player_pos_i-1][player_pos_j]='P'
               player_pos_i=player_pos_i - 1
               key=0
               
           if  key==115 and  a[player_pos_i+1][player_pos_j]=='H' :  ###  CLIMB DOWN STAIRS
          
                if (player_pos_i == 9 and player_pos_j == 23) or (player_pos_i == 19 and player_pos_j == 32): 
                           key=0
                           continue
                a[player_pos_i][player_pos_j]=last_element
                player_pos_i=player_pos_i+5
                last_element=a[player_pos_i][player_pos_j]
                a[player_pos_i][player_pos_j]='P'
                key=0
              
           if key ==119 or key==115:
                       key=0   
              

           if key==113 or exit[0]==1:                                            ###### QUIT ##
               hookman.cancel() 
               os.system('stty echo')
               break
           



def get_position():
          global player_pos_i , player_pos_j
          position[0]=player_pos_i
          postition[1]=player_pos_j
          return position 



if __name__=="__main__" :
       handler()
