#!/usr/bin/env python
import math
import enum
import random


# Using enum class create enumerations

class Player:

    '''Class Player
            Hidden members:
                (str)       __id
                (str)       __name
                (int)       __rating
                (Country)   __country
                (Color)     __color

            Constructors:
                void __init__(str, str, int, Country, Color)
    '''

    __id
    __name
    __rating
    __country
    __color

    def __init__(id, name, rating, country, color):
        self.__id = id
        self.__name = name
        self.__rating = rating
        self.__country = country
        self.__color = color

class Location:
    
    __x = 0
    __y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def copyLocation(self, location):
        self.__x = location.__x
        self.__y = location.__y
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x
    
    def setY(self, y):
        self.__y = y

    def distanceLocation(self, location):
        return math.sqrt((self.__x - location.__x)**2 + \
            (self.__y - location.__y)**2)

class Direction(enum.Enum):
    EAST = 1
    WEST = 2
    NORTH = 3
    SOUTH = 4
    EASTNORTH = 5
    EASTSOUTH = 6
    WESTSOUTH = 7
    WESTNORTH = 8
    def getRandomDirection():
        rand = random.randint(1,8)
        switch = {
            1:Direction.EAST,
	        2:Direction.WEST,
	        3:Direction.NORTH,
	        4:Direction.SOUTH,
	        5:Direction.EASTNORTH,
	        6:Direction.EASTSOUTH,
	        7:Direction.WESTSOUTH,
	        8:Direction.WESTNORTH
        }
        return switch.get(rand,0)

class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    PURPLE = 4

class Country(enum.Enum):
    ENGLAND = 1
    FRANCE = 2
    ARMENIA = 3



class Soldier:

    '''Class Soldier
            Hidden members:
                (Player)    __player
                (Location)  __location
                (Direction) __direction
                (int)       __health
                (int)       __atack
                (int)       __defense

            Constructors:
                void __init__(Player, Location, Direction,
                                int, int, int)
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
    __location

    ''' Which direction does he face?'''
    __direction = NORTH

    '''Number from [0..100] where 0 is dead.'''
    __health = 100

    '''How good is this soldier at attacking.'''
    __attack

    '''How good is this soldier at defending.'''
    __defense
	
    '''Solder knows to which player it belongs.'''
    __player

    def __init__(self, player, location, direction,\
         health, attack, defense):
    
         self.__player = player
         self.__location = location
         self.__attack = attack
         self.__defense = defense
         self.__direction = direction
         self.__health = health
    
    
    def getLocation(self):
        return self.__location

    def getDirection(self):
        return self.__direction

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
        self.__direction = self.__direction.getRandomDirection()

    '''Moves soldier in the direction it faces now.'''
    def move(self):
        if self.__direction == Direction.NORTH:
            self__location.setY(self.__location.getY() - 1)
		elif self.__direction == Direction.SOUTH:
            self__location.setY(self.__location.getY() + 1)
        elif self.__direction == Direction.EAST:
            self__location.setX(self.__location.getX() + 1)
        elif self.__direction == Direction.WEST:
            self__location.setX(self.__location.getX() - 1)
        elif self.__direction == Direction.EASTNORTH:
            self__location.setY(self.__location.getY() - 1)
            self__location.setX(self.__location.getX() + 1)
        elif self.__direction == Direction.EASTSOUTH:
            self__location.setY(self.__location.getY() + 1)
            self__location.setX(self.__location.getX() + 1)
        elif self.__direction == Direction.WESTNORTH:
            self__location.setY(self.__location.getY() - 1)
            self__location.setX(self.__location.getX() - 1)
        elif self.__direction == Direction.WESTSOUTH:
            self__location.setY(self.__location.getY() + 1)
            self__location.setX(self.__location.getX() - 1)
        else:
            print "Invalid direction"
	

if __name__ == "__main__"
    p1 = Player("Levon", 100, Armenia, RED)
    p2 = Player("Raz", 100, ENGLAND, GREEN)