#loop
i= 1
while i<=10:
    print("apna college")
    i+=1




print("loop ended")
# print a multiplication table
n=int(input("the first input is :"))
i=1
while i<=10:
    print(i*15)
    i+=1



numb= [1,2,3,4,5,6,7,8,9,10]
print(len(numb))
inx = 0
while inx< len(numb):
    print(inx)
    inx+=1



numbs = [12, 24, 37, 4, 59, 65, 74, 28, 91, 10]
x=74
i= 0
while i< len(numbs):
    if numbs[i] == x :
        print("found the value", i)
        break# mean it stop here from
    else:
        print("not found")
    i += 1# this lone is wrote wto bw in the last


i= 1
while i <= 10:
    if i%2 ==0:#cheak for even numbers

        i += 1
        continue# skip 2,4,6 and 10 and print another number

    print(i)
    i += 1


#applying the range function
for i in range(2,10,2):
    print(i)
for i in range(2, 102, 2):#(2, 102, 2)=(start, stop , increase)
    print(i)



#normal example
tuple=(12,3,4,56,78)
for val in tuple:#(2, 102, 2)=(start, stop , increase)
    print(val)

#step size negetive o hoi always
for i in range(100,1,-2):#the shep can be negetive and it print the traverse value
    print(i)
n=10
sum=0

for i in range(1,n+1):#the shep can be negetive and it print the traverse value
    sum+=i#sum = sum + i; বর্তমান সংখ্যাটি যোগ হচ্ছে মোট যোগফলে
    print("the sum is",sum)




# now using the while loop

n=12
sum =0
i=1
while i<=n:
    sum+=i #sum = sum+i
    i+=1
    print("the total sum is", sum)