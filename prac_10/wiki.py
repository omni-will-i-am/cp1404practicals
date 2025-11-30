"""
CP1404/CP5632 Practical
Wikipedia API example with exception handling
"""

import wikipedia


def main():
    """Prompt user for a page title (input) and show details from Wikipedia (output) until blank user input."""

    title = input("Enter Wikipedia page title or search phrase: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)  # no autosuggest for now
            print(page.title)
            print(page.summary)

            one_sentence_summary = wikipedia.summary(page.title, sentences=1, auto_suggest=False)
            print(one_sentence_summary)

            print(page.url)

        except wikipedia.exceptions.PageError:
            print(f'Page ID "{title}" does not match any pages. Try another ID!')

        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        print()
        title = input("Enter Wikipedia page title or search phrase: ").strip()

    print("Thank you for using Practical Wikipedia API!")


if __name__ == "__main__":
    main()
