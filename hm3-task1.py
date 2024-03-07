from datetime import datetime


def get_count_day(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        diff = current_date - date
        
        return diff.days
    except ValueError:
        return "Використовуйте формат 'РРРР-ММ-ДД'."


date = input("ВВедіть дату використвуйте формат дати 'РРРР-ММ-ДД'.\n")
try:
    print(get_count_day(date))
except ValueError:
    print(f"{date} це не є дата заданого формата")










