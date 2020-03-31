# line graph of daily new cases in Italy

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['1/31/2020', '2/1/2020', '2/2/2020', '2/3/2020', '2/4/2020', '2/5/2020', '2/6/2020', '2/7/2020', '2/8/2020', '2/9/2020', '2/10/2020', '2/11/2020', '2/12/2020', '2/13/2020', '2/14/2020', '2/15/2020', '2/16/2020', '2/17/2020', '2/18/2020', '2/19/2020', '2/20/2020', '2/21/2020', '2/22/2020', '2/23/2020', '2/24/2020', '2/25/2020', '2/26/2020', '2/27/2020', '2/28/2020', '2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020']

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

# quarantine of red zone
plt.axvline(dt.datetime(2020, 3, 1), linestyle='--', color='red', linewidth=2, label='red zone')
# schools closed
plt.axvline(dt.datetime(2020, 3, 4), linestyle='--', color='orange', linewidth=2, label='schools')
# stay-at-home
plt.axvline(dt.datetime(2020, 3, 21), color='#0b28f7', linewidth=2, label='nonessential')

# new cases by day
new_cases = [2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 58, 78, 72, 94, 147, 185, 234, 239, 573, 335, 466, 587, 769, 778, 1247, 1492, 1797, 977, 2313, 2651, 2547, 3497, 3590, 3233, 3526, 4207, 5322, 5986, 6557, 5560, 4789, 5249, 5210, 6203, 5909, 5974, 5217, 4050]

# text labels
plt.title('Covid-19 in Italy: New Confirmed Diagnoses')
plt.xlabel('Date')
plt.ylabel('Number of New Cases')
plt.legend(['Quarantine of Red Zone', 'Nationwide Schools Closure', 'Non-Essential Services Closure'], loc='upper left')

# create the graph
plt.plot(x_values, new_cases, color='#730af2', linewidth=2)

plt.show()