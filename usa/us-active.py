# line graph of active cases in the US

import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['2/17/2020', '2/18/2020', '2/19/2020', '2/20/2020', '2/21/2020', '2/22/2020', '2/23/2020', '2/24/2020', '2/25/2020', '2/26/2020', '2/27/2020', '2/28/2020', '2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020']

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
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x/1000))))

# active cases by day
active = [12, 12, 12, 10, 29, 29, 28, 48, 51, 54, 54, 57, 60, 65, 85, 106, 138, 200, 289, 401, 504, 663, 949, 1248, 1581, 2126, 2664, 3484, 4434, 6127, 8940, 13464, 18965, 23720, 33000, 42930, 53697, 66790, 82272, 99908]

# text labels
plt.title('Covid-19 Total Active Cases in the USA')
plt.xlabel('Date')
plt.ylabel('Number of Active Cases (in thousands)')

# create the graph
plt.plot(x_values, active, color='#17cb11', linewidth=2)

plt.show()