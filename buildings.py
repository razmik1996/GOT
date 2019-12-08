#!/usr/bin/env python
from util import *
from player import *
from location import *

class Buildings:
    """Class Buildings
        Hidden members:
            (Player)    __player
            (Location)  __location
            (int)       __health
            (int)       __atack
            (int)       __spawnTime
            (int)       __currentSoldersCount
            (int)       __atackDistance
            (int)       __defense
        Constructor:
            __init__(self, player, location, health, atack, spawnTime,
                    atackDistance, defense)
    """
    __player = Player("", "", 0, Country.ENGLAND, Color.RED)
    __location = Location(0, 0)
    __health = 100
    __atack = 5
    __spawnTime = 5
    __currentSoldersCount = 0
    __atackDistance = 5
    __defense = 0
    
    def __init__(self, player, location, health, atack, spawnTime,\
        defense):

        self.__player = player
        self.__location = location
        self.__health = health
        self.__atack = atack
        self.__spawnTime = spawnTime
        self.__defense = defense
    
    def getPlayer(self):
        return self.__player

    def getLocation(self):
        return self.__location

    def getHealth(self):
        return self.__health    
    
    def getAttack(self):
        return self.__attack

    def getSpawnTime(self):
        return self.__spawnTime

    def getDefense(self):
        return self.__defense
    
    def setPlayer(self, player):
        self.__player = player

    def setLocation(self, location):
        self.__location = location

    def setHealth(self, health):
        self.__health = health   
    
    def setAttack(self, attack):
        self.__attack = attack

    def setSpawnTime(self, spawnTime):
        self.__spawnTime = spawnTime

    def setDefense(self, defense):
        self.__defense = defense
    
class ArcherBuilding(Buildings):
    def __init__(self, hp = 100, spawnTime = 7):
        Buildings.__init__(self, hp, spawnTime)
 
    def __str__(self):
        return "This is Archer house hp = " + str(self.__hp) + " Spawn time = " + str(self.__spawnTime)
 
class SwordsmanBuilding(Buildings):
    def __init__(self, hp = 100, spawnTime = 5):
        Buildings.__init__(self, hp, spawnTime)
 
    def __str__(self):
        return "This is Swiordsman house hp = " + str(self.__hp) + " Spawn time = " + str(self.__spawnTime)
 
class MagBuilding(Buildings):
    def __init__(self, hp = 100, spawnTime = 10):
        Buildings.__init__(self, hp, spawnTime)
 
    def __str__(self):
        return "This is Mags house hp = " + str(self.__hp) + " Spawn time = " + str(self.__spawnTime)


