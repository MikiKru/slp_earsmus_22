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
