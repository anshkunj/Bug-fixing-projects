# Fixed Python code

def sum_even_numbers(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:  # Corrected to even numbers
            total += i
    return total

print("Sum of even numbers from 1 to 10:", sum_even_numbers(10))

numbers = [10, 20, 30, 40]
max_num = numbers[0]
for num in numbers:
    if num > max_num:  # Corrected comparison
        max_num = num
print("Maximum number is:", max_num)
