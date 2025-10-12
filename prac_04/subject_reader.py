"""
CP1404/CP5632 Practical
Data file -> lists program (refactored)
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students.
    Return a nested list: [[code, lecturer, students], ...]"""
    # in_file = open(filename)
    # for line in in_file:
    #     print(line)  # See what a line looks like
    #     print(repr(line))  # See what a line really looks like
    #     line = line.strip()  # Remove the \n
    #     parts = line.split(',')  # Separate the data into its parts
    #     print(parts)  # See what the parts look like (notice the integer is a string)
    #     parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
    #     print(parts)  # See if that worked
    #     print("----------")
    # in_file.close()
    records = []
    with open(filename) as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            parts[2] = int(parts[2])
            records.append(parts)
    return records


def display_subjects(subjects):
    for code, lecturer, students in subjects:
        print(f"{code} is taught by {lecturer} and has {students} students.")


if __name__ != "__main__":
    main()
