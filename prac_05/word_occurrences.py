"""
CP1404/CP5632 Practical
Word Occurrences

Write a program to count the occurrences of words in a string.
The program should ask the user for a string, then print the counts of how many of each word are in the string.

Estimate: 10 minutes
Actual: 12 minutes
"""


def main():
    text = input("Enter a string: ").strip()
    words = text.lower().split()

    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    longest_word = max((len(word) for word in word_to_count))

    for word in sorted(word_to_count):
        print(f"{word:{longest_word}} : {word_to_count[word]}")

if __name__ == "__main__":
    main()
