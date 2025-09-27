def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]   # এখানে dictionary থেকে দাম বের করবে
        cost = price * quantity        # দাম × পরিমাণ
        print(f"total cost is {cost}") # মোট দাম দেখাবে

    except KeyError:   # যদি dictionary তে ওই item না থাকে
        print("Sorry that chai is not on menu")

    except TypeError:  # যদি quantity সংখ্যার বদলে string বা অন্য টাইপ দেওয়া হয়
        print("Quantity must be in number")


process_order("ginger", 2)    # case-1
process_order("masala", "two") # case-2





# make your own exception


# Step 1: Custom Exception Class বানানো
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be above 18"):
        self.message = message
        super().__init__(self.message)

# Step 2: Function এ ব্যবহার করা
def check_age(age):
    try:
        if age < 18:
            raise InvalidAgeError(" You are too young! Minimum age is 18.")
        else:
            print(" You are eligible!")
    except InvalidAgeError as e:
        print(e)

# Step 3: Function কল করা
check_age(15)   # Custom Exception উঠবে
check_age(20)   # ঠিক আছে





