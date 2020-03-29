# plot of deaths vs recoveries in Italy

import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['2/20/2020', '2/21/2020', '2/22/2020', '2/23/2020', '2/24/2020', '2/25/2020', '2/26/2020', '2/27/2020', '2/28/2020', '2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020']

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

# format y-axis
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x), ',')))

# recoveries
recoveries = [0, 2, 4, 5, 8, 13, 15, 62, 67, 79, 124, 201, 239, 383, 562, 720, 822, 988, 1187, 1635, 1872, 2274, 2705, 3407, 4144, 4907, 5444, 7003, 7845, 9161, 10897, 12500, 13509, 15146, 16865, 18576, 20084]

# deaths
deaths = [0, 1, 2, 3, 6, 10, 12, 17, 21, 29, 34, 52, 79, 107, 148, 197, 233, 366, 463, 631, 827, 1016, 1266, 1441, 1809, 2158, 2503, 2978, 3405, 4032, 4825, 5476, 6077, 6820, 7503, 8215, 9134]

# create the graph
plt.plot(x_values, recoveries, color='#12cfdf', linewidth=2)
plt.plot(x_values, deaths, color='#C70039', linewidth=2)

# text labels
plt.title('Covid-19 Recoveries vs Deaths in Italy')
plt.xlabel('Date')
plt.ylabel('Total')
plt.legend(['Total Recoveries', 'Total Deaths'], loc='upper left')

plt.show()