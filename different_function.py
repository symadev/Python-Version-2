# Normal function
def add(x, y):
    return x + y

# Lambda function
add_lambda = lambda x, y: x + y

print(add_lambda(5, 3))

# pure function

def pure_add(x, y):
    return x + y

print(pure_add(2, 3))  # সবসময় 5 আসবে



# impure function
count = 0

def impure_add(x):
    global count
    count += 1
    return x + count

print(impure_add(5))  # output: 6
print(impure_add(5))  # output: 7,, cause first time the count value is the 1




# dunder function

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"


p = Person("Syma")
print(p)  # My name is Syma

