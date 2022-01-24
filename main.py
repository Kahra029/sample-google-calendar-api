import datetime
from api.calendarApi import CalendarApi
from data.calendarData import CalendarBody, CalendarData

def insert():
    try:
        calendar = CalendarApi()
        calData = CalendarData()
        calContent = CalendarBody()

        now = datetime.datetime.now(datetime.timezone.utc)
        nextWeek = now + datetime.timedelta(days=7)
        calData.year = int(nextWeek.year)
        calData.month = int(nextWeek.month) 
        calData.day = int(nextWeek.day)
        calData.hour = int(18)
        calData.minute = int(00)

        calData.summary = '夕食'
        calData.description = 'さっぱりおろしハンバーグとカキフライ膳を食べるよ'

        body = calContent.createInsertData(calData)
        result = calendar.insert(body)
        calData.eventId = result["id"]
    except Exception as e:
        print(e)

def get():
    calendar = CalendarApi()
    try:
        result = calendar.get()
        if result == []:
            print('No upcoming events found.')
        else:
            for event in result:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])
    except Exception as e:
        print(e)

def delete(eventId):
    try:
        calendar = CalendarApi()
        calendar.delete(eventId)
    except Exception as e:
        print(e)
    