# plot of deaths vs recoveries in USA

import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['2/25/2020', '2/26/2020', '2/27/2020', '2/28/2020', '2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020']

# format dates
x_values = [datetime.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
# major tick = every 3 days
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU), interval=4))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# format y-axis
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x), ',')))

# recoveries by day
recoveries = [6, 6, 6, 6, 8, 10, 15, 18, 20, 21, 30, 34, 37, 41, 45, 53, 49, 57, 106, 129, 162, 217, 257, 315, 402, 472, 592, 851, 1159, 1421, 3163, 4218]

# deaths by day
deaths = [0, 0, 0, 0, 1, 2, 6, 9, 12, 12, 18, 19, 22, 26, 31, 38, 42, 49, 56, 62, 75, 96, 122, 174, 229, 296, 408, 519, 681, 906, 1159, 1476]

# create the graph
plt.plot(x_values, recoveries)
plt.plot(x_values, deaths, color='red')

# text labels
plt.title('Covid-19 Recoveries vs Deaths in the USA')
plt.xlabel('Date')
plt.ylabel('Total')
plt.legend(['Total Recoveries', 'Total Deaths'], loc='upper left')

plt.show()