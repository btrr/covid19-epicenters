import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['2/28/2020', '2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020', '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020', '4/26/2020', '4/27/2020', '4/28/2020', '4/29/2020', '4/30/2020', '5/1/2020', '5/2/2020', '5/3/2020', '5/4/2020', '5/5/2020', '5/6/2020', '5/7/2020', '5/8/2020', '5/9/2020', '5/10/2020', '5/11/2020', '5/12/2020', '5/13/2020', '5/14/2020', '5/15/2020', '5/16/2020', '5/17/2020', '5/18/2020', '5/19/2020', '5/20/2020', '5/21/2020', '5/22/2020', '5/23/2020', '5/24/2020', '5/25/2020', '5/26/2020', '5/27/2020', '5/28/2020', '5/29/2020', '5/30/2020', '5/31/2020', '6/1/2020', '6/2/2020', '6/3/2020', '6/4/2020', '6/5/2020', '6/6/2020', '6/7/2020', '6/8/2020', '6/9/2020', '6/10/2020', '6/11/2020', '6/12/2020', '6/13/2020', '6/14/2020', '6/15/2020', '6/16/2020', '6/17/2020', '6/18/2020', '6/19/2020', '6/20/2020', '6/21/2020', '6/22/2020', '6/23/2020', '6/24/2020', '6/25/2020', '6/26/2020', '6/27/2020', '6/28/2020', '6/29/2020', '6/30/2020', '7/01/2020', '7/02/2020', '7/03/2020', '7/04/2020', '7/05/2020', '7/06/2020', '7/07/2020', '7/08/2020', '7/09/2020', '7/10/2020', '7/11/2020', '7/12/2020', '7/13/2020', '7/14/2020', '7/15/2020', '7/16/2020', '7/17/2020', '7/18/2020', '7/19/2020', '7/20/2020', '7/21/2020', '7/22/2020', '7/23/2020', '7/24/2020', '7/25/2020', '7/26/2020', '7/27/2020', '7/28/2020', '7/29/2020', '7/30/2020', '7/31/2020', '8/01/2020', '8/02/2020', '8/03/2020', '8/04/2020', '8/05/2020', '8/06/2020', '8/07/2020', '8/08/2020', '8/09/2020', '8/10/2020', '8/11/2020', '8/12/2020', '8/13/2020', '8/14/2020', '8/15/2020', '8/16/2020', '8/17/2020', '8/18/2020', '8/19/2020', '8/20/2020', '8/21/2020', '8/22/2020', '8/23/2020', '8/24/2020', '8/25/2020', '8/26/2020', '8/27/2020', '8/28/2020', '8/29/2020', '8/30/2020', '8/31/2020', '9/01/2020', '9/02/2020']

# format dates
x_values = [dt.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU), interval=10))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# format y-axis
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x))))

# nationwide lockdown lifted
plt.axvline(dt.datetime(2020, 5, 1), linestyle='--', color='black', linewidth=1, label='lift')

# new cases by day
new_deaths = [0, 1, 1, 4, 3, 2, 0, 3, 5, 2, 5, 5, 6, 4, 8, 7, 6, 14, 21, 26, 52, 55, 68, 110, 111, 162, 225, 253, 433, 447, 392, 554, 821, 940, 1075, 1186, 1352, 1175, 1214, 1926, 1936, 1856, 2078, 1909, 1483, 1462, 2378, 2438, 2141, 2080, 1743, 1631, 1646, 2585, 2160, 1998, 1903, 1815, 1197, 1239, 2166, 2549, 2070, 1794, 1668, 1105, 889, 2456, 1729, 2922, 1734, 1516, 945, 840, 1581, 1715, 1868, 1524, 1231, 785, 792, 1425, 1528, 1286, 1262, 1089, 646, 504, 634, 1379, 1216, 1175, 979, 605, 478, 1039, 1004, 909, 849, 723, 450, 491, 926, 861, 812, 758, 654, 345, 384, 739, 742, 694, 682, 550, 283, 292, 766, 688, 644, 599, 506, 250, 338, 613, 670, 671, 610, 273, 212, 244, 902, 810, 874, 839, 735, 476, 284, 785, 873, 924, 936, 879, 512, 390, 1039, 1103, 1082, 1150, 985, 552, 1079, 1144, 1449, 1231, 1323, 1207, 462, 505, 1265, 1328, 1248, 1287, 1109, 554, 432, 1334, 1486, 1149, 1234, 1190, 616, 400, 1205, 1369, 1122, 1113, 1013, 554, 339, 1145, 1260, 1118, 1009, 1007, 434, 399, 1021, 1016]

# text labels
plt.title('Covid-19 in the United States: New Confirmed Deaths')
plt.xlabel('Date')
plt.ylabel('Number of New Deaths')
plt.legend(['Nationwide Stay-at-Home Ends'], loc='upper left')

# create the graph
plt.plot(x_values, new_deaths, color='#f22d0a', linewidth=2)

plt.show()