# Write a program to count even numbers and odd numbers stored in a list.
numbers = [10, 25, 33, 42, 55, 60, 71, 84]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)