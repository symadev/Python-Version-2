f=open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()# here f means file

f=open("read.txt","r")#file ta open korlo
data = f.read()# file ta read korlo
print(data)# file ar data k print korlo
print(type(data))#ki type ar data ta include korlo
f.close()# fila ta close kore dilo

f=open("demo.txt","r")
data = f.read(10)
print(data)
print(type(data))
f.close()

f=open("demo.txt","r")
data = f.readline()
print(data)
print(type(data))
f.close()




f=open("read.txt","w")
data = f.write("ritu you are the best man , oh hooo!!!")
print(data)
print(type(data))

f.close()

f=open("write.txt","w")
data = f.write(" ritu you are the best man , oh hooo!! ")
print(data)
print(type(data))

f.close()


f = open("demo.txt", "a+")
# f.write("abc")
print(f.read())
f.write("abc")
f.close()

#print(f.read())
# This tries to read the file contents, but it won't show anything. Why?
#
# Because when you open in "a+" mode, the file pointer is at the end of the file.
#
# f.read() reads from the current position to the end — but there's nothing after the end!
#
# So, you should add f.seek(0) before reading.

f= open ("demo.txt","r+")
f.write("abc")#
print(f.read())
f.close()

with open("demo.txt", "r") as f: # with use korle kaj shesh hole python nije file off kore dey
    data = f.read()
    print(data)
with open("demo.txt", "w") as f:
    f.write("new data")# replaced text by nre data

#important example

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")
print(new_data)












order_amount=int(input("enter your order amount :"))

delivery_cost= 0 if order_amount > 300 else 30

print(" the delivery price is:",delivery_cost)


for token in range  (1,10): # 0-9 index print hobe just
    print("this is my value", token)

