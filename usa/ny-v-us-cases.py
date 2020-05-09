import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020', '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020', '4/26/2020', '4/27/2020', '4/28/2020', '4/29/2020', '4/30/2020', '5/1/2020', '5/2/2020', '5/3/2020', '5/4/2020', '5/5/2020', '5/6/2020', '5/7/2020', '5/8/2020']

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

# us cases (minus NY state cases)
us_cases = [25.32, 23.48, 25.33, 32.68, 38.26, 31.35, 29.19, 28.6, 27.39, 23.54, 26.2, 31.09, 26.1, 22.01, 17.33, 16.7, 17.09, 17.06, 15.6, 14.54, 13.59, 8.96, 9.79, 9.73, 8.46, 8.55, 7.67, 6.79, 5.75, 5.03, 4.91, 4.45, 5.61, 5.31, 4.54, 4.15, 3.91, 4, 4.36, 4.48, 4.69, 3.89, 3.31, 2.6, 3.09, 2.99, 3.41, 3.83, 3.29, 2.7, 2.25, 2.36, 2.47, 2.72, 2.67]

# ny state cases
ny_cases = [18.92, 30.32, 44.63, 73.36, 74.31, 71.05, 45.82, 46.47, 37.63, 22.95, 20.05, 20.92, 19.8, 17.21, 13.75, 11.74, 13.98, 10.45, 10.36, 11.35, 10.54, 7.32, 7.09, 6.23, 7.55, 7.11, 6.61, 5.83, 4.56, 3.36, 3.68, 5.72, 3.98, 3.31, 3.09, 2.56, 1.95, 1.69, 2.2, 2.43, 3.09, 3.89, 2.09, 1.37, 1.07, 1.55, 1.56, 1.3, 1.51, 1.1, .8, .7, .87, 1.08, .9]

# create the graph
plt.plot(x_values, us_cases, color='#12cfdf', linewidth=2)
plt.plot(x_values, ny_cases, color='#1b42f1', linewidth=2)

# text labels
plt.title('Covid-19 in the United States: New Diagnoses in US as a Whole (Minus NY State) vs NY State')
plt.xlabel('Date')
plt.ylabel('Percent Increase')
plt.legend(['US Confirmed (Except for NY State)', 'NY State Confirmed'], loc='upper right')

plt.show()