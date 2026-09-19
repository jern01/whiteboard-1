def fizzbuzz(arr):
    result = []

    for num in arr:
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(num))

    return result


if __name__ == "__main__":
    numbers = list(range(1, 101))
    print(fizzbuzz(numbers))
