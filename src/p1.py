"""
The algorithm used is merge sort. Because the array is split evenly regardless
of the order of elements, the time complexity is O(n log n) in all cases
(best, average, and worst). The space complexity is O(n) because we need to
create temporary arrays for the left and right halves during the merge process.
"""


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])

    return merge(left, right)


if __name__ == "__main__":
    arr = [21, 400, 8, -3, 77, 99, -16, 55, 111, -36, 28]
    print(sort(arr))
