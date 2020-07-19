from abc import ABCMeta, abstractmethod

#Abstract Factory
class PizzaFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def createVegPizza(self):
        pass
    
    @abstractmethod
    def createNonVegetablePizza(self):
        pass

#Concrete Factories
class IndianPizzaFactory(PizzaFactory):

    def createVegPizza(self):
        return DeluxVeggiePizza()
    
    def createNonVegetablePizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):

    def createVegPizza(self):
        return MexicanVegetablePizza()

    def createNonVegetablePizza(self):
        return HamPizza()

#Abstract Products 
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, VegPizza):
        pass

class NonVegetablePizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self,VegPizza):
        pass
#ConcreteProducts
class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare", type(self).__name__)

class ChickenPizza(NonVegetablePizza):
    def serve(self,VegPizza):
        print(type(self).__name__,"is served with Chicken on",
        type(VegPizza).__name__)
#Another Concrete Product
class MexicanVegetablePizza(VegPizza):
    def prepare(self):
        print("Prepare", type(self).__name__)

class HamPizza(NonVegetablePizza):
    def serve(self, VegPizza):
        print(type(self).__name__, 'is served with Ham on', 
        type(VegPizza).__name__)

#<-------------------------------------------------------------------------------------------------->

#Client Interface

class PizzaStore:
    
    def __init__(self):
        pass
    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegetablePizza = self.factory.createNonVegetablePizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegetablePizza.serve(self.VegPizza)

pizza = PizzaStore()
pizza.makePizzas()   

#output
# Prepare DeluxVeggiePizza
# ChickenPizza is served with Chicken on DeluxVeggiePizza
# Prepare MexicanVegetablePizza
# HamPizza is served with Ham on MexicanVegetablePizza
