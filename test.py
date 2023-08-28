# print(6*2-5/(1+4)+3**2)
# print(6*2-5/5)

# print((6-2)/(5*(1+4))+3)
# print(type("a"))

# def greeting(name, age): #parameter
#     print("my name is " + name) #message
#     print("i'm " + age) #message

# greeting("lusi","21")

# print(5//2)

# print((2**2)==4)

# def difference(x,y):
# 	z=x-y
# 	return z
# print(difference(5,3))

# print(7<"number")

# def decade_counter():
#     while year < 50:
#         year += 10
#     return year

# for count in range(1,6):
#     print(count+1)

# num1 = 0
# num2 = 0
# for x in range(5):
#     num1 = x
#     for y in range(14):
#         num2 = y+3
# print(num1+num2)

# def count_to_ten():
#     x=1
#     while x <= 10:
#         print(x)
#         x+=1
# count_to_ten()

# for x in range(1,10,3):
#     print(x)

# name = "papayaa"
# print(name[:3] + name[3:])

# print("saya"[1:2])

# animals = "lions tigers and bears"
# print ("tigers" in animals)

# print("this is anoter".isnumeric())

# x="jalan jaan"
# print(x.endswith("jaan"))

# def is_palindrome(input_string):
#     new_string = ""
#     reverse_string = ""

#     for letter in input_string:
#         if letter != " ":
#             new_string += letter
#             reverse_string = letter + reverse_string

#     if new_string.lower() == reverse_string.lower():
#         return True
#     else:
#         return False

# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True

# print("rainfall"[:4])

# x=["saya","makan"]
# print(len(x))
# print("saya" in x)

# def pig_latin(text):
#     say = ""
#     # Separate the text into words
#     words = text.split()
#     pig_latin_words = []
#     for word in words:
#         # Create the pig latin word and add it to the list
#         # In Pig Latin, move the first letter to the end and add "ay"
#         pig_word = word[1:] + word[0] + "ay"
#         pig_latin_words.append(pig_word)
#     # Turn the list back into a phrase
#     say = " ".join(pig_latin_words)
#     return say

# print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun"))

# def groups_per_user(group_dictionary):
#     user_groups = {}
#     # Go through group_dictionary
#     for group, users in group_dictionary.items():
#         # Now go through the users in the group
#         for user in users:
#             # Now add the group to the list of groups for this user
#             if user in user_groups:
#                 user_groups[user].append(group)
#             else:
#                 user_groups[user] = [group]
#     return user_groups

# print(groups_per_user({
#     "local": ["admin", "userA"],
#     "public": ["admin", "userB"],
#     "administrator": ["admin"]
# }))

# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)

# def sales_prices(item_and_price):
#     # Initialize variables "item" and "price" as strings
#     item = ""
#     price = ""
#     # Create a variable "item_or_price" to hold the result of the split. 
#     item_or_price = item_and_price.split()

#     # For each element "x" in the split variable "item_or_price" 
#     for x in item_or_price:

#         # Check if the element is a number
#         if x.isalpha():

#             # If true, assign the element to the "item" string variable and add a space 
#             # for any item names containing multiple words, like "Winter fleece jacket".
#             item += x + " "
#             print(item)

#         # Else, if x is a number (if x.isalpha() is false): 
#         else:
#             # Assign the element to the "price" string variable. 
#             price = x
#             print(price)

#     # Strip the extra space to the right of the last "item" word
#     item = item.strip()

#     # Return the item name and price formatted in a sentence 
#     return "{} are on sale for ${}".format(item,price)


# # Call to the function 
# print(sales_prices("Winter fleece jackets 49.99"))

# car_make = "Lamborghini"
# print(car_make[3:-5])
# print(car_make[-4:])
# print(car_make[:7])

# car_makes = ["Ford", "Volkswagen", "Toyota"]
# car_makes.remove("Ford")
# print(car_makes)

# host_addresses = {"router": "192.168", "localhost": "127.001"}
# print(host_addresses.keys())

# import numpy as np

# def numpyArray():
#     x = np.array([[1, 2, 3],[4, 5, 6]], np.int32)
#     y = numpy.array([[3, 6, 2],[9, 12, 8]], np.int32)
#     return x*y
# print(numpyArray())

print("hello")