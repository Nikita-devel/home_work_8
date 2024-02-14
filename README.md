[Main page](https://github.com/Nikita-devel) | [Python Core Page](https://github.com/Nikita-devel/Python_Core)

# Birthday Greetings

This Python script checks and prints the upcoming birthdays for the current week and the next week. It considers the weekdays and weekends and outputs the names of users whose birthdays fall within these periods.

## Usage

1. Make sure you have Python installed on your system.

2. Clone the repository:

    ```bash
    git clone https://github.com/Nikita-devel/home_work_8.git
    ```

3. Navigate to the project directory:

    ```bash
    cd home_work_8
    ```

4. Run the script:

    ```bash
    python birthday_greetings.py
    ```

5. View the output in the console.

## Example

```python
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # The function implementation...

def main():
    users = [
        {'name': 'Bill', 'birthday': datetime(1990, 6, 12)},
        {'name': 'Jill', 'birthday': datetime(1991, 6, 12)},
        # Add more users as needed
    ]
    
    get_birthdays_per_week(users)

if __name__ == "__main__":
    main()
```
