from datetime import date #class object returns current date
from datetime import datetime #class object returns current time
from datetime import timedelta #class method returns time difference from given date

def display_current_datetime():
    current_date = date.today().isoformat()
    now_time = datetime.now().strftime('%H:%M:%S')

    print(f'Current date and time: {current_date} {now_time}')

def calculate_future_date():
    days = int(input('Enter the number of days to add to the current date: '))
    future_date = date.today() + timedelta(days)

    print(f'Future date: {future_date}')
