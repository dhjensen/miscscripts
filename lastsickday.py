from datetime import date
from datetime import timedelta

firstsickday = date(year = 2019, month = 10, day = 7)

maxsickdays = timedelta(days = 120)

lastsickday = firstsickday + maxsickdays

print ('Last sick day: ', lastsickday.strftime("%d/%m/%Y"))