#Create a class called Human
class Human:
    leg_count=4
    def get_gender(self):
        return "Unknown"
#Add an attribute leg_count with the value of 4

#Add a method called get_gender() that returns "Unknown" in the Human class

#Create another class called Man that extends Human
class Man(Human):
    def get_gender(self):
        return "Man"
#Create another class called Woman that extends Human
class Woman(Human):
    def get_gender(self):
        return "Woman"
#In the class, Man create the method get_gender() which should return "man"

#In the class, Woman create the method get_gender() which should return "woman"

#Instantiate the Man and Woman classes
man = Man()
print("Man "+ man.get_gender())

woman = Woman()
print("Woman "+ woman.get_gender())

#Print out the value of get_gender() from the Man and Woman object instances