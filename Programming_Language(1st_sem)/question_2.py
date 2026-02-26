# Write a program to display prime numbers up to 200
for num in range(2, 201):  
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)