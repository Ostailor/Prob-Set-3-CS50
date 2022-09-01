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

while True:
    try:
        date = input("Date: ")
        if date[0].isalpha() and date.find("/") == -1:
            month, day, year = date.split(" ")
            for i in range(len(months)):
                if month == months[i]:
                    month = i + 1
            day = day[0:-1]
            if 0 > int(day) or int(day) > 31:
                raise ValueError
            if 1 > int(month) or int(month) > 12:
                raise ValueError
        elif date[0].isnumeric() and date.find(" ") == -1:
            month, day, year = date.split("/")
            if 0 > int(day) or int(day) > 31:
                raise ValueError
            if 1 > int(month) or int(month) > 12:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        pass
    else:
        break

print(f"{int(year):04}-{int(month):02}-{int(day):02}")
