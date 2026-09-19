"""
This function generates the Fibonacci sequence up to the nth number using recursion.
Bonus: Using iteration instead of recursion to prevent stack overflow for large n.
"""


def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    sequence = fibonacci(n - 1)
    sequence.append(sequence[-1] + sequence[-2])
    return sequence


if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    print(fibonacci(n))
