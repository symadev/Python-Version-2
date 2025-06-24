f=open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

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

f=open("write.txt","w")
data = f.write(" i love you so much ")
print(data)
print(type(data))

f.close()


f=open("read.txt","w")# automatic file  reate hoye chole ashbe
data = f.write(" i love you so much ")
print(data)
print(type(data))

f.close()

# f=open("demo.txt","r+")
# data = f.write(" i love you so much ")
# print(data)
# print(type(data))
#
# f.close()


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

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
with open("demo.txt", "w") as f:
    f.write("new data")# replaced text by nre data

#important example

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")
print(new_data)




word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        # if (word in data) != -1):
        print("found")
    else:
        print(" not found")


word = "xlearning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print(" not found")

