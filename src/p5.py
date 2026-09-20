"""
This function takes two lists as input and returns a new list containing the elements that appear in one list but not the
other. Each list is scanned in turn and an element is kept when a search of the other list finds no match, which covers
both directions of the difference. Time complexity is O(n*m) where n and m are the lengths of the two lists, since each
element of one list is compared against the other list in the worst case. Space complexity is O(1) auxiliary as no
additional structure is built, or O(n+m) counting the returned list when the lists share no elements. Sorting the result
with the merge sort from problem 1 adds O(k log k) time and O(k) space for k elements in the difference, so that the output
is in ascending order.
"""

from p1 import sort


def symmetric_difference(list1, list2):
    result = []

    for item in list1:
        if item not in list2 and item not in result:
            result.append(item)
    for item in list2:
        if item not in list1 and item not in result:
            result.append(item)

    return sort(result)


if __name__ == "__main__":
    list1 = [4, 5, 2, 3, 1, 6]
    list2 = [8, 7, 6, 9, 4, 5]
    print(symmetric_difference(list1, list2))
