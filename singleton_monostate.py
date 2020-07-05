class Borg:
    _shared_state = {"1":"2"}
    def __init__(self):
        self.x = 1
        self.__dict__ = self._shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 4

print ("Borg Object 'b':", b)
print ("Bor Object 'b1':", b1)
print ("Object State 'b':", b.__dict__)
print ("Object State 'b1':", b1.__dict__)

#B e B1 compartilham o mesmo estado

# Borg Object 'b': <__main__.Borg object at 0x7f3323ed5b70>
# Bor Object 'b1': <__main__.Borg object at 0x7f3323ed5ba8>
# Object State 'b': {'1': '2', 'x': 4}
# Object State 'b1': {'1': '2', 'x': 4}
 
class Borg(object):
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj.__dict__ = cls._shared_state
        return obj

#Ajustado usando __new__
