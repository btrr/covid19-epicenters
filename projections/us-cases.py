# if cases had continued at same rate as they were on April 4th (when social distancing started to slow the curve)

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['1/21/2020', '1/22/2020', '1/23/2020', '1/24/2020', '1/25/2020', '1/26/2020', '1/27/2020', '1/28/2020', '1/29/2020', '1/30/2020', '1/31/2020', '2/1/2020', '2/2/2020', '2/3/2020', '2/4/2020', '2/5/2020', '2/6/2020', '2/7/2020', '2/8/2020', '2/9/2020', '2/10/2020', '2/11/2020', '2/12/2020', '2/13/2020', '2/14/2020', '2/15/2020', '2/16/2020', '2/17/2020', '2/18/2020', '2/19/2020', '2/20/2020', '2/21/2020', '2/22/2020', '2/23/2020', '2/24/2020', '2/25/2020', '2/26/2020', '2/27/2020', '2/28/2020', '2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020']

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

actual = [1, 1, 1, 2, 3, 5, 5, 5, 5, 6, 7, 8, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 14, 14, 14, 14, 14, 14, 15, 15, 19, 24, 42, 57, 85, 111, 175, 252, 353, 497, 645, 936, 1205, 1598, 2163, 2825, 3501, 4373, 5664, 8074, 12022, 17439, 23710, 32341, 42751, 52690, 64916, 81966, 101012, 121105, 140223, 160686, 186082, 212814, 241626, 273808, 307876, 333593, 362955, 393707, 425746, 459989, 493567, 525436, 553493, 578178, 604165, 633630, 665706]

estimate = [1, 1, 1, 2, 3, 5, 5, 5, 5, 6, 7, 8, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 14, 14, 14, 14, 14, 14, 15, 15, 19, 24, 42, 57, 85, 111, 175, 252, 353, 497, 645, 936, 1205, 1598, 2163, 2825, 3501, 4373, 5664, 8074, 12022, 17439, 23710, 32341, 42751, 52690, 64916, 81966, 101012, 121105, 140223, 160686, 186082, 212814, 241626, 273808, 307876, 346176, 389240, 437662, 492107, 553325, 622158, 699555, 786579, 884430, 994453, 1118163, 1257262]

# create the graph
plt.plot(x_values, actual, color='#730af2', linewidth=2)
plt.plot(x_values, estimate, color='red', linewidth=2)

# text labels
plt.title('Covid-19 in the United States: Actual Cases vs Estimate without Social Distancing')
plt.xlabel('Date')
plt.ylabel('Number of Cases (in thousands)')
plt.legend(['Social Distancing Slowed Increase', 'Actual', 'Estimated'], loc='upper left')

plt.show()