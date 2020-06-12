import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['2/28/2020', '2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020', '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020', '4/26/2020', '4/27/2020', '4/28/2020', '4/29/2020', '4/30/2020', '5/1/2020', '5/2/2020', '5/3/2020', '5/4/2020', '5/5/2020', '5/6/2020', '5/7/2020', '5/8/2020', '5/9/2020', '5/10/2020', '5/11/2020', '5/12/2020', '5/13/2020', '5/14/2020', '5/15/2020', '5/16/2020', '5/17/2020', '5/18/2020', '5/19/2020', '5/20/2020', '5/21/2020', '5/22/2020', '5/23/2020', '5/24/2020', '5/25/2020', '5/26/2020', '5/27/2020', '5/28/2020', '5/29/2020', '5/30/2020', '5/31/2020', '6/1/2020', '6/2/2020', '6/3/2020', '6/4/2020', '6/5/2020', '6/6/2020', '6/7/2020', '6/8/2020', '6/9/2020', '6/10/2020']

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
new_cases = [6, 4, 12, 5, 11, 34, 29, 46, 46, 65, 50, 52, 83, 134, 207, 264, 330, 152, 407, 676, 643, 714, 1035, 665, 967, 1427, 1452, 2129, 2890, 2556, 2502, 2665, 3250, 4567, 4522, 4672, 4000, 6199, 4143, 3888, 5865, 4675, 5706, 5233, 5288, 4342, 5252, 4603, 4617, 5599, 5525, 5850, 4676, 4301, 4451, 4583, 5386, 4913, 4463, 4309, 3996, 4076, 6032, 6201, 4806, 4339, 3985, 4406, 6111, 5614, 4649, 3896, 3923, 3877, 3403, 3242, 3446, 3560, 3450, 3534, 2711, 1887, 0, 2615, 3287, 2959, 2405, 1625, 2004, 4052, 1887, 2095, 1604, 1936, 1570, 1653, 1871, 1805, 1650, 1557, 1326, 1205, 1741, 1003]

# text labels
plt.title('Covid-19 in the UK: New Confirmed Diagnoses')
plt.xlabel('Date')
plt.ylabel('Number of New Cases')
plt.legend(['Nationwide Stay-at-Home Order', 'Boris confirmed to have coronavirus'], loc='upper left')

# create the graph
plt.plot(x_values, new_cases, color='#730af2', linewidth=2)

plt.show()