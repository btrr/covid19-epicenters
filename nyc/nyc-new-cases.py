# line graph of new cases in NYC

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020']

# format dates
x_values = [dt.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
# major tick = every 3 days
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU), interval=5))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# format y-axis
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x/1000), ',')))

# social gatherings > 500 people canceled
plt.axvline(dt.datetime(2020, 3, 10), linestyle='--', color='green', linewidth=2, label='gatherings')
# schools closed
plt.axvline(dt.datetime(2020, 3, 18), linestyle='--', color='orange', linewidth=2, label='schools')
# non-essential businesses closed
plt.axvline(dt.datetime(2020, 3, 20), linestyle='--', color='red', linewidth=2, label='nonessential')
# stay-at-home
plt.axvline(dt.datetime(2020, 3, 22), color='black', linewidth=2, label='stay at home')

# new cases by day
new_cases = [0, 1, 0, 0, 0, 3, 0, 7, 9, 7, 5, 23, 47, 59, 115, 60, 485, 109, 1086, 1606, 2068, 2432, 2649, 2355, 2478, 4414, 3101, 3585, 4033, 2744, 4613, 5052, 4210, 2358]

# text labels
plt.title('Covid-19 in NYC: New Cases')
plt.xlabel('Date')
plt.ylabel('Number of New Cases (in thousands)')
plt.legend(['Ban on Gatherings > 500', 'Schools Closure', 'Non-Essential Businesses Closure', 'Statewide Stay-at-Home Order'], loc='upper left')

# create the graph
plt.plot(x_values, new_cases, color='#730af2', linewidth=2)

plt.show()