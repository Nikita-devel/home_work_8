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
            if user['birthday'].date() == current_day:
                users_to_greet.append(user['name'])
            elif user['birthday'].date().weekday() > 4 and current_day.weekday() == 0:
                if (user['birthday'].date() - timedelta(days=7)).day == current_day.day:
                    users_to_greet.append(user['name'])
        if users_to_greet:
            print(f'{weekdays[day]}: {", ".join(users_to_greet)}')

def main():
    users = [
        {'name': 'Bill', 'birthday': datetime(2023, 6, 12)},
        {'name': 'Jill', 'birthday': datetime(2023, 6, 12)},
        {'name': 'Kim', 'birthday': datetime(2023, 6, 16)},
        {'name': 'Jan', 'birthday': datetime(2023, 6, 16)},
        {'name': 'John', 'birthday': datetime(2023, 6, 19)},
        {'name': 'Jane', 'birthday': datetime(2023, 6, 21)},
        {'name': 'Joe', 'birthday': datetime(2023, 6, 23)},
    ]
    
    get_birthdays_per_week(users)

if __name__ == "__main__":
    main()
