from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    today = datetime.now().date()
    zero_of_week = today - timedelta(days=today.weekday())
    end_of_week = zero_of_week + timedelta(days=6)

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for day in range(7):
        current_day = zero_of_week + timedelta(days=day)
        if current_day > end_of_week:
            break

        users_to_greet = []
        for user in users:
            if (user['birthday'].date().day, user['birthday'].date().month) == (current_day.day, current_day.month):
                if user['birthday'].date().year != today.year:
                    users_to_greet.append(user['name'])
            elif user['birthday'].date().weekday() > 4 and current_day.weekday() == 0:
                if (user['birthday'].date() - timedelta(days=7)).day == current_day.day:
                    if user['birthday'].date().year != today.year:
                        users_to_greet.append(user['name'])
        if users_to_greet:
            print(f'{weekdays[day]}: {", ".join(users_to_greet)}')

def main():
    users = [
        {'name': 'Bill', 'birthday': datetime(1990, 6, 12)},
        {'name': 'Jill', 'birthday': datetime(1991, 6, 12)},
        {'name': 'Kim', 'birthday': datetime(1992, 6, 16)},
        {'name': 'Jan', 'birthday': datetime(1993, 6, 16)},
        {'name': 'John', 'birthday': datetime(1994, 6, 19)},
        {'name': 'Jane', 'birthday': datetime(1995, 6, 21)},
        {'name': 'Joe', 'birthday': datetime(1996, 6, 23)},
    ]
    
    get_birthdays_per_week(users)

if __name__ == "__main__":
    main()
