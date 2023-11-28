def fibonacci(n,fib_dict = {}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fib_dict[n]

def generate_fibonacci_sequence(n):
    fibonacci_sequence = []
    for i in range(n):
        fibonacci_sequence.append(fibonacci(i))
    return fibonacci_sequence

result = generate_fibonacci_sequence(10)
print("Fibonacci Series")
print(result)


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes_up_to_n(n):
    for i in range(n+1):
        if is_prime(i):
            print(i)

n = int(input("Enter a number 'n' to print prime number: "))
print("Prime Number")
print_primes_up_to_n(n)


input_string= input("Enter the string to check for palindrome:")
restring= input_string[::-1]
if input_string == restring:
    print(f"{input_string} is palindrome")
else:
    print(f"{input_string} is not palindrome")


print("counts the number of lines in a file")
with open("input.txt",'r') as f1:
    f = f1.readlines()
    count= 0
    for lines in f:
        count += 1
    print(count)


print("Anagrams Check")
s1 = "earthq"
s2 = "heart"
char_list_1 = list(s1)
char_list_2 = list(s2)
char_count = {}
for char in char_list_1:
    if char not in char_count:
        char_count[char] = 0
    char_count[char] += 1

for char in char_list_2:
    if char not in char_count:
        print("The strings are not anagrams.")
        break
    char_count[char] -= 1

for count in char_count.values():
    if count != 0:
        print("The strings are not anagrams.")
        break
else:
    print("The strings are anagrams.")


def fun(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

print("prints the numbers from 1 to 100")
fun(100)
