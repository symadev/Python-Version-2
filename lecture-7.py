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