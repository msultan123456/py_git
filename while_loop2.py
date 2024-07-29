# Counting up to a number:

# python
# Copy code
num = 1
while num <= 10:
    print(num)
    num += 1
# Sum of numbers up to a limit:


limit = 10
sum = 0
num = 1
while num <= limit:
    sum += num
    num += 1
print("Sum of numbers:", sum)
# Printing even numbers:


num = 2
while num <= 20:
    print(num)
    num += 2
# Printing a sequence:

# python
# Copy code
count = 0
while count < 5:
    print("Hello")
    count += 1
# Reversing a string:


text = "hello"
index = len(text) - 1
while index >= 0:
    print(text[index])
    index -= 1
# Finding factorial:


n = 5
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print("Factorial:", factorial)
# Finding prime numbers:


num = 2
while num <= 20:
    is_prime = True
    check = 2
    while check <= num // 2:
        if num % check == 0:
            is_prime = False
            break
        check += 1
    if is_prime:
        print(num)
    num += 1
# User input validation:


valid = False
while not valid:
    age = input("Enter your age: ")
    if age.isdigit():
        valid = True
    else:
        print("Please enter a valid age.")
# Fibonacci sequence:


n = 10
a, b = 0, 1
while n > 0:
    print(a)
    a, b = b, a + b
    n -= 1
# Printing a triangle:


rows = 5
i = 1
while i <= rows:
    print('*' * i)
    i += 1
# Sum of digits of a number:


num = 12345
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)
# Multiplication table:


num = 5
multiplier = 1
while multiplier <= 10:
    print(num, 'x', multiplier, '=', num * multiplier)
    multiplier += 1
# Binary to decimal conversion:


binary = '1010'
decimal = 0
power = len(binary) - 1
index = 0
while index < len(binary):
    decimal += int(binary[index]) * (2 ** power)
    power -= 1
    index += 1
print("Decimal:", decimal)
# Checking palindrome:


text = "radar"
is_palindrome = True
left = 0
right = len(text) - 1
while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")
# Printing characters in a string:


text = "Python"
index = 0
while index < len(text):
    print(text[index])
    index += 1
# Finding the largest number in a list:


numbers = [3, 7, 2, 9, 5]
max_num = numbers[0]
index = 1
while index < len(numbers):
    if numbers[index] > max_num:
        max_num = numbers[index]
    index += 1
print("Largest number:", max_num)
# Calculating power:

base = 2
exponent = 5
result = 1
while exponent > 0:
    result *= base
    exponent -= 1
print("Result:", result)
# Removing duplicates from a list:


numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
index = 0
while index < len(numbers):
    if numbers[index] not in unique_numbers:
        unique_numbers.append(numbers[index])
    index += 1
print("Unique numbers:", unique_numbers)
# Finding GCD:


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

result = gcd(48, 18)
print("GCD:", result)
# Checking if a number is perfect:

num = 28
sum_divisors = 0
divisor = 1
while divisor <= num // 2:
    if num % divisor == 0:
        sum_divisors += divisor
    divisor += 1
if sum_divisors == num:
    print("Perfect number")
else:
    print("Not a perfect number")
# Printing a pattern:


rows = 5
i = rows
while i >= 1:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()
    i -= 1
# Calculating LCM:


def lcm(a, b):
    gcd = 1
    temp = a * b
    while b != 0:
        temp = b
        b = a % b
        a = temp
    gcd = a
    lcm = int(temp / gcd)
    return lcm

result = lcm(4, 5)
print("LCM:", result)
# Checking Armstrong number:

num = 153
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
# Printing a multiplication table using nested while loop:


num = 5
i = 1
while i <= 10:
    j = 1
    while j <= num:
        print(i * j, end='\t')
        j += 1
    print()
    i += 1
# Finding sum of series:


n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum of series:", sum)
# Binary search:


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

result = binary_search([2, 3, 5, 7, 9, 11], 7)
print("Index of target:", result)
# Bubble sort:


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("Sorted array:", numbers)
# Checking leap year:


year = 2024
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
# Finding factorial using a recursive function:


def factorial(n):
    if n:

# Certainly! Here are more examples of Python code using while loops:

# Calculating the sum of a series with user input:


        n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum of series:", sum)
# Printing the Fibonacci sequence up to a specified limit:


limit = 100
a, b = 0, 1
while a <= limit:
    print(a, end=' ')
    a, b = b, a + b
# Calculating the sum of digits of a number until a single digit is obtained:


num = 9876
while num >= 10:
    temp = num
    sum = 0
    while temp > 0:
        sum += temp % 10
        temp //= 10
    num = sum
print("Single digit sum:", num)
# Generating a random number between 1 and 10 and allowing the user to guess it:


import random

target = random.randint(1, 10)
guess = 0
while guess != target:
    guess = int(input("Guess the number (1-10): "))
    if guess < target:
        print("Too low, try again.")
    elif guess > target:
        print("Too high, try again.")
print("Congratulations! You guessed it.")
# Printing characters of a string in reverse order:


text = "Python"
index = len(text) - 1
while index >= 0:
    print(text[index], end=' ')
    index -= 1
# Simulating a simple ATM with balance checking and withdrawal:


balance = 1000
while True:
    print("Your balance is:", balance)
    choice = input("Press 'W' to withdraw, 'D' to deposit, or 'Q' to quit: ").upper()
    if choice == 'W':
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful. Remaining balance:", balance)
        else:
            print("Insufficient funds.")
    elif choice == 'D':
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit successful. Updated balance:", balance)
    elif choice == 'Q':
        print("Thank you for using our ATM.")
        break
    else:
        print("Invalid choice. Please try again.")
# Calculating the sum of squares of numbers from 1 to n:


n = 5
sum = 0
i = 1
while i <= n:
    sum += i ** 2
    i += 1
print("Sum of squares:", sum)
# Printing prime numbers up to a specified limit:


limit = 50
num = 2
while num <= limit:
    is_prime = True
    check = 2
    while check <= num // 2:
        if num % check == 0:
            is_prime = False
            break
        check += 1
    if is_prime:
        print(num, end=' ')
    num += 1
# Calculating the average of numbers entered by the user until a negative number is entered:


count = 0
total = 0
while True:
    num = float(input("Enter a number (negative number to stop): "))
    if num < 0:
        break
    total += num
    count += 1
if count > 0:
    average = total / count
    print("Average:", average)
else:
    print("No valid numbers entered.")
# Counting occurrences of a specific character in a string:


text = "banana"
char = 'a'
count = 0
index = 0
while index < len(text):
    if text[index] == char:
        count += 1
    index += 1
print("Occurrences of", char + ":", count)
# Reversing a number entered by the user:

num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed number:", reversed_num)
# Printing numbers in a specified range in steps of 3:


start = 1
end = 20
step = 3
while start <= end:
    print(start, end=' ')
    start += step
# Checking if a number is a power of 2:


num = 16
power_of_two = True
while num > 1:
    if num % 2 != 0:
        power_of_two = False
        break
    num //= 2
if power_of_two:
    print("Number is a power of 2.")
else:
    print("Number is not a power of 2.")
# Generating a multiplication table up to a specified limit:


limit = 5
num = 1
while num <= limit:
    multiplier = 1
    while multiplier <= limit:
        print(num * multiplier, end='\t')
        multiplier += 1
    print()
    num += 1
# Calculating the sum of natural numbers divisible by 3 or 5 up to a specified limit:


limit = 10
sum = 0
num = 1
while num <= limit:
    if num % 3 == 0 or num % 5 == 0:
        sum += num
    num += 1
print("Sum:", sum)
# Generating a pattern using nested loops:


rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()
    i += 1
# Simulating a simple dice rolling game until the user decides to stop:


import random

while True:
    input("Press enter to roll the dice...")
    dice_value = random.randint(1, 6)
    print("You rolled:", dice_value)
    choice = input("Roll again? (y/n): ").lower()
    if choice != 'y':
        break
print("Goodbye!")
# Calculating the average of positive numbers entered by the user:


count = 0
total = 0
while True:
    num = float(input("Enter a number (negative number to stop): "))
    if num < 0:
        break
    total += num
    count += 1
if count > 0:
    average = total / count
    print("Average of positive numbers:", average)
else:
    print("No positive numbers entered.")
# Calculating the sum of even numbers from 1 to n:


n = 10
sum = 0
num = 2
while num <= n:
    sum += num
    num += 2
print("Sum of even numbers:", sum)
# Calculating the product of numbers entered by the user until a zero is entered:


product = 1
while True:
    num = float(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    product *= num
print("Product of numbers:", product)
# Printing a right triangle pattern using nested loops:


rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i += 1