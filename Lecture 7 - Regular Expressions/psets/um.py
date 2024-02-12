import re


def main():
    print(count(input("Text: ")))


def count(s):
    # Pretty straightforward, just gets the len of all appearances
    return len(re.findall(r"\b(um)\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()
