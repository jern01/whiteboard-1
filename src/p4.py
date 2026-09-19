"""
This function takes two lists as input and returns a new list containing the elements that are present in both input lists.
Time complexity is O(n*m) where n and m are the lengths of the two lists since every element of one list is compared with
every element of the other list in the worst case. Space complexity is O(1) auxiliary as no additional structure is built.
"""


def intersection(list1, list2):
    result = []

    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in result:
                result.append(item1)
                break

    return result


if __name__ == "__main__":
    list1 = [4, 5, 2, 3, 1, 6]
    list2 = [8, 7, 6, 9, 4, 5]
    print(intersection(list1, list2))
