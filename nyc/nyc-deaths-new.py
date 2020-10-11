import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020', '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020', '4/26/2020', '4/27/2020', '4/28/2020', '4/29/2020', '4/30/2020', '5/1/2020', '5/2/2020', '5/3/2020', '5/4/2020', '5/5/2020', '5/6/2020', '5/7/2020', '5/8/2020', '5/9/2020', '5/10/2020', '5/11/2020', '5/12/2020', '5/13/2020', '5/14/2020', '5/15/2020', '5/16/2020', '5/17/2020', '5/18/2020', '5/19/2020', '5/20/2020', '5/21/2020', '5/22/2020', '5/23/2020', '5/24/2020', '5/25/2020', '5/26/2020', '5/27/2020', '5/28/2020', '5/29/2020', '5/30/2020', '5/31/2020', '6/1/2020', '6/2/2020', '6/3/2020', '6/4/2020', '6/5/2020', '6/6/2020', '6/7/2020', '6/8/2020', '6/9/2020', '6/10/2020', '6/11/2020', '6/12/2020', '6/13/2020', '6/14/2020', '6/15/2020', '6/16/2020', '6/17/2020', '6/18/2020', '6/19/2020', '6/20/2020', '6/21/2020', '6/22/2020', '6/23/2020', '6/24/2020', '6/25/2020', '6/26/2020', '6/27/2020', '6/28/2020', '6/30/2020', '7/01/2020', '7/02/2020', '7/03/2020', '7/04/2020', '7/05/2020', '7/06/2020', '7/07/2020', '7/08/2020', '7/09/2020', '7/10/2020', '7/11/2020', '7/12/2020', '7/13/2020', '7/14/2020', '7/15/2020', '7/16/2020', '7/17/2020', '7/18/2020', '7/19/2020', '7/20/2020', '7/21/2020', '7/22/2020', '7/23/2020', '7/24/2020', '7/25/2020', '7/26/2020', '7/27/2020', '7/28/2020', '7/29/2020', '7/30/2020', '7/31/2020', '8/01/2020', '8/02/2020', '8/03/2020', '8/04/2020', '8/05/2020', '8/06/2020', '8/07/2020', '8/08/2020', '8/09/2020', '8/10/2020', '8/11/2020', '8/12/2020', '8/13/2020', '8/14/2020', '8/15/2020', '8/16/2020', '8/17/2020', '8/18/2020', '8/19/2020', '8/20/2020', '8/21/2020', '8/22/2020', '8/23/2020', '8/24/2020', '8/25/2020', '8/26/2020', '8/27/2020', '8/28/2020', '8/29/2020', '8/30/2020', '8/31/2020', '9/01/2020', '9/02/2020', '9/3/2020', '9/4/2020', '9/5/2020', '9/7/2020', '9/08/2020', '9/09/2020', '9/10/2020', '9/11/2020', '9/12/2020', '9/14/2020', '9/15/2020', '9/16/2020', '9/17/2020', '9/18/2020', '9/19/2020', '9/20/2020', '9/21/2020', '9/22/2020', '9/23/2020', '9/24/2020', '9/25/2020', '9/26/2020', '9/27/2020', '9/28/2020', '9/29/2020', '9/30/2020', '10/01/2020', '10/02/2020', '10/03/2020', '10/04/2020', '10/05/2020', '10/06/2020', '10/07/2020', '10/08/2020', '10/09/2020', '10/10/2020']

# format dates
x_values = [datetime.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU), interval=14))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# format y-axis
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x), ',')))

# new deaths by day
new_deaths = [0, 1, 1, 3, 2, 3, 1, 11, 21, 17, 39, 26, 7, 88, 85, 85, 222, 104, 138, 182, 278, 188, 305, 387, 218, 266, 806, 716, 518, 651, 313, 440, 0, 407, 251, 723, 327, 558, 363, 290, 461, 382, 346, 456, 215, 499, 248, 112, 467, 284, 429, 156, 163, 217, 188, 214, 224, 227, 93, 271, 175, 173, 132, 116, 73, 334, 132, 95, 76, 94, 79, 101, 70, 66, 13, 83, 45, 63, 64, 48, 63, 34, 10, 41, 59, 63, 58, 33, 23, 34, 52, 45, 51, 37, 27, 18, 22, 32, 20, 39, 17, 33, 40, 21, 28, 30, 38, 26, 21, 692, 5, 22, 16, 20, 28, 13, 15, 7, 19, 16, 14, 3, 38, 12, 14, 20, 4, 13, 5, 11, 13, 3, 33, 0, 13, 13, 10, 6, 9, 11, 8, 4, 5, 12, 6, 4, 1, 6, 5, 7, 4, 6, 4, 9, 8, 2, 5, 4, 1, 4, 0, 4, 7, 3, 8, 4, 1, 7, 7, 3, 0, 8, 5, 3, 3, 7, 7, 10, 8, 0, 1, 17, 4, 4, 7, 3, 8, 4, 0, 3, 3, 0, 0, 7, 6, 2, 4, 7, 5, 4, 5, 14, 1, 4, 5, 4, 11, 2, 4, 2]

# text labels
plt.title('Covid-19 in NYC: New Fatalities')
plt.xlabel('Date')
plt.ylabel('Number of Deaths')

# create the graph
plt.plot(x_values, new_deaths, color='#f22d0a', linewidth=2)

plt.show()