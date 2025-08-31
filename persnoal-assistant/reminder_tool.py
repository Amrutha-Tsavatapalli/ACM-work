import datetime
import pickle
import os

REMINDER_FILE = "reminders.pkl"

def load_reminders():
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "rb") as f:
            return pickle.load(f)
    return []

def save_reminders(reminders):
    with open(REMINDER_FILE, "wb") as f:
        pickle.dump(reminders, f)

def add_reminder(message, time_str):
    try:
        reminder_time = datetime.datetime.fromisoformat(time_str)
        reminders = load_reminders()
        reminders.append({"message": message, "time": time_str})
        save_reminders(reminders)
        return "✅ Reminder added successfully."
    except ValueError:
        return "❌ Invalid datetime format. Use YYYY-MM-DDTHH:MM:SS"

def check_reminders():
    now = datetime.datetime.now()
    reminders = load_reminders()
    due = []

    for reminder in reminders:
        reminder_time = datetime.datetime.fromisoformat(reminder["time"])
        if now >= reminder_time:
            due.append(reminder)

    # Remove due reminders
    reminders = [r for r in reminders if r not in due]
    save_reminders(reminders)

    return due
