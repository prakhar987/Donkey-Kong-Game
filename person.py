class Person :
      pos_i=0
      pos_j=0
      def __init__(self):
        pass





class Donkey(Person) :
     
     def __init__(self,donkey_pos_i,donkey_pos_j):
           Person.pos_i=donkey_pos_i
           Person.pos_j=donkey_pos_j
       
     def move_donkey(self,a):
        a[Person.pos_i][Person.pos_j]=0
        Person.pos_j=Person.pos_j %8 + 1
        a[Person.pos_i][Person.pos_j]='D'

