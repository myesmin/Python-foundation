"""
This is chapter 1 of the book "Automate the Boring Stuff with Python"
- Common Data Types
- Math Operators
- Data Types
- Variable Names

Math Operators:
**   power        -> 2 ** 3 = 8
%    remainder   -> 22 % 8 = 6
//   int divide  -> 22 // 8 = 2
/    divide      -> 22 / 8 = 2.75
*    multiply    -> 3 * 5 = 15
-    subtract    -> 5 - 2 = 3
+    add         -> 2 + 2 = 4

Data Types:
int    -> whole numbers (1, 2, -3)
float  -> decimals (1.5, -0.5)
str    -> text ('hello', '5')

Variable Names:
✔ use letters, numbers, _
✔ start with letter or _
✘ no spaces, symbols, or starting with numbers

Examples:
valid   -> current_balance, account4, _total
invalid -> current-balance, current balance, 4account

"""
#This program says hello and asks for my name.
print('Hello, world!')
print('What is your name?') #ask for their name 
name = input('>') #What is this '>' for?
print('It is nice to meet you, ' + name)
print('The length of your name is: ' + str(len(name))) #why str is needed to convert the length to a string?

print('What is your age') #ask for their age
age = input('>')
print('You will be ' + str(int(age) + 1) + ' in a year')


