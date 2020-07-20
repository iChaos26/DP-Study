#Facade Client
class EventManager(object):
    
    def __init__(self):
        print("Event Manager: Let me talk to the specialists\n")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()

#System subproperties

class Hotelier(object):
    
    def __init__(self):
        
        print("Arranging the Hotel for Marriage?--")

    def _isAvailable(self):
        
        print("Is the Hotel free for the event on given day?")
        return True

    def bookHotel(self):
        if self._isAvailable():
            print('Registered the Booking\n\n')

class Florist(object):

    def __init__(self):
        print('Flower Decorations for the Event ')

    def setFlowerRequirements(self):
        print('Carnations, Roses and Lilies would be user for Decorations and\n\n')

class Caterer(object):
        
        def __init__(self):
            print('Food arrangement for the event -- ')
        
        def setCuisine(self):
            print('Chinese e Continental Cuisine to be serve\n\n')  

class Musician(object):
    
    def __init__(self):
        print('Musical Arranging for the Marriage--')

    def setMusicType(self):
        print('Jazz and Classical will be played\n\n')

#Client Interface

class You(object):
    
    def __init__(self):
        print('You: Marriage Arrangements???')

    def askEventManager(self):
        print('You: Lets contact the Event Manager\n\n')
        EventManager().arrange()

    def __del__(self):
        print("You: Thanks to Event Manager, all preparations done!")

#Fachada pronta
you = You()
you.askEventManager()

#output 
# You: Marriage Arrangements???
# You: Lets contact the Event Manager


# Event Manager: Let me talk to the specialists

# Arranging the Hotel for Marriage?--
# Is the Hotel free for the event on given day?
# Registered the Booking


# Flower Decorations for the Event 
# Carnations, Roses and Lilies would be user for Decorations and


# Food arrangement for the event -- 
# Chinese e Continental Cuisine to be serve


# Musical Arranging for the Marriage--
# Jazz and Classical will be played


# You: Thanks to Event Manager, all preparations done!
