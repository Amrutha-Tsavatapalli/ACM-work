# main.py

from tools.search_tool import google_search
from tools.reminder_tool import set_reminder, show_reminders
from tools.weather_tool import get_weather
from tools.calendar_tool import create_event, list_events

def main():
    print("🤖 Hello! I'm your Personal Assistant.")

    while True:
        user_input = input("\nHow can I help you? (type 'exit' to quit)\n> ").lower()

        if "exit" in user_input:
            print("👋 Goodbye!")
            break

        elif "search" in user_input:
            query = input("🔍 What do you want to search?\n> ")
            result = google_search(query)
            print(f"🔗 Top Result: {result}")

        elif "weather" in user_input:
            city = input("🏙️ City name?\n> ")
            print(get_weather(city))

        elif "set reminder" in user_input:
            task = input("📌 Reminder task?\n> ")
            time_str = input("⏱️ When? (e.g., 10s, 5m, 1h)\n> ")
            print(set_reminder(task, time_str))

        elif "show reminders" in user_input:
            print("📋 Reminders:")
            print(show_reminders())

        elif "add event" in user_input:
            summary = input("📅 Event title?\n> ")
            start = input("🕒 Start (YYYY-MM-DDTHH:MM:SS)\n> ")
            end = input("🕒 End (YYYY-MM-DDTHH:MM:SS)\n> ")
            print(create_event(summary, start, end))

        elif "view events" in user_input:
            print("📆 Upcoming Events:")
            print(list_events())

        else:
            print("❓ Sorry, I didn’t understand. Try saying:")
            print(" - search")
            print(" - weather")
            print(" - set reminder")
            print(" - show reminders")
            print(" - add event")
            print(" - view events")

if __name__ == "__main__":
    main()
