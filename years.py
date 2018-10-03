import time
import datetime

#04/23/2011 @ 12:00am (UTC)
START = 1303516800

days = (int(time.time()) - START) // 1200
date = datetime.datetime(1, 1, 1) + datetime.timedelta(days - 365)
print('%02d/%02d/%s' % (date.day, date.month, date.year))
