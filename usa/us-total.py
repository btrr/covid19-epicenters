# line graph of total cases in the US

import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['1/21/2020', '1/22/2020', '1/23/2020', '1/24/2020', '1/25/2020', '1/26/2020', '1/27/2020', '1/28/2020', '1/29/2020', '1/30/2020', '1/31/2020', '2/1/2020', '2/2/2020', '2/3/2020', '2/4/2020', '2/5/2020', '2/6/2020', '2/7/2020', '2/8/2020', '2/9/2020', '2/10/2020', '2/11/2020', '2/12/2020', '2/13/2020', '2/14/2020', '2/15/2020', '2/16/2020', '2/17/2020', '2/18/2020', '2/19/2020', '2/20/2020', '2/21/2020', '2/22/2020', '2/23/2020', '2/24/2020', '2/25/2020', '2/26/2020', '2/27/2020', '2/28/2020', '2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020']

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

# total cases by day
total_cases = [1, 1, 1, 2, 3, 5, 5, 5, 5, 6, 7, 8, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 15, 15, 15, 15, 15, 15, 35, 35, 35, 53, 57, 60, 60, 63, 68, 75, 100, 124, 158, 221, 310, 435, 541, 704, 994, 1301, 1630, 2183, 2770, 3613, 4596, 6344, 9197, 13779, 19367, 24192, 33592, 43781, 54856, 68211, 85435, 104126]

# text labels
plt.title('Covid-19 Total Confirmed Diagnoses in the USA')
plt.xlabel('Date')
plt.ylabel('Number of Cases')

# create the graph
plt.plot(x_values, total_cases)

plt.show()