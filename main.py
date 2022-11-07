# printing
print("Hello")
age = 20
name = "Michael"
status = True
print(name, age, status)
print(name, age, status, end="\n\n", sep=";")
print("END")
# type checking
print(type(name))
# casting
number_in_string_type = "123"   # snake case for Python in prefered
numberOne = 1                   # camel case
print(int(number_in_string_type))
# special characters
print('I\'m Michael')
print('www.xyz.com/abc')
print('www.xyz.com\\abc')

class User:
    def __init__(self):
        pass

# operators
print("Result: ", 2 + 3 * 2)

# a = 1     assign
# a == 1    compare
name = None
list_of_numbers = [1,2,3]
print(5 not in list_of_numbers)
print(name is not None)

print('john' > 'JOHN')
print('JZ' > 'JOHN')
print(len("abc"))

print(5+3 == 0 and False)
print(5+3 == 0 or True)

try:
    number_from_user = int(input("Input a number"))
    print("You wrote: ", number_from_user)
except:
    print("Your value is not a number!")
