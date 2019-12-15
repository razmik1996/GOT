#!/usr/bin/env python
from util import *
from player import *
from location import *

class Soldier:

    '''Class Soldier
            Hidden members:
                (Player)    __player
                (Location)  __location
                (Direction) __direction
                (int)       __health
                (int)       __atack
                (int)       __defense
                (int)       __cost

         Constructors:
                void __init__(Player, Location, Direction,
                                int, int, int, int)
            Setters:
                void setPlayer(Player)
                void setLocation(Location)
                void setDirection(Direction)
                void setHealth(int)
                void setAttack(int)
                void setDefense(int)
            
            Getters:
                Player      getPlayer()
                Location    getLocation()
                Direction   getDirection()
                int         getHealth()
                int         getAttack()
                int         getDefense()

            Movements:
                void turn(Direction)
                void turnRandom()
                void move()
            
            Controling:
                void reduceHealth(int)      
    '''

    ''' Where does current soldier stand?'''
    __location = Location(0,0)

    ''' Which direction does he face?'''
    __direction = Direction.NORTH

    '''Number from [0..100] where 0 is dead.'''
    __health = 100

    '''How good is this soldier at attacking.'''
    __attack = 0

    '''How good is this soldier at defending.'''
    __defense = 0
    
    '''Solder knows to which player it belongs.'''
    __player = Player("", "", 0, Country.ENGLAND, Color.RED, 1000)

    __cost = 100

    def __init__(self, player, location, direction,\
         health, attack, defense, cost, image_id):
    
         self.__player = player
         self.__location = location
         self.__attack = attack
         self.__defense = defense
         self.__direction = direction
         self.__health = health
         self.__cost = cost
         self.__image_id = image_id
    
    
    def getLocation(self):
        return self.__location

    def getImageId(self):
        return self.__image_id

    def getDirection(self):
        return self.__direction

    def getCost(self):
        return self.__cost

    def getHealth(self):
        return self.__health    
    
    def getAttack(self):
        return self.__attack

    def getDefense(self):
        return self.__defense
    
    def getPlayer(self):
        return self.__player



    def setLocation(self, location):
        self.__location = location

    def setDirection(self, direction):
        self.__direction = direction

    def setImageId(self, image_id):
        self.__image_id = image_id

    def setDirection(self, cost):
        self.__cost = cost

    def setHealth(self, health):
        self.__health = health   
    
    def setAttack(self, attack):
        self.__attack = attack

    def setDefense(self, defense):
        self.__defense = defense
    
    def setPlayer(self, player):
        self.__player = player


    def reduceHealth(self, amount):
        if self.__health < amount:
            self.__health = 0
        else:
            self.__health -= amount



    '''returns True if everything went fine and false otherwise.'''
    def turn(self, new_direction):
        self.__direction = new_direction
    
    '''Turns the soldier in a random direction.'''
    def turnRandom(self):
        self.__direction = getRandomDirection()

    '''Moves soldier in the direction it faces now.'''
    def move(self):
        if self.__direction == Direction.NORTH:
            self.__location.setY(self.__location.getY() - 1)
        elif self.__direction == Direction.SOUTH:
            self.__location.setY(self.__location.getY() + 1)
        elif self.__direction == Direction.EAST:
            self.__location.setX(self.__location.getX() + 1)
        elif self.__direction == Direction.WEST:
            self.__location.setX(self.__location.getX() - 1)
        elif self.__direction == Direction.EASTNORTH:
            self.__location.setY(self.__location.getY() - 1)
            self.__location.setX(self.__location.getX() + 1)
        elif self.__direction == Direction.EASTSOUTH:
            self.__location.setY(self.__location.getY() + 1)
            self.__location.setX(self.__location.getX() + 1)
        elif self.__direction == Direction.WESTNORTH:
            self.__location.setY(self.__location.getY() - 1)
            self.__location.setX(self.__location.getX() - 1)
        elif self.__direction == Direction.WESTSOUTH:
            self.__location.setY(self.__location.getY() + 1)
            self.__location.setX(self.__location.getX() - 1)
        else:
            print "Invalid direction"

    def printSoldier(self):

        p = self.getPlayer()
        p.printPlayer()

        l = self.getLocation()
        print "\nLocation = (",l.getX(), l.getY(),")"
        
        print "Direction =",self.getDirection()        
        print "Health =",self.getHealth()
        print "Attack =",self.getAttack()
        print "Defense =",self.getDefense()
        
    
class Swordsman(Soldier):

    __radius = 2

    def __init__(self, player, location, direction,\
         health, attack, defense, radius, cost, image_id):
        Soldier.__init__(self,player, location, direction,\
         health, attack, defense, cost, image_id)
        self.__radius = radius

class Archer(Soldier):

    __radius = 5

    def __init__(self, player, location, direction,\
         health, attack, defense, radius, cost, image_id):
        Soldier.__init__(self,player, location, direction,\
         health, attack, defense, cost, image_id)
        self.__radius = radius

class Mag(Soldier):

    __radius = 6

    def __init__(self, player, location, direction,\
         health, attack, defense, radius, cost, image_id):
        Soldier.__init__(self,player, location, direction,\
         health, attack, defense, cost, image_id)
        self.__radius = radius

if __name__ == "__main__":

    s1 = Soldier(Player("1234", "Levon", 100, Country.ARMENIA, Color.RED), \
        Location(3,4), getRandomDirection(), 100, 150, 80)
    s2 = Soldier(Player("1235", "Raz", 100, Country.ENGLAND, Color.GREEN), \
        Location(5,12), getRandomDirection(), 100, 120, 90)

    s1.printSoldier() 
    s2.printSoldier()

    sw = Swordsman(Player("1234", "Arthur", 100, Country.FRANCE, Color.BLUE), \
        Location(10,54), getRandomDirection(), 199, 128, 88, 2)
    sw.printSoldier()