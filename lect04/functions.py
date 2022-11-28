# unnamed functions

def avg_calc(*grades):
    sum = 0
    for grade in grades:
        sum += grade
    return sum/len(grades)


print(avg_calc(3,3,3))
print(avg_calc(3,3,4,4,5,5))

def student_grades(**studnet_grades):
    for key in studnet_grades.keys():
        print(key, studnet_grades[key])
    print("---")

student_grades(name="Michal", grades=[3,4,5])
student_grades(name = "Adam", grades1 = 3, grade2 = 4,grade3 = 5)
student_grades(name = "John", grades1 = 3, grade2 = 4)

global_var = 1

# function that returns elements of geometric series
def arithmetic_series(a, r, n):
    elements = []
    for iter in range(n):
        elements.append(a*(r**iter))
    return elements

print(arithmetic_series(2,2,4))

# function that prints different values -> black or white
colour = "black"
def get_colour():
    global colour           # information that function uses global object
    if colour == "black":
        colour = "white"
        return colour
    else:
        colour = "black"
        return colour

print(get_colour())
print(get_colour())
print(get_colour())
print(get_colour())
print(get_colour())