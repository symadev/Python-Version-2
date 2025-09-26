# List comprehension:
# range(5) মানে → [0, 1, 2, 3, 4]


# x*x মানে হলো x এর square।
#
# যখন x = 0 → 0*0 = 0 → লিস্টে যোগ হবে [0]
#
# যখন x = 1 → 1*1 = 1 → লিস্টে যোগ হবে [0, 1]
#
# যখন x = 2 → 2*2 = 4 → লিস্টে যোগ হবে [0, 1, 4]
#
# যখন x = 3 → 3*3 = 9 → লিস্টে যোগ হবে [0, 1, 4, 9]
#
# যখন x = 4 → 4*4 = 16 → লিস্টে যোগ হবে [0, 1, 4, 9, 16]




squares = [x*x for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]

#Set Comprehension
nums = {x*x for x in range(5)}
print(nums)   # {0, 1, 4, 9, 16}

#
# Dictionary Comprehension
squares = {x: x*x for x in range(5)}
print(squares)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16


#Simple Dictionary
squares = {x: x*x for x in range(5)}
print(squares)



# Generator Comprehension কী?
#
# List comprehension যেমন এক লাইনে লিস্ট তৈরি করে,
#
# তেমনি Generator comprehension এক লাইনে generator object তৈরি করে।
#
#  Syntax প্রায় একই, শুধু **square bracket [ ] এর বদলে parenthesis ( ) ব্যবহার হয়।

squares = (x*x for x in range(5))
print(squares)


#
# <generator object <genexpr> at 0x0000022C8F...>
# এখানে <genexpr> মানে হচ্ছে "generator expression"
# 0x0000022C8F... হলো memory address যেখানে ওই generator object রাখা আছে।



# Example 2: Using next()
squares = (x*x for x in range(5))

print(next(squares))  # 0
print(next(squares))  # 1
print(next(squares))  # 4



#  তুমি একটা রেস্টুরেন্টে গেছো।
#
# List comprehension: তুমি সব খাবার একসাথে অর্ডার করছো, টেবিলে সব একসাথে চলে আসছে। (মেমোরি বেশি খরচ)
#
# Generator comprehension: তুমি waiter কে বলছো, “যখন আমি ডাকব, তখন একটা খাবার আনবে।” Waiter একে একে খাবার আনছে।
# (মেমোরি efficient, প্রয়োজনমতো ডেলিভারি)



# //infinate generators

def infinite_counter(start=0):
    while True:
        yield start
        start += 1   # প্রতিবার ১ করে বাড়বে

gen = infinite_counter()

# Infinite বলে break করতে হবে
for num in gen:
    if num > 10:
        break
    print(num)


def even_numbers():
    n = 0
    while True: # this is the infinite loop ,which is never finish
        yield n
        n += 2

gen = even_numbers()

for i in range(5):
    print(next(gen))
