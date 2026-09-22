"""
Takes a string as input and returns the character that occurs the most along with its occurrence count.
Ignores non-alphanumeric characters and is case-sensitive.
"""


def max_occurence(string):
    counts = {}

    for char in string:
        if not char.isalnum():
            continue
        counts[char] = counts.get(char, 0) + 1

    best_char = None
    best_count = 0

    for char, count in counts.items():
        if count > best_count:
            best_char = char
            best_count = count

    print(f"Character: '{best_char}', Occurrence: {best_count}")


if __name__ == "__main__":
    max_occurence("Hello, World!")
