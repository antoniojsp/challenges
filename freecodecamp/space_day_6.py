from datetime import datetime

def moon_phase(date_string):
    start_date = datetime.strptime("2000-01-06", "%Y-%m-%d")
    end_date = datetime.strptime(date_string, "%Y-%m-%d")

    days = (end_date-start_date).days
    day_month = days%28
    rslt = ""
    if 1 < day_month <= 6:
        rslt="New"
    elif 7 <= day_month <= 14:
        rslt="Waxing"
    elif 15 <= day_month <= 21:
        rslt="Full"
    elif 22 <= day_month <= 28:
        rslt="Waning"
    return rslt

print(moon_phase("2000-01-13"))