#!/usr/local/bin/python3

#Practice Python

# String comparison
def string_diff(str1, str2):
    for a, b in zip(str1, str2):
        if a != b:
            return a+b

print(string_diff('car', 'cat'))

"""for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)"""


# Using a for loop
for i in range(1, 51): print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i))


numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers):
    if num % 3 == 0 and num % 5 == 0:
        numbers[i] = 'fizzbuzz'
    elif num % 3 == 0:
        numbers[i] = 'fizz'
    elif num % 5 == 0:
        numbers[i] = 'buzz'
print(numbers)


def is_odd(x):
    return bool(x % 2)

#print(is_odd(8))

the_numbers = [1,8,9,13,71,35,18,29,77,88]
print(list(filter(is_odd,the_numbers)))

# List Comprehension
print([x for x in the_numbers if is_odd(x)])


long_list_numbers = [1,8,72,4,8,9,14,55,11,12,19,78,66]
print(sorted(long_list_numbers))
print(sorted(long_list_numbers, reverse=True))



student_grades = {}
grades = [
    ('Chuck', 91),
    ('Summer', 98),
    ('Elizabeth', 81),
    ('Chuck', 88),
    ('Elizabeth', 89),
    ('Chuck', 92),
    ('Elizabeth',88),
    ('Summer',100),
    ('Elizabeth',94),
]
for name, grade in grades:
    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)
print(student_grades)

my_keys_list = list(student_grades.keys())
my_vals_list = list(student_grades.values())

#defining averages of students grades
print(my_keys_list)
print(my_vals_list)
def average_grade(my_vals_list):
    return sum(my_vals_list) / len(my_vals_list)

print("Chucks average is: " + str(average_grade(my_vals_list[0])))
print("Summers average is: " + str(average_grade(my_vals_list[1])))
print("Elizabeths average is: " + str(average_grade(my_vals_list[2])))
