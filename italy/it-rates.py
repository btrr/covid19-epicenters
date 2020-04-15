import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['2/20/2020', '2/21/2020', '2/22/2020', '2/23/2020', '2/24/2020', '2/25/2020', '2/26/2020', '2/27/2020', '2/28/2020', '2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020']

# format dates
x_values = [datetime.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU), interval=5))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# format y-axis
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x), ',')))

# recovery rate
recoveries = [0, 0, 0, 0, .44, 0, .45, 6.46, .11, .35, 1.95, 3.24, .44, 3.76, 3.58, 2.35, 1.12, .45, 1.11, 2.76, .33, 1.41, 1.02, 2.49, 1.49, 1.48, .61, 3.04, 1.01, 1.47, 1.76, 1.61, .64, 1.29, 1.39, 1.24, .68, 1.55, .66, 1.56, 1.05, 1.01, 1.24, 1.24, .99, .64, .77, 1.15, 1.51, 1.38, 1.35, 1.37, 1.07, .77, 1.04]

# mortality rate
deaths = [0, 5, 2.53, 2, 2.62, 3.11, 2.7, 2.62, 2.36, 2.57, 2.01, 2.55, 3.16, 3.46, 3.84, 4.25, 3.96, 4.96, 5.05, 6.22, 6.64, 6.72, 7.17, 6.81, 7.31, 7.71, 7.94, 8.34, 8.3, 8.57, 9.01, 9.26, 9.51, 9.86, 10.09, 10.19, 10.56, 10.84, 11.03, 11.39, 11.75, 11.9, 12.07, 12.25, 12.33, 12.32, 12.47, 12.63, 12.67, 12.73, 12.77, 12.79, 12.73, 12.83, 12.97]

# create the graph
plt.plot(x_values, recoveries, color='#12cfdf', linewidth=2)
plt.plot(x_values, deaths, color='#C70039', linewidth=2)

# text labels
plt.title('Covid-19 in Italy: Recovery Rate vs Mortality Rate')
plt.xlabel('Date')
plt.ylabel('Percent')
plt.legend(['Recovery Rate', 'Mortality Rate'], loc='upper left')

plt.show()