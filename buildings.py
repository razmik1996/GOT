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
    __player = Player("", "", 0, Country.ENGLAND, Color.RED, 1000)
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

    def showBuilding(self):
        pass

    
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
    __image = "Sprites/Towers/ArcherTower.png"

    def __init__(self, player, location, health, atack, spawnTime, defense):
        Buildings.__init__(self, player, location, health, atack, spawnTime, defense)

    def __str__(self):
        return "This is Archer house hp = " + str(self.__health) + " Spawn time = " + str(self.__spawnTime)

    def getImage(self):
        return self.__image

    def showBuilding(self):
        pass


    
class SwordsmanBuilding(Buildings):
    __image = "Sprites/Towers/Tower2.png"

    def __init__(self, player, location, health, atack, spawnTime, defense):
        Buildings.__init__(self, player, location, health, atack, spawnTime, defense)
 
    def __str__(self):
        return "This is Swiordsman house hp = " + str(self.__health) + " Spawn time = " + str(self.__spawnTime)

    def getImage(self):
        return self.__image

class MagBuilding(Buildings):
    __image = "Sprites/Towers/Tower3.png"

    def __init__(self, player, location, health, atack, spawnTime, defense):
        Buildings.__init__(self, player, location, health, atack, spawnTime, defense)
 
    def __str__(self):
        return "This is Mags house hp = " + str(self.__health) + " Spawn time = " + str(self.__spawnTime)

    def getImage(self):
        return self.__image