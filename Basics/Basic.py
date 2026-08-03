# Python & Data Science Fundamentals — Module 2 Practice Code

#1. Variables & Data Types

# Strings
name = "Rakesh"
print(name)
print(type(name))  # <class 'str'>

# Integers
age = 22
print(age)
print(type(age))  # <class 'int'>

# Floats
height = 5.9
print(height)
print(type(height))  # <class 'float'>

# Booleans
is_student = True
print(is_student)
print(type(is_student))  # <class 'bool'>

# Type conversion
age_str = str(age)
num = int("10")
pi = float("3.14")
print(age_str, num, pi)


## 2. Loops — `for` and `while`

# for loop with range
for i in range(1, 6):
    print("Number:", i)

# for loop over a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# while loop
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# break and continue
for i in range(1, 10):
    if i == 5:
        break       # stops loop when i = 5
    print(i)

for i in range(1, 6):
    if i == 3:
        continue    # skips 3
    print(i)


## 3. Functions — `def`, arguments, return values

# Basic function
def greet(name):
    print("Hello,", name)

greet("Priya")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# Default argument
def greet_with_default(name="Guest"):
    print("Welcome,", name)

greet_with_default()
greet_with_default("Sanjay")

# Multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([4, 8, 1, 9, 3])
print("Min:", low, "Max:", high)


## 4. Lists — creating, indexing, slicing, methods


# Creating a list
numbers = [10, 20, 30, 40, 50]
print(numbers)

# Indexing
print(numbers[0])    # first item -> 10
print(numbers[-1])   # last item -> 50

# Slicing
print(numbers[1:4])  # [20, 30, 40]
print(numbers[:3])   # [10, 20, 30]
print(numbers[::-1]) # reversed list

# List methods
numbers.append(60)       # add item at end
print(numbers)

numbers.remove(20)       # remove specific value
print(numbers)

numbers.sort()            # ascending sort
print(numbers)

numbers.sort(reverse=True) # descending sort
print(numbers)

print(len(numbers))       # length of list

# Looping through a list
for n in numbers:
    print(n)



## 5. Dictionaries — key-value pairs, common methods


# Creating a dictionary
student = {
    "name": "Anjali",
    "age": 21,
    "course": "Data Science"
}
print(student)

# Accessing values
print(student["name"])
print(student.get("age"))

# Adding / updating values
student["grade"] = "A"
student["age"] = 22
print(student)

# Removing a key
student.pop("grade")
print(student)

# Looping through a dictionary
for key, value in student.items():
    print(key, ":", value)

# Keys and values separately
print(student.keys())
print(student.values())


## 6. File Handling — `.txt`, `.csv`, and pandas

### Writing and reading a `.txt` file


# Writing to a text file
with open("sample.txt", "w") as file:
    file.write("Hello, this is Module 2 practice.\n")
    file.write("Learning file handling in Python.")

# Reading from a text file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())


### Writing and reading a `.csv` file (basic way)


import csv

# Writing to a CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Ravi", 23, "Python"])
    writer.writerow(["Meena", 22, "Data Science"])

# Reading a CSV file
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

## Using pandas for CSV files (recommended for Data Science)

import pandas as pd
df = pd.read_csv("students.csv")
print(df)
print(df.head())        # first 5 rows
print(df.columns)       # column names
print(df.describe())    # basic statistics
print(df["Age"].mean()) # average age
df.to_csv("students_copy.csv", index=False)


