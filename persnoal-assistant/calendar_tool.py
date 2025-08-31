import datetime
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request  # Make sure this is imported

SCOPES = ['https://www.googleapis.com/auth/calendar']


def authenticate_google_calendar():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def create_event(summary, start_time_str, end_time_str):
    # Validation
    if not summary or not start_time_str or not end_time_str:
        return "⚠️ Event creation failed: One or more fields are empty."

    try:
        # Debug prints
        print("DEBUG - Summary:", summary)
        print("DEBUG - Start Time:", start_time_str)
        print("DEBUG - End Time:", end_time_str)

        # Parse time to check correctness
        start_dt = datetime.datetime.fromisoformat(start_time_str)
        end_dt = datetime.datetime.fromisoformat(end_time_str)

        if start_dt >= end_dt:
            return "⚠️ Event creation failed: Start time must be before end time."

        service = authenticate_google_calendar()

        event = {
            'summary': summary,
            'start': {
                'dateTime': start_time_str,
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': end_time_str,
                'timeZone': 'Asia/Kolkata',
            },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        return f"✅ Event created: [Open Event]({event.get('htmlLink')})"

    except ValueError:
        return "❌ Invalid date/time format. Use format: YYYY-MM-DDTHH:MM:SS"
    except Exception as e:
        return f"❌ Failed to create event: {str(e)}"


def list_events():
    try:
        service = authenticate_google_calendar()
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC
        events_result = service.events().list(
            calendarId='primary',
            timeMin=now,
            maxResults=5,
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])
        if not events:
            return "📭 No upcoming events found."

        event_list = ""
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            event_list += f"📅 {start} - {event['summary']}\n"
        return event_list

    except Exception as e:
        return f"❌ Failed to fetch events: {str(e)}"
