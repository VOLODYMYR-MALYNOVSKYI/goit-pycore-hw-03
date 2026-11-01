# Завдання 1

from datetime import datetime, timedelta

def get_days_from_today(date):
    try:
        selected_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return "Невірний формат дати. Використовуйте формат 'YYYY-MM-DD'."
    today_date = datetime.now().date()
    return (today_date - selected_date).days

# Приклад використання функції

print(get_days_from_today("2023-01-01"))

# Завдання 2

import random

def get_numbers_ticket(min, max, quantity):
    if min <= 0 or max > 1000 or quantity < 2 or quantity > (max - min)+1:
        return []
    
    return sorted(random.sample(range(min, max + 1), quantity))

# Приклад використання функції

lottery_numbers = get_numbers_ticket(1, 1000, 5)
print("Ваші лотерейні числа:", lottery_numbers)

# Завдання 3

# Номери телефонів для опрацювання

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
# Створення функції для нормалізації номерів телефонів

import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r"[^\d+]", "" , phone_number)
    if cleaned_number.startswith("+"):
        return cleaned_number
    elif cleaned_number.startswith("380"):
        return "+" + cleaned_number
    else:
        return "+38" + cleaned_number

for number in raw_numbers:
    normalized_number = normalize_phone(number)
    print(normalized_number)

# # Завдання 4

# Список працівників з їхніми днями народження

users = [
    {"name": "John Doe", "birthday": "1985.11.04"},
    {"name": "Jane Smith", "birthday": "1990.11.06"}
]
# Створення функції для оповіщення про майбутні дні народження

from datetime import datetime, timedelta


def get_upcoming_birthdays(users = None):
    today = datetime.today().date()
    upcoming_birthdays = []

    if users is None:
        return upcoming_birthdays

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1
            )

        if 0 <= (birthday_this_year - today).days <= 7:
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)

            upcoming_birthdays.append({"name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")}
            )

    return upcoming_birthdays

for birthdays in get_upcoming_birthdays(users):
    print(f"User: {birthdays['name']}, Congratulation Date: {birthdays['congratulation_date']}")


