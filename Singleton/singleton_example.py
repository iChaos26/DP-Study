class CreateSingleton(object):
#deixar o construtor da classe privado e criar um objeto(metodo estatico) que faz a inicializaca da classe
#trocar _init_ por _new_
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			return super(CreateSingleton, cls)._new_(cls)
#o metodo verifica se a classe foi iniciada, se nao, inicia o objeto novamente
s = CreateSingleton()
print ('Object created', s)
S1 = CreateSingleton()
#Object created <_main_.CreateSingleton object at 0x0000015B94F98A90>
#identifica que o objeto ja foi incializado e o atribui a nova variavel

#<------------------------------------------------------------------------------------------------------->

#lazy instanciation = trabalhar com recursos reduzidos e criar objetos somente quando necessario
#o metodo __init__ e chamado, porem nenhum objeto e criado. A criacao acontece quando chamamos o inicializador estatico

class LazySingleton:
    _instace = None 
    def __init__(self):
        if not LazySingleton._instace:
            print("__init__ method called")
        else:
            print('Instance already created:', self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls._instace:
            cls._instance = LazySingleton()
            return cls._instace

#classe e iniciada, mas o objeto nao e criado
s = LazySingleton()
#classe inicializada e objeto criado
s1 = LazySingleton.getInstance()

