# -*- coding: utf-8 -*-
import calendar
possible_years = []
c = calendar.Calendar()
for year in range(1, 2017):
    month = c.monthdays2calendar(year, 1)
    for week in month:
        # print week[0]
        if (26, 0) in week:
            if (str(year)[0] == '1' and str(year)[-1] == '6') and (
                        year % 4 == 0 or year % 400 == 0 and not year % 100 == 0):
                possible_years.append(year)
print possible_years
ctext = calendar.TextCalendar()
for year in possible_years:
    pass
    # print ctext.formatmonth(year, 1)
    # print c.monthdays2calendar(year, 1)


#print ctext.formatmonth(1599, 12)
#print ctext.formatmonth(1600, 1)

days_map = {0: "Monday", 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
            4: "Friday", 5: "Saturday", 6: 'Sunday'}

with open(u'D:\Загрузки\pyhon_calendar.txt', 'w') as f:
    for year in range(1,2017):
        f.write(str(year) + ': ' + days_map[(calendar.weekday(year, 1, 1))] + '\n')

print ctext.pryear(1581)