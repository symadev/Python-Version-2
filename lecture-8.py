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



class student :

    def __init__(self, fullname): #contructor with self perameter
     self.name = fullname
     print("new added members")#constructor can call autometically

s1= student("karan")
print(s1.name)

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