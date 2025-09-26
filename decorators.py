def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def greet():
    print("Hello, World!")

greet()



# Python এ decorator মানে হলো:
#
# এক function অন্য function কে wrap করে
#
# নতুন feature add করে
#
# আবার সেই function return করে
