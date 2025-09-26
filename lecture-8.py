class car :
    color ="blue"
    name= "rashikh"
car1 = car()
print(car1.color)
print(car1.name)

class student :
    color ="blue"
    def __init__(self): #contructor with self perameter
     print("new added members")#constructor can call autometically

s1= student()



class student:

    def __init__(self, fullname):  # constructor
        self.name = fullname
        print("new added members")

    @staticmethod
    def hello():  # static method
        print("hello")


s1 = student("karan")  # object তৈরি হচ্ছে
print(s1.name)         # karan দেখাবে
s1.hello()             # static method কল হচ্ছে


#class student:
# এখানে তুমি একটি student নামের ক্লাস তৈরি করছো।
#
# 🔹 def __init__(self, fullname):
# এটা হলো constructor method (Python-এ এটাকে __init__ বলে)।
#
# ক্লাস থেকে যখনই কোন object তৈরি হবে, তখন __init__() অটো কল হবে।
#
# self মানে হচ্ছে object নিজেই (মানে s1 object এর reference)।
#
# fullname হচ্ছে constructor এর জন্য একটা ইনপুট প্যারামিটার।
#
# 🔹 self.name = fullname
# এই লাইনটা মানে হলো object এর মধ্যে name নামের একটা variable তৈরি করা হচ্ছে, যার মান হবে fullname।
#
# 🔹 print("new added members")
# এই লাইনটা constructor-এর ভেতরে আছে, তাই object বানানোর সময় অটো print হবে।

#

class student :

    def __init__(self, fullname,mainmarks): #contructor with self perameter
     self.name = fullname
     self.marks = mainmarks
     print("new added members")#constructor can call autometically

s1= student("karan", 67)
print(s1.name, s1.marks)


college_name= "apna college"
class student :
    college_name = "apna college"

    def __init__(self, fullname,mainmarks): #contructor with self perameter
     self.name = fullname
     self.marks = mainmarks
     print("new added members")#constructor can call autometically

s1= student("karan", 67)
print(s1.name, s1.marks)

print(student.college_name)# store at once in constructor




class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):         # ← এটা হলো method
        print("Hello", self.name)



 #encapsulation example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # __ দিয়ে private বানানো হয়েছে

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # ✅ 1500 দেখাবে


#
# __balance একটি private attribute (double underscore দিয়ে লেখা)
#
# বাইরের কেউ সরাসরি access করতে পারছে না
#
# শুধুমাত্র method (যেমন deposit, get_balance) দিয়ে access/control করা যায়



#abstruction example

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Ghew "

class Cat(Animal):
    def sound(self):
        return "Meow"

d = Dog()
print(d.sound())  # Ghew Ghew

class car:
 def __init__(self):
    self.acc=False
    self.brk=False
    self.clutch=False

 def start(self):#must write it on under the car class
    self.acc=True
    self.clutch=True
    print("car stating")

car1 = car()
car1.start()


# perameterised constructor

class Student1:
    # Parameterized Constructor
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")


# Object তৈরি করার সময় parameter দিতে হবে
s1 = Student1("Rahim", 101)
s2 = Student1("Karim", 102)

s1.display()
s2.display()



# //without Parameterized Constructor



class Student2:
    # Default constructor (no parameter except self)
    def __init__(self):
        self.name = "Unknown"
        self.roll = 0

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")


# Object বানানোর সময় কোনো parameter লাগবে না
s1 = Student2()
s2 = Student2()

s1.display()
s2.display()





#  a proper example of all

class Student:
    # Constructor (Parameterized)
    def __init__(self, name, roll, dept):
        # Attributes
        self.name = name
        self.roll = roll
        self.dept = dept

    # Method 1: Display info
    def display_info(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Dept: {self.dept}")

    # Method 2: Change department
    def change_dept(self, new_dept):
        self.dept = new_dept
        print(f"{self.name}'s department changed to {self.dept}")


# ---------------------------
# Creating Objects
s1 = Student("Rahim", 101, "CSE")
s2 = Student("Karim", 102, "EEE")

# Accessing methods
s1.display_info()
s2.display_info()

# Changing attribute using method
s1.change_dept("AI")

# Again display after change
s1.display_info()




# //example of encapsulation


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private attribute

    # Public method → balance check
    def get_balance(self):
        return self.__balance

    # Public method → deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}, New Balance = {self.__balance}")
        else:
            print("Invalid deposit amount")

    # Public method → withdraw
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}, New Balance = {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance")





# abstruction example

from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass   # শুধু method define করা হলো, implement করা হলো না

# Child Class (implementing abstract method)
class Dog(Animal):
    def sound(self):
        return "Woof Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Object তৈরি
d = Dog()
c = Cat()

print(d.sound())  # Woof Woof!
print(c.sound())  # Meow!




# //inheritance example


# Parent class
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def show_info(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels}")

# Child class (inherit Vehicle)
class Car(Vehicle):
    def __init__(self, brand, wheels, model):
        super().__init__(brand, wheels)   # Parent constructor call
        self.model = model

    def show_model(self):
        print(f"Model: {self.model}")

# Object তৈরি
v = Vehicle("Generic", 2)
v.show_info()   # Brand: Generic, Wheels: 2

c = Car("Toyota", 4, "Corolla")
c.show_info()   # Parent method reused → Brand: Toyota, Wheels: 4
c.show_model()  # Child method → Model: Corolla

