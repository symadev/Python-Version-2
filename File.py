file = open("order.txt", "w")   # Opens (or creates) 'order.txt' in write mode
try:
    file.write("Masala chai – 2 cups")  # Writes text into the file
finally:
    file.close()   # Ensures the file is closed, even if an error occurs

    #
    # make a new file in write mode.যদি ফাইল না থাকে, তাহলে "w" মোড নতুন ফাইল তৈরি করে।

    # যদি ফাইল আগে থেকে থাকে, তাহলে সেটার কনটেন্ট মুছে ফেলে (overwrite করে) নতুন করে লেখা শুরু করে।


