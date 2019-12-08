from util import Color
from util import Country

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

    __id = ""
    __name = ""
    __rating = 0
    __country = Country.ENGLAND
    __color = Color.RED

    def __init__(self, id, name, rating, country, color):
        self.__id = id
        self.__name = name
        self.__rating = rating
        self.__country = country
        self.__color = color

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getRating(self):
        return self.__rating    
    
    def getCountry(self):
        return self.__country

    def getColor(self):
        return self.__color



    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def setRating(self, rating):
        self.__rating = rating
    
    def setCountry(self, country):
        self.__country = country

    def setColor(self, color):
        self.__color = color

    def printPlayer(self):
        print "\nPlayer settings:"
        print "\nId =", self.getId() 
        print "Name =", self.getName() 
        print "Rating =", self.getRating() 
        print "Country =", self.getCountry() 
        print "Color =",self.getColor()