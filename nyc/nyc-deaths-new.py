import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020', '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020', '4/26/2020', '4/27/2020', '4/28/2020', '4/29/2020', '4/30/2020', '5/1/2020', '5/2/2020', '5/3/2020', '5/4/2020', '5/5/2020', '5/6/2020', '5/7/2020', '5/8/2020', '5/9/2020', '5/10/2020', '5/11/2020', '5/12/2020', '5/13/2020', '5/14/2020', '5/15/2020', '5/16/2020', '5/17/2020', '5/18/2020', '5/19/2020', '5/20/2020', '5/21/2020', '5/22/2020', '5/23/2020', '5/24/2020', '5/25/2020', '5/26/2020', '5/27/2020', '5/28/2020', '5/29/2020', '5/30/2020', '5/31/2020', '6/1/2020', '6/2/2020', '6/3/2020', '6/4/2020', '6/5/2020', '6/6/2020', '6/7/2020', '6/8/2020', '6/9/2020', '6/10/2020', '6/11/2020', '6/12/2020', '6/13/2020', '6/14/2020', '6/15/2020', '6/16/2020', '6/17/2020', '6/18/2020', '6/19/2020', '6/20/2020', '6/21/2020', '6/22/2020', '6/23/2020', '6/24/2020', '6/25/2020', '6/26/2020', '6/27/2020', '6/28/2020', '6/30/2020', '7/01/2020', '7/02/2020', '7/03/2020', '7/04/2020', '7/05/2020', '7/06/2020', '7/07/2020',
         '7/08/2020', '7/09/2020', '7/10/2020', '7/11/2020', '7/12/2020', '7/13/2020', '7/14/2020', '7/15/2020', '7/16/2020', '7/17/2020', '7/18/2020', '7/19/2020', '7/20/2020', '7/21/2020', '7/22/2020', '7/23/2020', '7/24/2020', '7/25/2020', '7/26/2020', '7/27/2020', '7/28/2020', '7/29/2020', '7/30/2020', '7/31/2020', '8/01/2020', '8/02/2020', '8/03/2020', '8/04/2020', '8/05/2020', '8/06/2020', '8/07/2020', '8/08/2020', '8/09/2020', '8/10/2020', '8/11/2020', '8/12/2020', '8/13/2020', '8/14/2020', '8/15/2020', '8/16/2020', '8/17/2020', '8/18/2020', '8/19/2020', '8/20/2020', '8/21/2020', '8/22/2020', '8/23/2020', '8/24/2020', '8/25/2020', '8/26/2020', '8/27/2020', '8/28/2020', '8/29/2020', '8/30/2020', '8/31/2020', '9/01/2020', '9/02/2020', '9/3/2020', '9/4/2020', '9/5/2020', '9/7/2020', '9/08/2020', '9/09/2020', '9/10/2020', '9/11/2020', '9/12/2020', '9/14/2020', '9/15/2020', '9/16/2020', '9/17/2020', '9/18/2020', '9/19/2020', '9/20/2020', '9/21/2020', '9/22/2020', '9/23/2020', '9/24/2020', '9/25/2020', '9/26/2020', '9/27/2020', '9/28/2020', '9/29/2020', '9/30/2020', '10/01/2020', '10/02/2020', '10/03/2020', '10/04/2020', '10/05/2020', '10/06/2020', '10/07/2020', '10/08/2020', '10/09/2020', '10/10/2020', '10/11/2020', '10/12/2020', '10/13/2020', '10/14/2020', '10/15/2020', '10/16/2020', '10/17/2020', '10/18/2020', '10/19/2020', '10/20/2020', '10/21/2020', '10/22/2020', '10/23/2020', '10/24/2020', '10/25/2020', '10/26/2020', '10/27/2020', '10/28/2020', '10/29/2020', '10/30/2020', '10/31/2020', '11/01/2020', '11/02/2020', '11/03/2020', '11/04/2020', '11/05/2020', '11/06/2020', '11/07/2020', '11/08/2020', '11/09/2020', '11/10/2020', '11/11/2020', '11/12/2020', '11/13/2020', '11/14/2020', '11/15/2020', '11/16/2020', '11/17/2020', '11/18/2020', '11/19/2020', '11/20/2020', '11/21/2020', '11/22/2020', '11/23/2020', '11/24/2020', '11/25/2020', '11/26/2020', '11/27/2020', '11/28/2020', '11/29/2020', '11/30/2020', '12/01/2020', '12/02/2020', '12/03/2020', '12/04/2020', '12/05/2020', '12/06/2020', '12/07/2020', '12/08/2020', '12/09/2020', '12/10/2020', '12/11/2020', '12/12/2020', '12/13/2020', '12/14/2020', '12/15/2020', '12/16/2020', '12/17/2020', '12/18/2020', '12/19/2020', '12/20/2020', '12/21/2020', '12/22/2020', '12/23/2020', '12/24/2020', '12/25/2020', '12/26/2020', '12/27/2020', '12/28/2020', '12/29/2020', '12/30/2020', '12/31/2020', '01/01/2021', '01/02/2021', '01/03/2021', '01/04/2021', '01/05/2021', '01/06/2021', '01/07/2021', '01/08/2021', '01/09/2021', '01/10/2021', '01/11/2021', '01/12/2021', '01/13/2021', '01/14/2021', '01/15/2021', '01/16/2021', '01/17/2021', '01/18/2021', '01/19/2021', '01/20/2021', '01/21/2021', '01/22/2021', '01/23/2021', '01/24/2021', '01/25/2021', '01/26/2021', '01/27/2021', '01/28/2021', '01/29/2021', '01/30/2021', '01/31/2021', '02/01/2021', '02/02/2021', '02/03/2021', '02/04/2021', '02/05/2021', '02/06/2021', '02/07/2021', '02/08/2021', '02/09/2021', '02/10/2021', '02/11/2021', '02/12/2021', '02/13/2021', '02/14/2021', '02/15/2021', '02/16/2021', '02/17/2021', '02/18/2021', '02/19/2021', '02/20/2021', '02/21/2021', '02/22/2021', '02/23/2021', '02/24/2021', '02/25/2021', '02/26/2021', '02/27/2021', '02/28/2021', '03/01/2021', '03/02/2021', '03/03/2021', '03/04/2021', '03/05/2021', '03/06/2021', '03/07/2021', '03/08/2021', '03/09/2021', '03/10/2021', '03/11/2021', '03/12/2021', '03/13/2021', '03/14/2021', '03/15/2021', '03/16/2021', '03/17/2021', '03/18/2021', '03/19/2021', '03/20/2021', '03/24/2021', '03/25/2021', '03/26/2021', '03/27/2021', '03/28/2021', '03/29/2021', '03/30/2021', '03/31/2021', '04/01/2021', '04/02/2021', '04/03/2021', '04/04/2021', '04/05/2021', '04/06/2021', '04/07/2021', '04/08/2021', '04/09/2021', '04/10/2021', '04/11/2021', '04/12/2021', '04/13/2021', '04/14/2021', '04/15/2021', '04/16/2021', '04/17/2021', '04/18/2021', '04/19/2021', '04/20/2021', '04/21/2021', '04/22/2021', '04/23/2021', '04/24/2021', '04/25/2021', '04/26/2021', '04/27/2021', '04/28/2021', '04/29/2021', '04/30/2021', '05/01/2021', '05/02/2021', '05/03/2021', '05/04/2021', '05/05/2021', '05/06/2021', '05/07/2021', '05/08/2021', '05/09/2021', '05/10/2021', '05/11/2021', '05/12/2021', '05/13/2021', '05/14/2021', '05/15/2021', '05/16/2021', '05/17/2021', '05/18/2021', '05/19/2021', '05/20/2021', '05/21/2021', '05/22/2021', '05/23/2021', '05/24/2021', '05/25/2021', '05/26/2021', '05/27/2021', '05/28/2021', '05/29/2021', '05/30/2021', '05/31/2021', '06/01/2021', '06/02/2021', '06/03/2021', '06/04/2021', '06/05/2021', '06/06/2021', '06/07/2021', '06/08/2021', '06/09/2021', '06/10/2021', '06/11/2021', '06/12/2021', '06/13/2021', '06/14/2021', '06/15/2021', '06/16/2021', '06/17/2021', '06/18/2021', '06/19/2021', '06/20/2021', '06/21/2021', '06/22/2021', '06/23/2021', '06/24/2021', '06/25/2021', '06/26/2021', '06/27/2021', '06/28/2021', '06/29/2021', '06/30/2021', '07/01/2021', '07/02/2021', '07/03/2021', '07/04/2021', '07/05/2021']

# format dates
x_values = [datetime.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(
    byweekday=(MO, TU, WE, TH, FR, SA, SU), interval=21))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(
    byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# format y-axis
ax.get_yaxis().set_major_formatter(
    ticker.FuncFormatter(lambda x, pos: format(int(x), ',')))

# new deaths by day
new_deaths = [0, 1, 1, 3, 2, 3, 1, 11, 21, 17, 39, 26, 7, 88, 85, 85, 222, 104, 138, 182, 278, 188, 305, 387, 218, 266, 806, 716, 518, 651, 313, 440, 0, 407, 251, 723, 327, 558, 363, 290, 461, 382, 346, 456, 215, 499, 248, 112, 467, 284, 429, 156, 163, 217, 188, 214, 224, 227, 93, 271, 175, 173, 132, 116, 73, 334, 132, 95, 76, 94, 79, 101, 70, 66, 13, 83, 45, 63, 64, 48, 63, 34, 10, 41, 59, 63, 58, 33, 23, 34, 52, 45, 51, 37, 27, 18, 22,
              32, 20, 39, 17, 33, 40, 21, 28, 30, 38, 26, 21, 692, 5, 22, 16, 20, 28, 13, 15, 7, 19, 16, 14, 3, 38, 12, 14, 20, 4, 13, 5, 11, 13, 3, 33, 0, 13, 13, 10, 6, 9, 11, 8, 4, 5, 12, 6, 4, 1, 6, 5, 7, 4, 6, 4, 9, 8, 2, 5, 4, 1, 4, 0, 4, 7, 3, 8, 4, 1, 7, 7, 3, 0, 8, 5, 3, 3, 7, 7, 10, 8, 0, 1, 17, 4, 4, 7, 3, 8, 4, 0, 3, 3, 0, 0, 7, 6, 2, 4, 7, 5, 4, 5, 14, 1, 4, 5, 4, 11, 2, 4, 2, 1, 4, 7, 7, 6, 4, 6, 10, 8, 0, 2, 5, 9, 3, 3, 1, 6, 4, 11, 4, 2, 8, 5, 8, 13, 8, 8, 6, 12, 5, 4, 8, 2, 2, 14, 11, 4, 4, 15, 26, 12, 11, 9, 7, 5, 8, 6, 11, 7, 0, 9, 5, 8, 10, 15, 25, 11, 9, 18, 3, 10, 29, 21, 18, 22, 4, 46, 25, 47, 23, 12, 33, 22, 32, 43, 41, 29, 30, 33, 41, 40, 37, 49, 26, 25, 25, 26, 37, 54, 41, 43, 63, 54, 58, 67, 81, 57, 70, 55, 63, 49, 71, 85, 61, 70, 69, 68, 47, 72, 67, 87, 89, 80, 90, 64, 53, 67, 77, 94, 100, 68, 65, 105, 70, 89, 39, 124, 59, 67, 67, 107, 103, 68, 80, 51, 64, 72, 80, 83, 77, 64, 62, 76, 94, 83, 67, 62, 62, 48, 38, 59, 85, 61, 62, 65, 59, 51, 47, 65, 59, 44, 216, 60, 48, 54, 68, 102, 0, 58, 58, 59, 63, 57, 50, 33, 51, 59, 51, 43, 54, 55, 34, 50, 60, 48, 52, 29, 25, 33, 23, 42, 39, 44, 32, 8, 49, 27, 51, 34, 47, 27, 27, 30, 35, 33, 32, 29, 27, 27, 16, 37, 35, 0, 35, 31, 21, 20, 15, 16, 21, 13, 11, 17, 12, 13, 12, 12, 13, 7, 2, 14, 9, 14, 17, 9, 17, 4, 12, 5, 7, 12, 11, 6, 4, 6, 1, 5, 4, 3, 2, 3, 2, 2, 2, 5, 4, 7, 5, 1, 0, 7, 4, 0, 5, 2]

# text labels
plt.title('Covid-19 in NYC: New Fatalities')
plt.xlabel('Date')
plt.ylabel('Number of Deaths')

# create the graph
plt.plot(x_values, new_deaths, color='#f22d0a', linewidth=2)

plt.show()
