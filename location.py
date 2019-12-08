from math import sqrt

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
        return sqrt((self.__x - location.__x)**2 + \
            (self.__y - location.__y)**2)
