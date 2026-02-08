# Broken algorithm examples

# 1. Fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) - 1  # Logic error

print("Fibonacci of 5:", fibonacci(5))

# 2. Bubble sort
arr = [5, 2, 9, 1, 5]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] < arr[j+1]:  # Should be > for ascending
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted array:", arr)

# 3. Factorial
def factorial(n):
    result = 1
    for i in range(n):
        result *= i  # Should be i+1
    return result
print("Factorial of 5:", factorial(5))
