month_days = {"January": 31, "February": 28, "March": 31,
              "April": 30, "May": 31, "June": 30,
              "July": 31, "August": 31, "September": 30,
              "October": 31, "November": 30, "December": 31}


def is_leap(year):
    if year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 400 == 0:
        return True


def days_in_month(year, month):
    if is_leap(year) and month == "February":
        output = "29"
    else:
        output = month_days[month]
    print(f"There are {output} days in {month}.\n")


def main():
    again = True
    while again:
        while True:
            try:
                year = int(input("Enter a year: "))
                break
            except ValueError:
                print("Integer only please.")
        checker = True
        while checker:
            mth = []
            month = input("Enter a month: ").title()
            for mnth in month_days:
                mth.append(mnth)
            if month in mth:
                days = days_in_month(year, month)
                checker = False
            else:
                print("Please enter a correct month!")
    again = False





print("\nDAYS IN A MONTH CHECKER\n")
main()
another = True
while another:
    check = input("Do you want to try other months to check? Yes or No: ").lower()
    if check != "yes" and check != "no":
        print("Please Input Yes or No Only!")
    elif check == "yes":
        main()
    else:
        another = False
