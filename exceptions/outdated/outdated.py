months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date = get_formatted_date()
    print_date(date)


def get_formatted_date():
    while True:
        try:
            d = input("Date: ")
            d_list = d.split("/")
            if (1 <= int(d_list[0]) <= 12 and 1 <= int(d_list[1]) <= 31 and int(d_list[2]) >= 0):
                year = int(d_list[2])
                month = int(d_list[0])
                day = int(d_list[1])
                break

        except ValueError:
            d_list = d.split(" ")
            if (d_list[0] in months and 1 <= int(d_list[1][0:d_list[1].index(",")]) <= 31 and int(d_list[2]) >= 0):
                year = int(d_list[2])
                month = months.index(d_list[0]) + 1
                day = int(d_list[1][0:d_list[1].index(",")])
                break
        else:
            pass

    return [year, month, day]


def print_date(d):
    print(f"{d[0]:04}-{d[1]:02}-{d[2]:02}")


if __name__ == "__main__":
    main()
