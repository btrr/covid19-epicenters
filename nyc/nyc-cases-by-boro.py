import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020']

# format dates
x_values = [datetime.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU)))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# format y-axis
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x), ',')))

bronx = [8.55, 15.22, 9.8, 7.77, 7.4, 9.22, 9.89, 14.11, 9.64, 4.77, 5.51, 2.83, .32, 4.96, 4.27, 5.37, 3.71, 3.07, 2.18, 2.16]

brooklyn = [8.28, 15.33, 7.57, 6.26, 5.22, 9.77, 6.65, 8.47, 6.14, 4.81, 5.45, 2.09, .53, 3.79, 6.94, 3.9, 3.78, 2.21, 2.11, 1.62]

manhattan = [5.35, 11.14, 6.8, 5.35, 4.76, 5.81, 5.93, 5.74, 6.22, 4.19, 5.66, 2.04, .26, 3.26, 9.52, 2.66, 2.83, 2.13, 1.39, 1.25]

queens = [10.53, 11.92, 8.22, 6.92, 5.98, 7.48, 5.62, 5.93, 7.19, 4.34, 5.49, 2.2, .44, 3.61, 3.99, 3.39, 3.43, 2.9, 2.15, 1.98]

staten = [10.58, 10.45, 7.64, 8.14, 6.15, 12.31, 17.97, 23.44, 11.58, 4.71, 8.78, 2.42, .46, 3.25, 3.74, 3.9, 2.71, 3.62, 2.37, 1.8]


# create the graph
plt.plot(x_values, bronx, color='#fc9403', linewidth=2)
plt.plot(x_values, brooklyn, color='#cefc03', linewidth=2)
plt.plot(x_values, manhattan, color='#2dfc03', linewidth=2)
plt.plot(x_values, queens, color='#5e03fc', linewidth=2)
plt.plot(x_values, staten, color='#ca03fc', linewidth=2)

# text labels
plt.title('Covid-19 in NYC: Confirmed Case Increase Rate by Borough')
plt.xlabel('Date')
plt.ylabel('Percent')
plt.legend(['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island'], loc='upper left')

plt.show()