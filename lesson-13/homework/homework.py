# tasks.py
import re
import time
import pytz
from datetime import datetime, timedelta

# 1. Age Calculator
name = input("Enter your name: ")
birth = input("Enter your birthdate (YYYY-MM-DD): ")
bd = datetime.strptime(birth, "%Y-%m-%d")
now = datetime.now()
age_days = (now - bd).days
print(f"{name}, you are {age_days // 365} years, {(age_days % 365) // 30} months, and {(age_days % 365) % 30} days old.")

# 2. Days Until Next Birthday
next_bd = bd.replace(year=now.year + (bd.month < now.month or (bd.month == now.month and bd.day <= now.day)))
print(f"Days until your next birthday: {(next_bd - now).days}")

# 3. Meeting Scheduler
curr = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
dur = input("Enter meeting duration (H M): ").split()
end = datetime.strptime(curr, "%Y-%m-%d %H:%M") + timedelta(hours=int(dur[0]), minutes=int(dur[1]))
print(f"Meeting ends at: {end.strftime('%Y-%m-%d %H:%M')}")

# 4. Timezone Converter
dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
from_tz = input("Enter your timezone (e.g., Asia/Tashkent): ")
to_tz = input("Enter target timezone (e.g., US/Eastern): ")
from_zone = pytz.timezone(from_tz)
to_zone = pytz.timezone(to_tz)
dt_obj = from_zone.localize(datetime.strptime(dt_str, "%Y-%m-%d %H:%M"))
converted = dt_obj.astimezone(to_zone)
print(f"Converted time: {converted.strftime('%Y-%m-%d %H:%M')}")

# 5. Countdown Timer
future = input("Enter a future date and time (YYYY-MM-DD HH:MM:SS): ")
ft = datetime.strptime(future, "%Y-%m-%d %H:%M:%S")
print("Countdown (press Ctrl+C to stop):")
try:
    while (left := ft - datetime.now()).total_seconds() > 0:
        print(f"\rTime left: {str(left).split('.')[0]}", end='')
        time.sleep(1)
    print("\nTime's up!")
except KeyboardInterrupt:
    print("\nCountdown stopped.")

# 6. Email Validator
email = input("Enter an email to validate: ")
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Valid email!")
else:
    print("Invalid email.")

# 7. Phone Number Formatter
phone = input("Enter a 10-digit phone number (e.g., 1234567890): ")
formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
print(f"Formatted phone number: {formatted}")

# 8. Password Strength Checker
pw = input("Enter a password: ")
if len(pw) >= 8 and re.search(r"[A-Z]", pw) and re.search(r"[a-z]", pw) and re.search(r"\d", pw):
    print("Strong password!")
else:
    print("Weak password. Make sure it's at least 8 characters and includes uppercase, lowercase, and a number.")

# 9. Word Finder
word = input("Enter word to find: ")
text = input("Enter sample text: ")
positions = [m.start() for m in re.finditer(re.escape(word), text)]
print(f"Found at positions: {positions}" if positions else "Word not found.")

# 10. Date Extractor
user_text = input("Enter text to extract dates (format: YYYY-MM-DD): ")
found_dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', user_text)
print(f"Dates found: {found_dates}" if found_dates else "No dates found.")

