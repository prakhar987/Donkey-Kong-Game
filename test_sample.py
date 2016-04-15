import pytest
from board import Board
from board import Board_first
from fireball import Fireball
from jumper import Jumper
from person import Donkey
from printer import Printer
class Test_Game():
  """This is the test class"""
  
  def test_coins(self): ## CHECK MINIMUM NO OF COINS IS 20 or not
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    total_coin=0
    for i in range (31):
      for j in range (80):
          if a[i][j]=='C':
            total_coin=total_coin+1
    assert (total_coin>=20)

  def test_coins_in_board_first(self): ## CHECK MINIMUM NO OF COINS IS 20 or not
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board_first()  ## check for Board_first function
    h.structure(a,1,1,1)
    total_coin=0
    for i in range (31):
      for j in range (80):
          if a[i][j]=='C':
            total_coin=total_coin+1
    assert (total_coin>=20)
  def test_stairs(self): ## CHECK randomly stairs elements
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    flag=0
    for i in range (30):
          if a[i][0]!='X':
            flag=flag+1
    assert (flag==0)
  def test_stairs_in_board_first(self): ## CHECK randomly stairs elements
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board_first()
    h.structure(a,1,1,1)
    flag=0
    for i in range (30):
          if a[i][0]!='X':
            flag=flag+1
    assert (flag==0)
  def test_coin_in_air(self): ## CHECK randomly if some coin generates in air
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    flag=0
    i=0
    # check for last level
    for j in range (80):
          if a[23][j]=='C':
            flag=flag+1
    assert (flag==0)

  def test_fireball_collision (self): ## To check how fireballs behave after collision with wall
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    a[9][78]='O'       ## put fireball at last index
    h=Fireball()         
    f=[9,77,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,'X','X','X','X']
    remedy=[1,0,29,1,0,0]  
    h.fire(a,f,1,1,1,0,29,1,remedy) ## this updates the position of fireball
    assert (a[9][78]=='O')

  def test_fireball_on_ladder (self): ## To check how fireballs behave after collision with wall
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    a[24][30]='O'       ## put fireball at head of ladder
    h=Fireball()         
    f=[24,30,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,'X','X','X','X']
    remedy=[1,0,29,1,0,0]  
    h.fire(a,f,1,1,1,0,29,1,remedy) ## call 4 times to ensure fireball descends
    h.fire(a,f,1,1,1,'H',29,1,remedy)
    h.fire(a,f,1,1,1,'H',29,1,remedy)
    assert (a[27][30]=='O')

  def test_fireball_collision_among_self (self): ## To check how fireballs behave after collision with wall
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    h=Fireball()         
    f=[4,9,4,10,-1,-1,-1,-1,-1,-1,-1,-1,'X','X','X','X'] # two fireballs are created
    remedy=[1,0,29,1,0,0]  
    h.fire(a,f,1,1,1,0,29,1,remedy) ## call fire two times
    assert (a[4][10]==0)

  def test_fireball_respawn_at_begining(self): ## To check if fireballs respawn after reaching end
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    h=Fireball()         
    f=[29,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,'X','X','X','X'] # two fireballs are created
    remedy=[1,0,29,1,0,0]  
    h.check_collision(a,f,29,20,1,1,remedy)
    assert (f[0]==4 and f[1]==3)  # check if postion of fireball changes to that of beginning  

  def test_player_boundry_jump_right(self) :  ## checks right jump near boundry
   try: 
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    h=Jumper()
    player_pos=[29,78]
    f=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,'X','X','X','X']
    h.jumper(a,3,player_pos,1,1,1,0,f)
   except IndexError as exc:
        pytest.fail(exc, pytrace=True)
  
  def test_player_boundry_jump_left(self) :  ## checks left jump near boundry
   try: 
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    h=Jumper()
    player_pos=[29,1]
    f=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,'X','X','X','X']
    h.jumper(a,-3,player_pos,1,1,1,0,f)
   except IndexError as exc:
        pytest.fail(exc, pytrace=True)

  def test_jump_from_ladder(self): ## what happens if jump is pressed on a ladder
   try: 
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    h=Jumper()
    player_pos=[28,30]
    f=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,'X','X','X','X']
    h.jumper(a,3,player_pos,1,1,1,0,f)
    assert(a[28][32]!='P')
   except IndexError as exc :
       pytest.fail(exc,pytrace=True) 

  def test_player_respawn(self):    ## check wether player respawns from initail position after dying
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    h=Fireball()
    f=[29,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,'X','X','X','X']
    remedy=[0,0,0,0,0,0]
    h.check_collision(a,f,29,10,1,1,remedy)
    assert (a[29][1]=='P')

  def test_queen_respawn(self):    ## check wether queen respawns after level completition
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    h=Fireball()
    f=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,'X','X','X','X']
    remedy=[0,0,0,0,0,0]
    ##here remedy[5] contains score
    h.check_collision(a,f,2,26,1,1,remedy)
    #we check wether queen respawns or not 
    assert (a[1][26]=='Q')
  def test_check_level_increase(self):  ## what happens when player gets to princess
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    h=Fireball()
    f=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,'X','X','X','X']
    remedy=[0,0,0,0,0,0]
    ##here remedy[5] contains score
    h.check_collision(a,f,2,26,1,1,remedy)
    #we check wether player respwans and score increses by 50 or not
    assert (a[29][1]=='P' and remedy[1]==50)

  def test_jump_through_ladder_left(self):   ## standing besides a ladder and jumping
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    h=Jumper()
    player_pos=[29,29]
    f=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,'X','X','X','X']
    h.jumper(a,3,player_pos,1,1,1,0,f)
    assert(a[29][32]=='P' and a[27][30]=='H')

  def test_jump_through_ladder_right(self):   ## standing besides a ladder and jumping right
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    h=Jumper()
    player_pos=[29,31]
    f=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,'X','X','X','X']
    h.jumper(a,-3,player_pos,1,1,1,0,f)
    assert(a[29][28]=='P' and a[27][30]=='H') 
  def test_donkey_presence(self):            ## check how donkey behaves after 100 moves
    a=[[0 for x in range(80)] for x in range (31)]
    h=Board()
    h.structure(a)
    h=Donkey(4,3)
    flag=0
    for i in range (100): ## move donkey 100 times
      h.move_donkey(a)
    for i in range (80):
         if a[4][i]=='D':
            flag=flag+1
    assert (flag==1) ## flag = 1  means there is 1 donkey , and at level 4

  def test_donkey_number(self):            ## check if number of donkeys increase due to bugs
     a=[[0 for x in range(80)] for x in range (31)]
     h=Board()
     h.structure(a)
     h=Donkey(4,3)
     count=0
     for i in range (100): ## move donkey 100 times
       h.move_donkey(a)
     for i in range (80):
         if a[4][i]=='D':
            count=count+1
     assert (count==1)

  def test_donkey_boundry(self):            ## check if donkey doesnt crosses boundry
     a=[[0 for x in range(80)] for x in range (31)]
     h=Board()
     h.structure(a)
     h=Donkey(4,3)
     count=0
     for i in range (1000): ## move donkey 100 times
      h.move_donkey(a)
     assert (a[4][79]!='D')








