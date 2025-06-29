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



