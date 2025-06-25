str1 = "my name is tisha.\n i am 23 years old"
strmain = "my name is ritu"
print(len(strmain))
print(str1)
print(len(str1))
#indexing
print(str1[5])

#slicing

print(str1[5:10])
print(str1[6:15])
print(str1[6:])

str2="apnacollege"
print(str2[-10:-5])


str3 = "my name is tisha.\n i am 23 years old"
print(str3.find("my"))
str4=str3.capitalize()
print(str4)
print(str3.count("m"))
print(str3.replace("a","h"))



#conditinal statement
age= 8
if age>=10:
    print("yes this is i am ")
elif  age >= 9:
    print("this is my sister ")
else:
    print("this is my  mom")



#conditinal statement with input
age =int(input("my real age is:"))
if age >= 11:
    print("yes this ritu ")
elif  age<= 8:
    print("this is my sister ")
else:
    print("this is my  mom")

