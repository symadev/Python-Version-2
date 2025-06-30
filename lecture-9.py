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

#class method

class Person():
    name= "mahin kumar"

    def changeClass (self,name):
        self.name= name

p1 = Person()
p1.changeClass("rahul kumar")
print(p1.name)
print(Person.name)




class Person():
    name= "mahin kumar"

    def changeClass (self,name):
        Person.name= name

p1 = Person()
p1.changeClass("rahul kumar")
print(p1.name)
print(Person.name)




# @classmethod দিয়ে ডেকোরেট করা মেথডগুলোতে self এর জায়গায় cls প্যারামিটার ব্যবহার করা হয়।
#
# এর মাধ্যমে ক্লাসের সাথে সম্পর্কিত কাজ করা যায়, যেমন: ক্লাস লেভেল ডেটা অ্যাকসেস বা অবজেক্ট তৈরি করার জন্য ফ্যাক্টরি মেথড তৈরি করা।



# class Student:
#     school_name = "ABC School"
#
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     @classmethod
#     def change_school(cls, new_name):
#         cls.school_name = new_name
#
#     def show(self):
#         print(f"Name: {self.name}, Grade: {self.grade}, School: {Student.school_name}")
#
#
#
# p1 = Student()


print([1,2,4]+[1,2,4])# this is called the marge


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

num1 = Complex(1, 3)
num1.showNumber()
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)


    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


    num1 = Complex(1, 3)
    num1.showNumber()  # Output: 1 i + 3 j

    num2 = Complex(4, 6)
    num2.showNumber()  # Output: 4 i + 6 j

    num2 = Complex(2, 10)
    num2.showNumber()  # Output: 4 i + 6 j



    num2 = Complex(3, 6)
    num2.showNumber()  # Output: 4 i + 6 j




class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary



    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)





e1 = Employee("accountant", "Finance", "60,000")
e1.showDetails()

