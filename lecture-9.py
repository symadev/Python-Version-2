#last of oop
class Student:
    def __init__(self,name):
        self.name= name

s1=Student("ritu")
print(s1)
del s1#name 's1' is not defined because it deleted from here



class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no= acc_no
        self.acc_pass= acc_pass

s1=Account("123456","abcde")
print(s1.acc_no)
print(s1.acc_pass)

# self.acc_no = acc_no মানে হচ্ছে →
# এই ক্লাসের অবজেক্টে acc_no নামের একটা প্রপার্টি রাখো, আর সেটার ভ্যালু হবে ইউজার যেটা পাঠিয়েছে।



class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no= acc_no
        self.__acc_pass= acc_pass# for do it private

    def __int__(self,acc_pass):
        self.__acc_pass=acc_pass
        print(acc_pass)# now it print because inside of the class

s1=Account("123456","abcde")
print(s1.acc_no)

# we can not access the pass in the outside of the class


class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1 = ToyotaCar("marcedies")
car2 = ToyotaCar("lemborgini")

print (car1.name)
print (car2.name)
print (car1.start())#cause we access the car through the toyotacar


print (car1.stop())



# Multilevel inheritance



class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand


class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

carmain2 =ToyotaCar("this is new car")
car1 = Fortuner("this is my fancy car")
print(carmain2.brand)
print(car1.type)
print(car1.start())
print(car1.start())



class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand


class Prius(ToyotaCar):
    def __init__(self,type):
        self.type=type
        super().__init__(type)#


car2 = Prius("red class")
print(car2.type)

# কটি superclass থেকে অন্যান্য ক্লাস ডেটা বা মেথড উত্তরাধিকার (inherit) পায়।



class Animal:
    def sound(self):
        print("animal sound")

class Dog(Animal):
    def sound(self):
        print("ghew ghew")

class Cat(Animal):
    def sound(self):
        print("mew mew")



animal1= Cat()
print(animal1.sound())



class Person():
    name= "mahin kumar"

    def changeClass (self,name):
        self.name= name

p1 = Person()
p1.changeClass("rahul kumar")
print(p1.name)
print(Person.name)















