"""
~ Singleton Pattern ensures only instance of class is created.(Creational Design Pattern)
~ Usage - When Control access to shared database or file.
        - When provide access to global variable.
"""

from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def req_data():
        """Implement In Child Class"""
    
class PersonSingleton(IPerson):
    __instance = None   # Private instance
    
    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance
    
    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton Error, Initiated More than once !")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
    
    @staticmethod
    def req_data():
        print(f"Name is: {PersonSingleton.__instance.name}, Age is: {PersonSingleton.__instance.age}")
    
p = PersonSingleton("Name1", 25)
print(p)
p.req_data()