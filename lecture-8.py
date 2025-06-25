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



