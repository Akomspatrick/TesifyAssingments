#3.	Using the OOP feature Inheritance, create a class Animal with the method sound() a
# nd then create a Cat and Dog class that inherits from the Animal class.
# The Cat and Dog class should override the sound class and print a different sound.

class Animal():
    def Sound(self):
        print("No clear Sound")

class Cat(Animal):
    def Sound(self):
        print("Meow meow ")

class Dog(Animal):
    def Sound(self):
        print("Bark Bark")

animal =Animal()
animal.Sound()

cat  =Cat()
cat.Sound()
dog=Dog()
dog.Sound()