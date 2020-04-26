# if cases had continued at same rate as they were on April 4th (when social distancing started to slow the curve)

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020', '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020']

# format dates
x_values = [dt.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU), interval=3))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# format y-axis
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x/1000))))

# social distancing (by state) started to slow the curve
plt.axvline(dt.datetime(2020, 4, 4), color='black', linewidth=2, label='social distancing')

# American deaths from Vietnam War
plt.axhline(y=58220, color='orange', linestyle='-', linewidth=1, label='vietnam')
# American deaths from WWI
plt.axhline(y=116516, color='#98FB98', linestyle='-', linewidth=1, label='wwi')

actual = [123, 175, 230, 298, 408, 519, 681, 906, 1159, 1592, 2039, 2431, 2985, 3806, 4746, 5821, 7007, 8359, 9534, 10748, 12674, 14610, 16466, 18544, 20453, 21936, 23398, 25776, 28214, 30355, 32435, 34178, 35809, 37455, 40040, 42200, 44198, 46101, 47916]

estimate = [123, 175, 230, 298, 408, 519, 681, 906, 1159, 1592, 2039, 2431, 2985, 3806, 4746, 5821, 7007, 8359, 9971, 11895, 14189, 16927, 20192, 24087, 28733, 34276, 40888, 48775, 58183, 69407, 82796, 98767, 117819, 140546, 167657, 199999, 238578, 284600, 339499]

# create the graph
plt.plot(x_values, actual, color='#0b6cf7', linewidth=2)
plt.plot(x_values, estimate, color='#C70039', linewidth=2)

# text labels
plt.title('Covid-19 in the United States: Actual Deaths vs Estimate without Social Distancing')
plt.xlabel('Date')
plt.ylabel('Number of Deaths (in thousands)')
plt.legend(['Social Distancing Took Hold', 'American Casualties in Vietnam War', 'American Casualties in WWI', 'Actual Deaths', 'Estimated w/o Social Distancing'], loc='upper left')

plt.show()