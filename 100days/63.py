#!/usr/bin/python
# -*- coding: UTF-8 -*-

#生成图片见63.png
from matplotlib import pyplot as plt
from datetime import datetime

dates = []
highs = [64,71,64,59,62,61,57,59,61,59,63,60,57,69,63,59,57,57,61,59,61,61,66]
lows  = [38,36,43,44,31,39,35,31,44,43,45,42,43,37,36,39,40,31,35,31,40,31,33]
datearrs = ['2018-06-01', '2018-06-04', '2018-06-07', '2018-06-10', '2018-06-13', '2018-06-16',
'2018-07-01', '2018-07-04', '2018-07-07', '2018-07-10', '2018-07-13', '2018-07-16',
'2018-08-01', '2018-08-04', '2018-08-07', '2018-08-10', '2018-08-13', '2018-08-16',
'2018-09-01', '2018-09-04', '2018-09-07', '2018-09-10', '2018-09-13'           
]
for row in datearrs:
    current_date = datetime.strptime(row, "%Y-%m-%d")
    dates.append(current_date)

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,highs, c='red')
plt.plot(dates,lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
