import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        for ip in matches.groups():
            if int(ip) > 255:
                return False

        return True

    return False


if __name__ == "__main__":
    main()
