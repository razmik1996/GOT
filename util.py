import math
import random
import enum

class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    PURPLE = 4

class Country(enum.Enum):
    ENGLAND = 1
    FRANCE = 2
    ARMENIA = 3

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

class Location:
    
    __x = 0
    __y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "x = " + str(self.__x) + " y = " + str(self.__y)
    
    def __repr__(self):
        return { 'x':self.__x, 'y':self.__y }
    
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

