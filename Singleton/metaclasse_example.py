class MyInt(type):
    def __call__(cls, *args, **kwds):
        print("Here's My Int", args)
        print("Now dow whatever you want with these objects")
        return type.__call__(cls, *args, **kwds)

class int(metaclass=MyInt):
    def __init__(self,x ,y):
        self.x = x
        self.y = y

i = int(4,5)

# Here's My Int (4, 5)
# Now dow whatever you want with these objects

# O __call__ controla a instanciacao do obj por meio da nova classe, nao da classe antiga. A class int apenas aplicas as alteracoes ao construtor da antiga classe.

#<---------------------------------------------------------------------------------------->

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, \
                cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)

# <__main__.Logger object at 0x7fe15e999da0> <__main__.Logger object at 0x7fe15e999da0>
