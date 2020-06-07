import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['1/21/2020', '1/22/2020', '1/23/2020', '1/24/2020', '1/25/2020', '1/26/2020', '1/27/2020', '1/28/2020', '1/29/2020', '1/30/2020', '1/31/2020', '2/1/2020', '2/2/2020', '2/3/2020', '2/4/2020', '2/5/2020', '2/6/2020', '2/7/2020', '2/8/2020', '2/9/2020', '2/10/2020', '2/11/2020', '2/12/2020', '2/13/2020', '2/14/2020', '2/15/2020', '2/16/2020', '2/17/2020', '2/18/2020', '2/19/2020', '2/20/2020', '2/21/2020', '2/22/2020', '2/23/2020', '2/24/2020', '2/25/2020', '2/26/2020', '2/27/2020', '2/28/2020', '2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020', '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020', '4/26/2020', '4/27/2020', '4/28/2020', '4/29/2020', '4/30/2020', '5/1/2020', '5/2/2020', '5/3/2020', '5/4/2020', '5/5/2020', '5/6/2020', '5/7/2020', '5/8/2020', '5/9/2020', '5/10/2020', '5/11/2020', '5/12/2020', '5/13/2020', '5/14/2020', '5/15/2020', '5/16/2020', '5/17/2020', '5/18/2020', '5/19/2020', '5/20/2020', '5/21/2020', '5/22/2020', '5/23/2020', '5/24/2020', '5/25/2020', '5/26/2020', '5/27/2020', '5/28/2020', '5/29/2020', '5/30/2020', '5/31/2020', '6/1/2020', '6/2/2020', '6/3/2020', '6/4/2020', '6/5/2020', '6/6/2020']

# format dates
x_values = [dt.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU), interval=6))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# format y-axis
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x/1000))))

# first anti-lockdown protest: Columbus, OH on April 13
plt.axvline(dt.datetime(2020, 4, 13), linestyle='-', color='orange', linewidth=1, label='protest')
# Georgia starts to reopen
plt.axvline(dt.datetime(2020, 4, 24), linestyle='--', color='#FF1493', linewidth=2, label='georgia')
# nationwide lockdown lifted
plt.axvline(dt.datetime(2020, 5, 1), linestyle='--', color='black', linewidth=1, label='lift')
# Wisconsin lockdown lifted
plt.axvline(dt.datetime(2020, 5, 14), linestyle='--', color='pink', linewidth=1, label='lift')

# new cases by day
new_cases = [1, 0, 0, 1, 1, 2, 0, 0, 0, 1, 1, 1, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 4, 5, 18, 15, 28, 26, 64, 77, 101, 144, 148, 291, 269, 393, 565, 662, 676, 872, 1291, 2410, 3948, 5417, 6271, 8631, 10410, 9939, 12226, 17050, 19046, 20093, 19118, 20463, 25396, 26732, 28812, 32182, 34068, 25717, 29362, 30752, 32039, 34243, 33578, 31869, 28057, 24685, 25987, 29465, 32076, 30915, 28274, 26323, 24593, 25304, 29473, 31926, 36229, 34955, 27488, 21464, 24447, 25904, 29674, 33007, 30568, 25375, 21296, 22404, 24420, 27822, 27518, 25158, 20698, 17779, 21475, 20568, 26754, 25382, 24527, 19731, 21107, 19662, 22368, 25017, 23923, 22784, 20286, 18586, 16700, 18677, 23051, 23862, 23581, 21703, 16079, 20073, 19703, 21021, 23324, 23408]

# text labels
plt.title('Covid-19 in the United States: New Confirmed Diagnoses')
plt.xlabel('Date')
plt.ylabel('Number of New Cases (in thousands)')
plt.legend(['First Anti-Lockdown Protest: Columbus, OH', 'Georgia lifted lockdown', 'Nationwide Stay-at-Home Ends', 'Wisconsin lifted lockdown'], loc='upper left')

# create the graph
plt.plot(x_values, new_cases, color='#730af2', linewidth=2)

plt.show()