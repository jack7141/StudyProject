from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__} - {self.name}, {self.age} years old {self.gender}'


