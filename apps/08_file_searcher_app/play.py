
# Factorials are iterative processes


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n-1)


print("5!={:,}, 3!={:,}, 11!={:,}".format(
    factorial(5),
    factorial(3),
    factorial(11)
))

#  Fibonacci numbers:
#  1, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums


print("via lists")
for n in fibonacci(100):
    print(n, end=", ")


#  Same Fibonacci-function as above, but with yield instead

def fibonacci_co(limit):
    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        yield current

print()
print("via yield")
for n in fibonacci_co(100):
    print(n, end=", ")

