"""
A Simple script to practice Python Basics:
- Variables
- Input and Output
- String formatting
"""
# def is a function declaration
def main(): 
    name = input("Enter your name:")
    birth_year = int(input("Enter your birth year:")) # int() is a function that converts the input to an integer
    current_year = 2025
    age = current_year - birth_year 

    print(f"\nHello, {name}!)")
    print(f"You are approximately {age} years old.")
    print(f"Your name has {len(name)} characters.")

""" 
if __name__ == "__main__": is needed to control when code runs
- When you run this file directly: __name__ == "__main__", so main() executes
- When you import this file as a module: __name__ == "hello", so main() does NOT execute
- This allows the same file to be both a script AND a reusable module  
"""
if __name__ == "__main__":
    main()


