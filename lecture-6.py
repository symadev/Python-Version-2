def calc_sum(a,b):
    #thats mean it uses one time in the function
    sum = a + b
    print(sum)
    return sum #ফলাফল রিটার্ন করে (যাতে বাইরে ব্যবহার করা যায়)

calc_sum(5,10)


calc_sum(6,12)
calc_sum(36,92)

def hello_world(a,b):
    return a+b

sum = hello_world(3,4)# this is call the function and hee a and b is called the arguments
print(sum)


print ("ritu", end=" ")#for print it in the same line
print ("rinty biti mohilam mota " )


def calk_mock(a,b=2):
    print(a+b)
    return a+b


calk_mock(1)#default value a=1 here

cities = ["dhaka", "khulna", "feni", "vola"]

movies= ["dhakaAttact", "panywise", "sinister", "piku","dhakaAttact", "panywise", "sinister", "piku"]
def print_len(list):
    print(len(list))# we just wrote here the formate


print_len(cities)

print_len(movies)


def cal_fact(n):
    fact = 1#ফ্যাক্টরিয়াল গুণ করার মাধ্যমে বের করা হয়, আর গুণের identity element হল 1
    for i in range(1, n+1):#এখানে 1 থেকে n পর্যন্ত (অর্থাৎ 1, 2, 3, ..., n) একটি লুপ চলছে।
        fact *= i#এটি fact = fact * i এর শর্টফর্ম
        #
        # প্রথমবার: fact = 1 * 1 = 1
        #
        # দ্বিতীয়বার: fact = 1 * 2 = 2
        #
        # তৃতীয়বার: fact = 2 * 3 = 6
        #
        # চতুর্থবার: fact = 6 * 4 = 24
        #
        # পঞ্চমবার: fact = 24 * 5 = 120
    print(fact)

cal_fact(5)


def converter(usd_val):
    inr_val= usd_val * 83
    print(usd_val ,"USD=" ,inr_val ,"INR")


converter(1)

converter(4)


converter(100)


#recursion function

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5)

def show(n):
    if(n == 0):
        return
    print(n)# here print the value of the n first
    show(n-1)

show(20)

def show(n):
    if(n == -1):
        return
    print(n)# here print the value of the n first
    show(n-1)

show(22)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))