month_names =  {
    1: "January",
    2: "Febuary",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"

}

date_int = input("Enter date integer: ")

date, month, year = date_int[0:2], date_int[2:4], date_int[4:6]

print(month_names[int(month)], date, year)

