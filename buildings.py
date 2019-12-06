#!/usr/bin/env python

class Buildings:
    __hp
    __spawnTime
    __currentSoldersCount
    
    def __init__(self, hp = 100, spawnTime = 5):
        self.__hp = hp
        self.__spawnTime = spawnTime

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


