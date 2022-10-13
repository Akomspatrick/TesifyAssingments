#Create an abstract class called Vehicle
import abc

class Vehicle(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def drive_direction(self):
        pass
#Create an abstract method called drive_direction()

#Create another class Car that inherits from Vehicle
class Car(Vehicle):
    def drive_direction(self):
        pass
#Create another class Plane that inherits from Vehicle
class Plane(Vehicle):
    def drive_direction(self):
        pass
#Try running the program and fix the abstract method issues

car = Car()
plane= Plane()