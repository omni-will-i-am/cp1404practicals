"""
CP1404/CP5632 Practical 05
Wimbledon gentlemen's singles champions data processing program

This program will read a file, process the data and display the following processed information:
    the champions and how many times they have won.
    the countries of the champions in alphabetical order

Estimate: 40 minutes
Actual: 51 minutes
"""

import csv


def main():
    filename = "wimbledon.csv"
    rows = load_wimbledon_data(filename)
    champion_to_wins = count_champion_victories(rows)
    countries = get_champion_country(rows)

    print("Wimbledon Champions: ")
    for champion in sorted(champion_to_wins):
        print(f"{champion}: {champion_to_wins[champion]}")

    sorted_countries = sorted(countries)
    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))


def load_wimbledon_data(filename):
    rows: list[list[str]] = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader, None)
        for row in reader:
            if row:
                rows.append(row)
    return rows


def count_champion_victories(rows):
    champion_to_wins: dict[str, int] = {}
    for row in rows:
        champion = row[2].strip()
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def get_champion_country(rows):
    countries: set[str] = set()
    for row in rows:
        country = row[1].strip()
        countries.add(country)
    return countries


if __name__ == "__main__":
    main()
