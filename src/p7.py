"""
Computes the square root of a non-negative integer using binary search. The root of x cannot exceed x//2 for x >= 2,
so the range from 1 to x//2 is repeatedly halved until the square root is found. The function returns the integer
part of the square root. Time complexity is O(log n) since the range is halved with each iteration. Space complexity
is O(1) as only two bounds and mid are held regardless of input size.
"""


def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")

    if x < 2:
        return x

    low = 1
    high = x // 2

    while low <= high:
        mid = (low + high) // 2
        square = mid * mid

        if square == x:
            return mid

        if square < x:
            low = mid + 1
        else:
            high = mid - 1

    return high


if __name__ == "__main__":
    print(square_root(144))
