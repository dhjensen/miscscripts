from datetime import date
from datetime import timedelta

# TODO: Move this to other branch as it's not related to "gmailscript"
# TODO: Add function to tell how long the doctors sick leave is for.

firstsickday = date(year = 2019, month = 10, day = 7)

maxsickdays = timedelta(days = 120)

lastsickday = firstsickday + maxsickdays

print ('Last sick day: ', lastsickday.strftime("%d/%m/%Y"))