from typing import Dict


def main():
    FRANKENSTEIN_PATH = "books/frankenstein.txt"
    contents = read_file(FRANKENSTEIN_PATH)
    letter_map = map_letters(contents)

    report_start = f"Begin report of {FRANKENSTEIN_PATH}"
    formatted_report_start = get_report_delimiter(report_start)
    print(formatted_report_start)

    report_words(contents)
    print()
    report_letters(letter_map)

    report_end = "End report"
    formatted_report_end = get_report_delimiter(report_end)
    print(formatted_report_end)


def read_file(path: str) -> str:
    with open(path, "r") as file:
        return file.read()


def map_letters(s: str) -> Dict[str, int]:
    letter_map: Dict[str, int] = {}

    for char in s:
        if not char.isalpha():
            continue
        char = char.lower()
        if char in letter_map:
            letter_map[char] += 1
        else:
            letter_map[char] = 1

    return letter_map


def get_report_delimiter(s: str) -> str:
    return f"--- {s} ---"


def get_word_count(s: str) -> int:
    return len(s.split())


def format_report_line(char: str, count: int) -> str:
    return f"The '{char}' character was found {count} times"


def report_words(s: str) -> None:
    word_count = get_word_count(s)
    print(f"{word_count} words found in the document")


def report_letters(d: Dict[str, int]) -> None:
    for letter, count in sorted(d.items(), key=lambda x: x[1], reverse=True):
        print(format_report_line(letter, count))


if __name__ == "__main__":
    main()
