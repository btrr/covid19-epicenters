import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020', '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020', '4/26/2020', '4/27/2020', '4/28/2020', '4/29/2020', '4/30/2020', '5/1/2020', '5/2/2020', '5/3/2020', '5/4/2020', '5/5/2020', '5/6/2020', '5/7/2020', '5/8/2020', '5/9/2020', '5/10/2020', '5/11/2020', '5/12/2020', '5/13/2020', '5/14/2020', '5/15/2020', '5/16/2020', '5/17/2020']

# format dates
x_values = [dt.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU), interval=5))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# format y-axis
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x), ',')))

# schools closed
plt.axvline(dt.datetime(2020, 3, 18), linestyle='--', color='orange', linewidth=2, label='schools')
# stay-at-home
plt.axvline(dt.datetime(2020, 3, 21), color='black', linewidth=2, label='stay at home')

# new cases by day
new_cases = [0, 1, 1, 1, 0, 1, 1, 2, 4, 2, 2, 10, 7, 10, 44, 27, 81, 55, 114, 94, 152, 76, 172, 349, 299, 327, 337, 313, 427, 585, 605, 767, 894, 427, 675, 671, 341, 469, 585, 434, 422, 308, 334, 422, 561, 454, 300, 476, 372, 345, 330, 363, 314, 375, 227, 139, 147, 195, 164, 220, 144, 211, 97, 178, 60, 89, 100, 95, 125, 99, 63, 59, 30, 15, 51, 115]

# text labels
plt.title('Covid-19 in Bergen County, NJ: New Confirmed Diagnoses')
plt.xlabel('Date')
plt.ylabel('Number of New Cases')
plt.legend(['Schools Closure', 'Non-Essential Businesses Closure', 'Statewide Stay-at-Home Order'], loc='upper left')

# create the graph
plt.plot(x_values, new_cases, color='#730af2', linewidth=2)

plt.show()