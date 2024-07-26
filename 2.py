months_days = {
    'January': 31,
    'February': 28,  # 29 for leap years, but we'll use 28 for non-leap years
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

entered_month = input("Enter name of month: ")
print(f"The month of {entered_month} has {months_days[entered_month.title()]} days")