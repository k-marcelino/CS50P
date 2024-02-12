import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        if matches := re.search(r"^(\d{1,2}):?(\d{0,2})\s(AM|PM)\sto\s(\d{1,2}):?(\d{0,2})\s(AM|PM)", s):
            h1, m1, p1, h2, m2, p2 = matches.groups()
            m1, m2 = map(lambda x: "0" if x == "" else x, [m1, m2])
            h1, m1, h2, m2 = map(int, [h1, m1, h2, m2])

            # Checking if the hours and minutes are out of the right ranges i.e. hours more than 12 and minutes >= 60
            if (0 <= h1 > 12) or (0 <= h2 > 12) or (0 <= m1 >= 60) or (0 <= m2 >= 60):
                raise ValueError

            # Ajusting hours accordingly to the period
            h1 = transform_hours(h1, p1)
            h2 = transform_hours(h2, p2)


            return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

        else:
            raise ValueError

    except (ValueError):
        raise


def transform_hours(h, p):
    # Checks conditions to add 12 to the number
    if ((p == "PM") and (h != 12)) or ((p == "AM") and (h == 12)):
        # Using module operator to force the answer to be at maximum 23
        return (h+ 12)%24
    else:
        return h


if __name__ == "__main__":
    main()
