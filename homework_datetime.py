from datetime import datetime, date, timedelta

date_now = datetime.now()
print(date_now.strftime('%A %d %B %Y'))

delta = timedelta(days=1)
yesterday = date_now - delta
print(yesterday.strftime('%A %d %B %Y'))

delta = timedelta(days=30)
# Как в стандартной поставке Python 3 заменить days=30 на month=1.
month_ago = date_now - delta
print(month_ago.strftime('%A %d %B %Y'))


str = '2015/01/25 12:10:03.234567'
given_time = datetime.strptime(str,'%Y/%m/%d %H:%M:%S.%f')
print(given_time)
