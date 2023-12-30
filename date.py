import datetime
import pytz
import requests
from dateutil import parser

# Fetch current UTC time from an internet source
response = requests.get("http://worldtimeapi.org/api/timezone/etc/UTC")
data = response.json()
utc_time_str = data["utc_datetime"]

# Parse datetime string with dateutil.parser
utc_time = parser.isoparse(utc_time_str)

# Convert UTC time to UTC+5:30
utc_plus_5_30 = pytz.timezone("Asia/Kolkata")
time_plus_5_30 = utc_time.replace(tzinfo=pytz.UTC).astimezone(utc_plus_5_30)
date=time_plus_5_30.strftime("%Y-%m-%d %H:%M:%S")
# Print the current time in UTC+5:30
print(date)