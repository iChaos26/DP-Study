from abc import ABCMeta, abstractmethod

#defines how section will be
class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print("PersonalSection")

class AlbumSection(Section):
    def describe(self):
        print("AlbumSection")

class PatentsSection(Section):
    def describe(self):
        print("PatentsSection")

class PublicationSection(Section):
    def describe(self):
        print("PublicationSection")

#abstract class Creator, createProfile needs a ConcreteClass to be implemented. 
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()
    
    @abstractmethod
    def createProfile(self):
        pass 
    
    def getSection(self):
        return self.sections
    
    def addSections(self, section):
        self.sections.append(section)
#ConcreteClass Creator ->> aqui ocorre a verdadeira criacao dos objetos
class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())
#ConcreteClass Creator
class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

#client
if __name__ == "__main__":
    profile_type = input("Qual profile criar?")
    profile = eval(profile_type.lower())()
    print("Criando perfil", type(profile).__name__)
    print("Perfil tem secoes --", profile.getSection())