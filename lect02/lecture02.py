# String
text = "python"
row_csv = "Michal;Kruczkowski;Lecturer;PBS"

print(text.capitalize())
print(row_csv.split(";"))
print(len(text))

# List
params = [1,2,3,4,5]
numbers_generated = range(10, 20, 3)
print(*numbers_generated)
# last element from list
print(params[-1])
print(params[len(params) - 1])
# dynamically changes
params.append([1,2,3])
print(params)
print(params[5][2])
params[5].remove(2)
print(params)


# element = int(input("write value ...."))
# print(element in params)

nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print(nested_list)

for row in nested_list:
    for data in row:
        print(data, end=" ")
    print()

# Tuple
static_elements = 3.14, 3.21
print(static_elements)
# static_elements.__add__(3)
print(static_elements[0])

static_elements = static_elements + tuple([1])      # tuple is immutable but here we have reinitialization
print(static_elements)

# Dictionary
roman_to_arabic = {1 : "I", 2 : "II", 3 : "III", 4 : "IV", 5 : "V"}
arabic_to_roman = {"I" : 1, "II" : 2, "III" : 3, "IV" : 4, "V" : 5}
print(roman_to_arabic)
print(arabic_to_roman)

roman_to_arabic[6] = "VI"
roman_to_arabic[1] = "iii"      # what will happend

for key in roman_to_arabic.keys():
    print(key, roman_to_arabic[key])

# roles = frozenset(['admin', 'user'])      # immutable
roles = set(['admin', 'user'])              # mutable
print(roles)
roles.add('author')
roles.add('author')
roles.add('author')
roles.remove('user')
print(roles)

# check the permissions
print('moderator' in roles)

# operations on sets
s1 = set([1,2,3])
s2 = set([3,4])

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)
print(s1 ^ s2)