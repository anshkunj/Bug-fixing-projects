# Broken Python code with runtime errors

numbers = [10, 0, 5]
for n in numbers:
    print("10 divided by", n, "is", 10 / n)  # ZeroDivisionError

data = {"name": "Kunj"}
print("Age:", data["age"])  # KeyError

text = "123"
num = text + 5  # TypeError
print(num)

arr = [1, 2, 3]
print(arr[5])  # IndexError
