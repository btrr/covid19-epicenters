import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020', '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020', '4/26/2020', '4/27/2020', '4/28/2020', '4/29/2020', '4/30/2020', '5/1/2020', '5/2/2020', '5/3/2020', '5/4/2020', '5/5/2020', '5/6/2020', '5/7/2020', '5/8/2020', '5/9/2020', '5/10/2020', '5/11/2020', '5/12/2020', '5/13/2020']

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

# us deaths (minus NY state deaths)
us_deaths = [51.46, 24.64, 38.63, 22.18, 11.82, 20.53, 27.67, 24.34, 22.92, 18.1, 17.73, 12.12, 11.44, 19.95, 16.1, 12.67, 13.84, 10.52, 6.13, 6.3, 11.99, 11.28, 9.23, 7.98, 6.13, 5.4, 5.28, 9.15, 6.69, 5.8, 5.2, 4.6, 2.65, 2.81, 5.54, 6.23, 4.76, 3.88, 3.4, 1.98, 1.56, 5.16, 1.71, 5.83, 3.1, 2.56, 1.43, 1.29, 2.59, 2.84]

# ny state deaths
ny_deaths = [5.17, 35.09, 34.81, 40.27, 32.55, 26.22, 27.26, 25.23, 22.26, 23.68, 21.47, 16.66, 14.4, 15.36, 14.19, 12.75, 10.99, 9.98, 8.79, 7.15, 7.74, 6.94, 5.23, 5.17, 4.21, 3.79, 3.52, 3.28, 3.2, 2.86, 2.68, 2.7, 2.21, 1.99, 1.94, 2.14, 1.7, 1.58, 1.61, 1.48, 1.18, 1.18, 4.85, 1.12, 1.04, 1.07, .97, .75, .95, .77]

# create the graph
plt.plot(x_values, us_deaths, color='#f28706', linewidth=2)
plt.plot(x_values, ny_deaths, color='#C70039', linewidth=2)

# text labels
plt.title('Covid-19 in the United States: New Deaths in US as a Whole (Minus NY State) vs NY State')
plt.xlabel('Date')
plt.ylabel('Percent Increase')
plt.legend(['US Confirmed (Except for NY State)', 'NY State Confirmed'], loc='upper right')

plt.show()