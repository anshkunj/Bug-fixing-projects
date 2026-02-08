# Fixed Python code with proper exception handling

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None

try:
    num = int(input("Enter a number: "))
    print("Number entered:", num)
except ValueError:
    print("Error: Invalid input, not a number")
