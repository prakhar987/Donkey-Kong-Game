from printer import Printer
import time
class Jumper:
 """  THE CLASS TAKES CONTROL OF JUMP MOVEMENTS 
            VARIABLE  z PASSED BY handler() TELLS DIRECTION OF JUMP. 
 """
 
 def __init__(self) :
   pass

 def jumper(self,a,z,player_pos,coins,player_life,score,last_element,f):
      p = Printer()
      pre=0
      i=player_pos[0]
      j=player_pos[1]

      a[i][j]=last_element
      p.printer(a,coins,player_life,score)           ########### JUMP IS ANIMATED USING APPROPRIATE DELAYS ###############
      time.sleep(0.09)
      pre=a[i-2][j]
      a[i-2][j]='P'
      p.printer(a,coins,player_life,score)
      time.sleep(0.07)
      a[i-2][j]=pre
      p.printer(a,coins,player_life,score)
      time.sleep(0.09)
      pre=a[i-2][j+z]
      a[i-2][j+z]='P'
      p.printer(a,coins,player_life,score)
      time.sleep(0.07)
      a[i-2][j+z]=pre
      p.printer(a,coins,player_life,score)
      time.sleep(0.09)
      pre=a[i][j+z]
      a[i][j+z]='P'
      p.printer(a,coins,player_life,score)
      player_pos[1]=j+z
      return pre
      
     


