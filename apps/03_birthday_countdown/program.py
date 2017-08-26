import datetime


def print_header():
    print('---------------------------')
    print('  BIRTHDAY COUNTDOWN APP')
    print('---------------------------')
    print()


def get_birthday_from_user():
    print('Please enter your birthday information: ')
    year = input('Enter year [YYY]: ')
    month = input('Enter month [MM]: ')
    day = input('Enter date [DD]: ')

    birthday = datetime.datetime(int(year), int(month), int(day))
    #  print(birthday)

    return birthday


def compute_days_between_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    dt = date1 - date2
    days = dt.total_seconds() / 60 / 60 / 24

    return int(days)


def print_birthday_information(days):
    if days < 0:
        print('Your birthday is in {} days!'.format(-days))
    elif days > 0:
        print('Your birthday was {} ago!'.format(days))
    else:
        print('Happy Birthday!!!')


def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)

main()
