#!/usr/bin/env python
import util


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

    __id = ""
    __name = ""
    __rating = 0
    __country = util.Country.ENGLAND
    __color = util.Color.RED

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
    __location = util.Location(0,0)

    ''' Which direction does he face?'''
    __direction = util.Direction.NORTH

    '''Number from [0..100] where 0 is dead.'''
    __health = 100

    '''How good is this soldier at attacking.'''
    __attack = 0

    '''How good is this soldier at defending.'''
    __defense = 0
    
    '''Solder knows to which player it belongs.'''
    __player = Player("", "", 0, util.Country.ENGLAND, util.Color.RED)

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
        self.__direction = util.getRandomDirection()

    '''Moves soldier in the direction it faces now.'''
    def move(self):
        if self.__direction == util.Direction.NORTH:
            self.__location.setY(self.__location.getY() - 1)
        elif self.__direction == util.Direction.SOUTH:
            self.__location.setY(self.__location.getY() + 1)
        elif self.__direction == util.Direction.EAST:
            self.__location.setX(self.__location.getX() + 1)
        elif self.__direction == util.Direction.WEST:
            self.__location.setX(self.__location.getX() - 1)
        elif self.__direction == util.Direction.EASTNORTH:
            self.__location.setY(self.__location.getY() - 1)
            self.__location.setX(self.__location.getX() + 1)
        elif self.__direction == util.Direction.EASTSOUTH:
            self.__location.setY(self.__location.getY() + 1)
            self.__location.setX(self.__location.getX() + 1)
        elif self.__direction == util.Direction.WESTNORTH:
            self.__location.setY(self.__location.getY() - 1)
            self.__location.setX(self.__location.getX() - 1)
        elif self.__direction == util.Direction.WESTSOUTH:
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
         health, attack, defense, radius):
        Soldier.__init__(self,player, location, direction,\
         health, attack, defense)
        self.__radius = radius

class Archer(Soldier):

    __radius = 5

    def __init__(self, player, location, direction,\
         health, attack, defense, radius):
        Soldier.__init__(self,player, location, direction,\
         health, attack, defense)
        self.__radius = radius

class Mag(Soldier):

    __radius = 6

    def __init__(self, player, location, direction,\
         health, attack, defense, radius):
        Soldier.__init__(self,player, location, direction,\
         health, attack, defense)
        self.__radius = radius

if __name__ == "__main__":

    s1 = Soldier(Player("1234", "Levon", 100, util.Country.ARMENIA, util.Color.RED), \
        util.Location(3,4), util.getRandomDirection(), 100, 150, 80)
    s2 = Soldier(Player("1235", "Raz", 100, util.Country.ENGLAND, util.Color.GREEN), \
        util.Location(5,12), util.getRandomDirection(), 100, 120, 90)

    s1.printSoldier() 
    s2.printSoldier()

    sw = Swordsman(Player("1234", "Arthur", 100, util.Country.FRANCE, util.Color.BLUE), \
        util.Location(10,54), util.getRandomDirection(), 199, 128, 88, 2)
    sw.printSoldier()
    
