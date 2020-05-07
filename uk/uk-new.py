import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['2/28/2020', '2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020']

# format dates
x_values = [dt.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU), interval=6))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# format y-axis
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x))))

# stay-at-home
plt.axvline(dt.datetime(2020, 3, 23), color='black', linewidth=2, label='stay at home')
# Boris Johnson confirmed to have coronavirus
plt.axvline(dt.datetime(2020, 3, 27), linestyle='--', color='orange', linewidth=2, label='boris')

# new cases by day
new_cases = [6, 4, 12, 5, 11, 34, 29, 46, 46, 65, 50, 52, 83, 134, 207, 264, 330, 152, 407, 676, 643, 714, 1035, 665, 967, 1427, 1452, 2129, 2890, 2556, 2502, 2665, 3250, 4567, 4522, 4672, 4000, 6199, 4143, 3888, 5865, 4675, 5706, 5233, 5288, 4342, 5252, 4603, 4617, 5599, 5525]

# text labels
plt.title('Covid-19 in the UK: New Confirmed Diagnoses')
plt.xlabel('Date')
plt.ylabel('Number of New Cases')
plt.legend(['Nationwide Stay-at-Home Order', 'Boris confirmed to have coronavirus'], loc='upper left')

# create the graph
plt.plot(x_values, new_cases, color='#730af2', linewidth=2)

plt.show()