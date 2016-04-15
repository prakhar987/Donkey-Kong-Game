from __future__ import print_function
import os
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

class Printer:
     """ CONTROLS PRINT FUNCTIONS 
     """      
     def __init__(self):
      pass
     ##PRINTER######
     def printer(self,a,coins,player_life,score):
        os.system('clear')
        for i in range (31):
           for j in range (80):
                if (a[i][j]!= 0):
                    if(a[i][j]=='X'):  
                     print (bcolors.FAIL + a[i][j] + bcolors.ENDC,end="")
                    elif (a[i][j]=='C'):
                     print (bcolors.WARNING + a[i][j] + bcolors.ENDC,end="")
                    elif (a[i][j]=='P'):
                     print (bcolors.OKGREEN + a[i][j] + bcolors.ENDC,end="")
                    else :
                      print (bcolors.HEADER + a[i][j] + bcolors.ENDC,end="")
                else :
                    print (' ',end="")
           print ('')
        print ('COINS=             ',end="")
        print (coins,end="")
        print(' LIFE=             ',end="")
        print (player_life,end="")
        print( ' Score=             ',end="")
        print(score)
          


#print(bcolors.WARNING + "Warning" + bcolors.ENDC)
  
################################# THIS SPECIAL CLASSS CONTROLS               ##############################################
################################# THE EFFECTS WHEN GAME STARTS              ##############################################
################################# i.e SLOW LOADING OF LADDERS, BLOCKS ETC  ##############################################

class Printer_first:
     def __init__(self):
      pass
     ##PRINTER######
     def printer(self,a,coins,player_life,score,flag):
        os.system('clear')
        for i in range (31):
           for j in range (80):
                if (a[i][j]!= 0):
                    print (a[i][j],end="")
                else :
                    print (' ',end="")
           print ('')
        if flag==1 :
         print (" COINS=    ",end="")
         print (coins,end="")
         print(" LIFE=  ",end="")
         print (player_life,end="")
         print(" Score= ",end="")
         print(score)
         print("!!!! GET READY !!!!!")
         time.sleep(0.8)
         print("GO!!!!!!!!!!!!!!!!!!")
         time.sleep(1.5)  
         os.system('clear')
