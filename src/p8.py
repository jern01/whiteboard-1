"""
Takes two strings and checks if they are anagrams of each other. Non-alphanumeric characters are skipped and
every character is lowercased, so whitespace, punctuation and case are ignored.Time complexity is O(n + m)
for strings of length n and m, as each is traversed once. Space complexity is O(k) where k is the number of
unique characters in the strings.
"""


def is_anagram(str1, str2):
    counts = {}

    for char in str1:
        if char.isalnum():
            char = char.lower()
            counts[char] = counts.get(char, 0) + 1

    for char in str2:
        if char.isalnum():
            char = char.lower()
            counts[char] = counts.get(char, 0) - 1

    for count in counts.values():
        if count != 0:
            return False

    return True


if __name__ == "__main__":
    print(is_anagram("Listen", "Silent"))
    print(is_anagram("Hello", "World"))
    print(is_anagram("debit card", "bad credit"))
