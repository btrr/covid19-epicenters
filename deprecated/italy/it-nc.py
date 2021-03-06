import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['1/31/2020', '2/1/2020', '2/2/2020', '2/3/2020', '2/4/2020', '2/5/2020', '2/6/2020', '2/7/2020', '2/8/2020', '2/9/2020', '2/10/2020', '2/11/2020', '2/12/2020', '2/13/2020', '2/14/2020', '2/15/2020', '2/16/2020', '2/17/2020', '2/18/2020', '2/19/2020', '2/20/2020', '2/21/2020', '2/22/2020', '2/23/2020', '2/24/2020', '2/25/2020', '2/26/2020', '2/27/2020', '2/28/2020', '2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020', '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020', '4/26/2020', '4/27/2020', '4/28/2020', '4/29/2020', '4/30/2020', '5/1/2020', '5/2/2020', '5/3/2020', '5/4/2020', '5/5/2020', '5/6/2020', '5/7/2020', '5/8/2020', '5/9/2020', '5/10/2020', '5/11/2020', '5/12/2020', '5/13/2020', '5/14/2020', '5/15/2020']

# format dates
x_values = [dt.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU), interval=6))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# quarantine of red zone
plt.axvline(dt.datetime(2020, 3, 1), linestyle='--', color='red', linewidth=2, label='red zone')
# schools closed
plt.axvline(dt.datetime(2020, 3, 4), linestyle='--', color='orange', linewidth=2, label='schools')
# stay-at-home
plt.axvline(dt.datetime(2020, 3, 21), color='#0b28f7', linewidth=2, label='nonessential')

# format y-axis
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x/1000), ',')))

# new cases by day
new_cases = [2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 58, 78, 72, 94, 147, 185, 234, 239, 573, 335, 466, 587, 769, 778, 1247, 1492, 1797, 977, 2313, 2651, 2547, 3497, 3590, 3233, 3526, 4207, 5322, 5986, 6557, 5560, 4789, 5249, 5210, 6203, 5909, 5974, 5217, 4050, 4053, 4782, 4668, 4585, 4805, 4316, 3599, 3039, 3836, 4204, 3951, 4694, 4092, 3153, 2972, 2667, 3786, 3493, 3491, 3047, 2256, 2729, 3370, 2646, 3021, 2357, 2324, 1739, 2091, 2086, 1872, 1965, 1900, 1389, 1221, 1075, 1444, 1401, 1327, 1083, 802, 744, 1402, 888, 992, 789]

# text labels
plt.title('Covid-19 in Italy: New Confirmed Diagnoses')
plt.xlabel('Date')
plt.ylabel('Number of New Cases (in thousands)')
plt.legend(['Quarantine of Red Zone', 'Nationwide Schools Closure', 'Non-Essential Services Closure'], loc='upper left')

# create the graph
plt.plot(x_values, new_cases, color='#730af2', linewidth=2)

plt.show()