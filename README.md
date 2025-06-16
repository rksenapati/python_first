Assignment 1
--------------
Task 1 – Basic Arithmetic Operations
This script performs basic arithmetic calculations on two numbers entered by the user:

Prompts the user to input two integers.

Performs and displays the result of the following operations:

Addition

Subtraction

Multiplication

Division

This script collects and combines the user's first and second names to display a personalized greeting message.

Prompts the user to input their first and second name.

Concatenates and prints a friendly welcome message using the full name.

Assignment2
------------

Task 1

Even or Odd Number Checker
This script determines whether a given number is even or odd.

Prompts the user to input an integer.

Uses the modulus operator % to check if the number is divisible by 2.

Prints a message indicating whether the number is even or odd.

Task 2

Sum of Numbers from 1 to 50
This script calculates the sum of all numbers from 1 to 50 using a for loop.

Initializes a counter (number) to 0.

Iterates from 0 to 50 using range(0, 51).

Adds each number in the range to the counter.

Prints the final sum.

Assignment 3
---------------

Task 1
Factorial Calculator Using Recursion
This script calculates the factorial of a given number using a recursive function.

Prompts the user to input a number.

Defines a recursive function factorial(n):

If n is less than 2, it returns 1 (base case).

Otherwise, it returns n * factorial(n-1).

Calls the factorial() function with the input and prints the result.

Task 2

Mathematical Functions using the math Module
This script performs several mathematical calculations on a user-provided number using the math module.

Prompts the user to enter a number.

Calculates and displays:

Square root using math.sqrt()

Natural logarithm (base e) using math.log()

Sine value (in radians) using math.sin()

Assignment 4
-------------
Task 1
Safe File Reading with Error Handling
This program attempts to open and read a file named sample.txt, printing its contents line by line. It also includes error handling to gracefully manage missing files.

🔧 Functionality:
Uses a try-except block to catch errors.

Opens the file in read mode ("r") using a with statement to ensure proper closure.

Uses readlines() to read all lines and iterates through them using a for loop.

Prints each line exactly as it appears in the file.

If the file does not exist, it prints a user-friendly error message:
"Error: 'sample.txt' not found."

Task 2

Full File Workflow: Write, Append, and Read
This program demonstrates a complete file handling workflow in Python using output.txt. It includes writing initial content, appending additional content, and finally reading and displaying the file contents.

🔧 Functionality:
Write to File ('w' mode)

Prompts the user for input.

Writes the text to output.txt (overwrites existing content).

Confirms successful write.

Append to File ('a' mode)

Prompts for additional input.

Appends the new text to the same file.

Confirms successful append.

Read from File ('r' mode)

Opens output.txt in read mode.

Reads all lines using readlines() and prints each line.
