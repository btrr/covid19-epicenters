import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020', '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020', '4/26/2020', '4/27/2020', '4/28/2020', '4/29/2020', '4/30/2020', '5/1/2020', '5/2/2020', '5/3/2020', '5/4/2020', '5/5/2020', '5/6/2020', '5/7/2020', '5/8/2020', '5/9/2020', '5/10/2020', '5/11/2020', '5/12/2020', '5/13/2020', '5/14/2020', '5/15/2020', '5/16/2020', '5/17/2020', '5/18/2020', '5/19/2020', '5/20/2020', '5/21/2020', '5/22/2020', '5/23/2020', '5/24/2020', '5/25/2020', '5/26/2020', '5/27/2020', '5/28/2020', '5/29/2020', '5/30/2020', '5/31/2020', '6/1/2020', '6/2/2020', '6/3/2020', '6/4/2020', '6/5/2020', '6/6/2020', '6/7/2020', '6/8/2020', '6/9/2020', '6/10/2020', '6/11/2020', '6/12/2020']

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
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x/100))))

# state started to reopen
plt.axvline(dt.datetime(2020, 4, 24), linestyle='--', color='#FF1493', linewidth=2, label='georgia')

# new cases by day
new_cases = [2, 0, 0, 0, 1, 4, 4, 6, 4, 9, 11, 0, 24, 33, 22, 25, 51, 90, 133, 87, 93, 172, 254, 221, 278, 476, 445, 237, 126, 1308, 521, 710, 483, 552, 264, 667, 1504, 1063, 685, 917, 778, 289, 1071, 957, 682, 1108, 1064, 409, 316, 790, 934, 859, 772, 635, 548, 706, 372, 994, 856, 410, 990, 1110, 469, 409, 549, 1002, 698, 462, 789, 469, 853, 802, 697, 526, 914, 440, 489, 380, 640, 926, 758, 722, 1005, 706, 483, 409, 691, 649, 600, 616, 700, 510, 711, 687, 953, 774, 688, 589, 599, 752, 731, 993, 810]

# text labels
plt.title('Covid-19 in Georgia: New Confirmed Diagnoses')
plt.xlabel('Date')
plt.ylabel('Number of New Cases (in hundreds')
plt.legend(['Lockdown started to lift'], loc='upper left')

# create the graph
plt.plot(x_values, new_cases, color='#730af2', linewidth=2)

plt.show()