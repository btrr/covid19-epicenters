import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['2/14/2020', '2/15/2020', '2/16/2020', '2/17/2020', '2/18/2020', '2/19/2020', '2/20/2020', '2/21/2020', '2/22/2020', '2/23/2020', '2/24/2020', '2/25/2020', '2/26/2020', '2/27/2020', '2/28/2020', '2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020']

# format dates
x_values = [datetime.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU), interval=4))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# format y-axis
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x), ',')))

# recovery rate
recoveries = [0, 25, 25, 25, 25, 25, 35.71, 35.71, 35.71, 35.71, 35.71, 42.86, 40, 40, 31.58, 29.17, 21.43, 15.79, 10.59, 8.11, 5.14, 5.95, 4.25, 3.02, 2.33, 1.6, 1.24, .94, .74, 1.73, 1.71, 1.72, 1.89, 1.33, .91, .84, .72, .55, .69, .72, .61, 2.27, 2.44, 2.67, 3.25, 3.43, 3.9, 4.17, 4.31, 4.49, 4.82, 5.39, 5.39, 5.51, 5.38, 5.64, 5.53, 5.8]

# mortality rate
deaths = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.17, 4.76, 10.53, 10.59, 9.91, 6.29, 5.56, 5.38, 4.23, 4.03, 3.31, 3.07, 2.57, 2.27, 1.98, 1.77, 1.74, 1.71, 1.52, 1.46, 1.32, 1.26, 1.26, 1.21, 1.29, 1.4, 1.41, 1.58, 1.68, 1.73, 1.86, 2.05, 2.23, 2.41, 2.56, 2.72, 2.86, 2.96, 3.22, 3.43, 3.58, 3.76, 3.89]

# create the graph
plt.plot(x_values, recoveries, color='#12cfdf', linewidth=2)
plt.plot(x_values, deaths, color='#C70039', linewidth=2)

# text labels
plt.title('Covid-19 in the United States: Recovery Rate vs Mortality Rate')
plt.xlabel('Date')
plt.ylabel('Percent')
plt.legend(['Recovery Rate', 'Mortality Rate'], loc='upper right')

plt.show()