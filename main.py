from datetime import datetime
import time
try:
    total = int(input("How much data do you want to enter? "))
    today = time.time()
    reminders = []
    for t in range(0, total):
        date = input("Please enter a date: (yyyy-mm-dd) ")
        t = input("Please enter a time: (hh:mm) ")
        print("")
        reminders.append((f'''{date} {t}:00''', f'''({date} - {t})'''))
    print("Thank you very much. I will notify them!")
    print("...")

    reminders2 = {datetime.fromisoformat(
        reminder[0]).timestamp(): reminder[1] for reminder in reminders}

    labels = {
        "1": "First",
        "2": "Second",
        "3": "Third",
        "4": "Fourth",
        "5": "Fifth"
    }
    current = 1
    while len(reminders2) > 0:
        now = time.time()
        for timestamp, reminder_msg in reminders2.items():
            if timestamp < now:

                print(
                    f"""The {labels[str(current)]} date {'has been' if timestamp > today else 'was'} reached! {reminder_msg}""")
                current += 1
                del reminders2[timestamp]
                break
        time.sleep(1)  # in seconds

except Exception as ex:
    print("Error occured", str(ex))
