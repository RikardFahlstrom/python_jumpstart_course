import datetime


def print_header():
    print('---------------------------')
    print('  BIRTHDAY COUNTDOWN APP')
    print('---------------------------')
    print()


def get_birthday_from_user():
    try:
        print('Please enter your birthday information: ')
        year = int(input('Enter year [YYY]: '))
        month = int(input('Enter month [MM]: '))
        day = int(input('Enter date [DD]: '))

        birthday = datetime.date(year, month, day)
        return birthday

    except ValueError:
        print('Error: Incorrect date')
        exit()


def compute_days_between_dates(original_date, current_date):
    date1 = current_date
    date2 = datetime.date(current_date.year, original_date.month, original_date.day)
    dt = date1 - date2

    return dt.days


def print_birthday_information(days, bday, current_date):
    if days < 0:
        print('Your birthday is in {} days!'.format(-days))
    elif bday.year > current_date.year:
        print("You are not born yet!")
    elif days > 0:
        print('Your birthday was {} days ago!'.format(days))
    else:
        print('Happy Birthday!!!')


def main():
    print_header()
    bday = get_birthday_from_user()
    current_date = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, current_date)
    print_birthday_information(number_of_days, bday, current_date)


main()
