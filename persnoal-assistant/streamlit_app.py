# streamlit_app.py

import streamlit as st
from tools.search_tool import google_search
from tools.weather_tool import get_weather
from tools.reminder_tool import set_reminder, show_reminders
from tools.calendar_tool import create_event, list_events

st.set_page_config(page_title="🧠 Personal Assistant", layout="centered")

st.title("🤖 Personal Assistant Dashboard")

menu = st.sidebar.selectbox("Choose a feature", ["Web Search", "Weather", "Reminders", "Calendar Events"])

if menu == "Web Search":
    st.header("🔍 Google Search")
    query = st.text_input("Enter your query")
    if st.button("Search"):
        result = google_search(query)
        st.write("Top Result:")
        st.write(result)

elif menu == "Weather":
    st.header("🌤️ Check Weather")
    city = st.text_input("City Name")
    if st.button("Get Weather"):
        weather = get_weather(city)
        st.success(weather)

elif menu == "Reminders":
    st.header("⏰ Set a Reminder")
    task = st.text_input("Task")
    time_str = st.text_input("Time (e.g. 10s, 5m, 1h)")
    if st.button("Set Reminder"):
        response = set_reminder(task, time_str)
        st.success(response)

    if st.button("Show Reminders"):
        st.subheader("📋 Current Reminders")
        st.text(show_reminders())

elif menu == "Calendar Events":
    st.header("📅 Google Calendar")
    with st.form("calendar_form"):
        title = st.text_input("Event Title")
        start = st.text_input("Start DateTime (YYYY-MM-DDTHH:MM:SS)")
        end = st.text_input("End DateTime (YYYY-MM-DDTHH:MM:SS)")
        submitted = st.form_submit_button("Create Event")
        if submitted:
            result = create_event(title, start, end)
            st.success(result)

    if st.button("View Events"):
        events = list_events()
        st.subheader("Upcoming Events")
        st.text(events)
