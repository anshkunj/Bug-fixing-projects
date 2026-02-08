# Broken Python code prone to exceptions

def divide(a, b):
    return a / b  # Can raise ZeroDivisionError

def read_file(filename):
    f = open(filename, 'r')  # Can raise FileNotFoundError
    content = f.read()
    f.close()
    return content

num = int(input("Enter a number: "))  # Can raise ValueError
print("Number entered:", num)
