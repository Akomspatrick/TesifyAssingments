#Create a class called Human
class Human:
    leg_count=4
    def get_gender(self ):
        return "Unknown"
#Add an attribute leg_count with the value of 4

#Add a method called get_gender() that returns "Unknown" in the Human class

#Create another class called Man that extends Human
class Man(Human):
    pass

human = Human()
print('HUman '+human.get_gender())
man = Man()
print('man '+ man.get_gender())
#Optionally you can instantiate the classes Man and Woman then print out t
# he values of the get_gender() method in each object instance
