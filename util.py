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
    return switch.get(rand)

def getRandomDirectionP1():
    rand = random.randint(1,5)
    switch = {
        1:Direction.EAST,
        2:Direction.NORTH,
        3:Direction.SOUTH,
        4:Direction.EASTNORTH,
        5:Direction.EASTSOUTH,
    }
    return switch.get(rand)

def getRandomDirectionP2():
    rand = random.randint(1,5)
    switch = {
        1:Direction.WEST,
        2:Direction.NORTH,
        3:Direction.SOUTH,
        4:Direction.WESTSOUTH,
        5:Direction.WESTNORTH
    }
    return switch.get(rand)