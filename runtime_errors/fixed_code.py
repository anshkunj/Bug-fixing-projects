# Fixed Python code

numbers = [10, 0, 5]
for n in numbers:
    if n != 0:  # Prevent division by zero
        print("10 divided by", n, "is", 10 / n)
    else:
        print("Cannot divide by zero:", n)

data = {"name": "Kunj"}
age = data.get("age", "Not Provided")  # Safely access
print("Age:", age)

text = "123"
num = int(text) + 5  # Convert string to int
print(num)

arr = [1, 2, 3]
if len(arr) > 5:
    print(arr[5])
else:
    print("Index 5 out of range, max index is", len(arr)-1)
