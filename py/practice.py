
"""
Python Foundations Script
-------------------------
This script covers many foundational aspects of Python:
- Variables and Data Types
- Control Flow (if/else, loops)
- Functions (including lambda functions)
- Data Structures (lists, tuples, dictionaries, sets)
- Exception Handling
- File I/O operations
- Object-Oriented Programming (classes, inheritance)
- Modules and Packages

Run the script and follow the printed sections to see examples of each topic.
"""

def section_variables():
    print("Section 1: Variables and Data Types")
    # Basic variable assignment
    a = 10                # integer
    b = 3.14              # float
    name = "Galen"        # string
    is_student = True     # boolean
    print("Integer a:", a)
    print("Float b:", b)
    print("String name:", name)
    print("Boolean is_student:", is_student)
    print()

def section_control_flow():
    print("Section 2: Control Flow (if/else and loops)")
    # if/else example
    number = 7
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    
    # For loop example
    print("For loop (printing numbers 0 to 4):")
    for i in range(5):
        print("Iteration:", i)
    
    # While loop example
    print("While loop (counting from 0 to 2):")
    count = 0
    while count < 3:
        print("Count:", count)
        count += 1
    print()

def section_functions():
    print("Section 3: Functions")
    # Defining a simple function with a parameter and a return value
    def greet(name):
        return f"Hello, {name}!"
    
    message = greet("Galen")
    print("Greeting:", message)
    
    # Lambda function: an anonymous function that squares a number
    square = lambda x: x * x
    print("Square of 4 is", square(4))
    print()

def section_data_structures():
    print("Section 4: Data Structures")
    # List: ordered, mutable collection
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")
    print("List (fruits):", fruits)
    
    # Tuple: ordered, immutable collection
    coordinates = (10, 20)
    print("Tuple (coordinates):", coordinates)
    
    # Dictionary: key-value pairs
    person = {"name": "Galen", "age": 21}
    person["city"] = "Manila"
    print("Dictionary (person):", person)
    
    # Set: collection of unique items
    unique_numbers = {1, 2, 3, 3, 2, 1}
    print("Set (unique_numbers):", unique_numbers)
    print()

def section_exception_handling():
    print("Section 5: Exception Handling")
    try:
        # Trying to divide by zero will raise an exception
        result = 10 / 0
    except ZeroDivisionError as e:
        print("Caught an exception:", e)
    finally:
        print("Finally block executed")
    print()

def section_file_io():
    print("Section 6: File I/O")
    filename = "sample.txt"
    
    # Writing to a file
    with open(filename, "w") as file:
        file.write("Hello, file!\nThis is a sample text file.\n")
    
    # Reading from a file
    with open(filename, "r") as file:
        content = file.read()
    print("File content:")
    print(content)
    print()

def section_oop():
    print("Section 7: Object-Oriented Programming")
    
    # A simple class representing an Animal
    class Animal:
        def __init__(self, name):
            self.name = name
        
        def speak(self):
            return f"{self.name} makes a sound."
    
    # Inheritance: Dog is a subclass of Animal
    class Dog(Animal):
        def speak(self):
            return f"{self.name} barks!"
    
    animal = Animal("Generic Animal")
    dog = Dog("Buddy")
    print("Animal speaks:", animal.speak())
    print("Dog speaks:", dog.speak())
    print()

def section_modules():
    print("Section 8: Modules and Packages")
    # Importing the math module and using a function from it
    import math
    print("Square root of 16 using math.sqrt():", math.sqrt(16))
    print()

def main():
    print("Welcome to Python Foundations, Galen!\n")
    section_variables()
    section_control_flow()
    section_functions()
    section_data_structures()
    section_exception_handling()
    section_file_io()
    section_oop()
    section_modules()
    print("End of Python Foundations. Happy Coding, Galen!")

if __name__ == "__main__":
    main()
