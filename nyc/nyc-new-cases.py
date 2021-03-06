import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020', '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020', '4/26/2020', '4/27/2020', '4/28/2020', '4/29/2020', '4/30/2020', '5/1/2020', '5/2/2020', '5/3/2020', '5/4/2020', '5/5/2020', '5/6/2020', '5/7/2020', '5/8/2020', '5/9/2020', '5/10/2020', '5/11/2020', '5/12/2020', '5/13/2020', '5/14/2020', '5/15/2020', '5/16/2020', '5/17/2020', '5/18/2020', '5/19/2020', '5/20/2020', '5/21/2020', '5/22/2020', '5/23/2020', '5/24/2020', '5/25/2020', '5/26/2020', '5/27/2020', '5/28/2020', '5/29/2020', '5/30/2020', '5/31/2020', '6/1/2020', '6/2/2020', '6/3/2020', '6/4/2020', '6/5/2020', '6/6/2020', '6/7/2020', '6/8/2020', '6/9/2020', '6/10/2020', '6/11/2020', '6/12/2020', '6/13/2020', '6/14/2020', '6/15/2020', '6/16/2020', '6/17/2020', '6/18/2020', '6/19/2020', '6/20/2020', '6/21/2020', '6/22/2020', '6/23/2020', '6/24/2020', '6/25/2020', '6/26/2020', '6/27/2020', '6/28/2020', '6/30/2020', '7/01/2020', '7/02/2020',
         '7/03/2020', '7/04/2020', '7/05/2020', '7/06/2020', '7/07/2020', '7/08/2020', '7/09/2020', '7/10/2020', '7/11/2020', '7/12/2020', '7/13/2020', '7/14/2020', '7/15/2020', '7/16/2020', '7/17/2020', '7/18/2020', '7/19/2020', '7/20/2020', '7/21/2020', '7/22/2020', '7/23/2020', '7/24/2020', '7/25/2020', '7/26/2020', '7/27/2020', '7/28/2020', '7/29/2020', '7/30/2020', '7/31/2020', '8/01/2020', '8/02/2020', '8/03/2020', '8/04/2020', '8/05/2020', '8/06/2020', '8/07/2020', '8/08/2020', '8/09/2020', '8/10/2020', '8/11/2020', '8/12/2020', '8/13/2020', '8/14/2020', '8/15/2020', '8/16/2020', '8/17/2020', '8/18/2020', '8/19/2020', '8/20/2020', '8/21/2020', '8/22/2020', '8/23/2020', '8/24/2020', '8/25/2020', '8/26/2020', '8/27/2020', '8/28/2020', '8/29/2020', '8/30/2020', '8/31/2020', '9/01/2020', '9/02/2020', '9/3/2020', '9/4/2020', '9/5/2020', '9/7/2020', '9/08/2020', '9/09/2020', '9/10/2020', '9/11/2020', '9/12/2020', '9/14/2020', '9/15/2020', '9/16/2020', '9/17/2020', '9/18/2020', '9/19/2020', '9/20/2020', '9/21/2020', '9/22/2020', '9/23/2020', '9/24/2020', '9/25/2020', '9/26/2020', '9/27/2020', '9/28/2020', '9/29/2020', '9/30/2020', '10/01/2020', '10/02/2020', '10/03/2020', '10/04/2020', '10/05/2020', '10/06/2020', '10/07/2020', '10/08/2020', '10/09/2020', '10/10/2020', '10/11/2020', '10/12/2020', '10/13/2020', '10/14/2020', '10/15/2020', '10/16/2020', '10/17/2020', '10/18/2020', '10/19/2020', '10/20/2020', '10/21/2020', '10/22/2020', '10/23/2020', '10/24/2020', '10/25/2020', '10/26/2020', '10/27/2020', '10/28/2020', '10/29/2020', '10/30/2020', '10/31/2020', '11/01/2020', '11/02/2020', '11/03/2020', '11/04/2020', '11/05/2020', '11/06/2020', '11/07/2020', '11/08/2020', '11/09/2020', '11/10/2020', '11/11/2020', '11/12/2020', '11/13/2020', '11/14/2020', '11/15/2020', '11/16/2020', '11/17/2020', '11/18/2020', '11/19/2020', '11/20/2020', '11/21/2020', '11/22/2020', '11/23/2020', '11/24/2020', '11/25/2020', '11/26/2020', '11/27/2020', '11/28/2020', '11/29/2020', '11/30/2020', '12/01/2020', '12/02/2020', '12/03/2020', '12/04/2020', '12/05/2020', '12/06/2020', '12/07/2020', '12/08/2020', '12/09/2020', '12/10/2020', '12/11/2020', '12/12/2020', '12/13/2020', '12/14/2020', '12/15/2020', '12/16/2020', '12/17/2020', '12/18/2020', '12/19/2020', '12/20/2020', '12/21/2020', '12/22/2020', '12/23/2020', '12/24/2020', '12/25/2020', '12/26/2020', '12/27/2020', '12/28/2020', '12/29/2020', '12/30/2020', '12/31/2020', '01/01/2021', '01/02/2021', '01/03/2021', '01/04/2021', '01/05/2021', '01/06/2021', '01/07/2021', '01/08/2021', '01/09/2021', '01/10/2021', '01/11/2021', '01/12/2021', '01/13/2021', '01/14/2021', '01/15/2021', '01/16/2021', '01/17/2021', '01/18/2021', '01/19/2021', '01/20/2021', '01/21/2021', '01/22/2021', '01/23/2021', '01/24/2021', '01/25/2021', '01/26/2021']

# format dates
x_values = [dt.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(
    byweekday=(MO, TU, WE, TH, FR, SA, SU), interval=14))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(
    byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# format y-axis
ax.get_yaxis().set_major_formatter(
    ticker.FuncFormatter(lambda x, pos: format(int(x/1000), ',')))

# schools closed
plt.axvline(dt.datetime(2020, 3, 18), linestyle='--',
            color='orange', linewidth=2, label='schools')
# non-essential businesses closed
plt.axvline(dt.datetime(2020, 3, 20), linestyle='--',
            color='red', linewidth=2, label='nonessential')
# stay-at-home
plt.axvline(dt.datetime(2020, 3, 22), color='black',
            linewidth=2, label='stay at home')
# massive funeral in brooklyn
plt.axvline(dt.datetime(2020, 4, 29), color='black',
            linestyle='--', linewidth=2, label='funeral')
# reopening, phase 1
plt.axvline(dt.datetime(2020, 6, 8), color='green',
            linewidth=2, label='stay at home')
# schools reopen
plt.axvline(dt.datetime(2020, 9, 21), color='red',
            linewidth=2, label='schools reopen')
# schools close again
plt.axvline(dt.datetime(2020, 11, 19), color='blue',
            linewidth=2, label='schools close')

# new cases by day
new_cases = [0, 1, 0, 0, 0, 3, 0, 7, 9, 7, 5, 23, 47, 59, 115, 60, 485, 109, 1086, 1606, 2068, 2432, 2649, 2355, 2478, 4414, 3101, 3585, 4033, 2744, 4613, 5052, 4210, 2358, 6582, 4561, 4105, 3821, 5825, 5603, 7521, 6684, 4306, 5695, 2403, 450, 4161, 6141, 4583, 4220, 3420, 2679, 2407, 3561, 3319, 4385, 4437, 2628, 2896, 1613, 2152, 2347, 2293, 2378, 1962, 1689, 1189, 1565, 1421, 1377, 1395, 1285, 4896, 657, 887, 1087, 1555, 1183, 1377, 665, 577, 724, 466, 1111, 716, 785, 646, 525, 728, 904, 783, 855, 654, 283, 293, 683, 513, 510, 601, 389, 434, 323, 435, 394, 441, 476, 284, 443, 324, 448, 276, 358, 308,
             550, 249, 331, 292, 338, 385, 321, 340, 503, 340, 362, 438, 349, 291, 209, 310, 199, 382, 313, 333, 326, 275, 269, 366, 396, 332, 333, 264, 319, 552, 98, 361, 152, 531, 94, 217, 424, 313, 314, 288, 309, 199, 192, 318, 346, 287, 403, 241, 321, 210, 272, 364, 429, 330, 224, 489, 221, 181, 261, 305, 203, 217, 284, 189, 171, 183, 236, 311, 233, 229, 225, 291, 248, 324, 222, 304, 230, 212, 196, 478, 216, 290, 420, 336, 253, 275, 327, 634, 188, 320, 284, 209, 379, 386, 401, 343, 367, 395, 486, 466, 579, 609, 530, 439, 473, 587, 421, 652, 680, 473, 352, 416, 502, 438, 555, 545, 486, 523, 390, 718, 436, 481, 968, 343, 367, 568, 561, 314, 1117, 641, 585, 447, 732, 592, 800, 1087, 1151, 646, 52, 1389, 963, 1127, 1154, 1228, 1489, 973, 1552, 1264, 1486, 1420, 1572, 1398, 1642, 1350, 1312, 1959, 1889, 1905, 1282, 2100, 2218, 2384, 2512, 2855, 2498, 2406, 2298, 2715, 2561, 2582, 2643, 3168, 2630, 2367, 3265, 2531, 2539, 3874, 2633, 2256, 2761, 2693, 3199, 3766, 3452, 3222, 2653, 2512, 4029, 3366, 3851, 4800, 5041, 2937, 2892, 3956, 3969, 5077, 5241, 4770, 5045, 4306, 5168, 4508, 4746, 6222, 5018, 4988, 4520, 4509, 3571, 4283, 5127, 4844, 5130, 4086, 3982]

# text labels
plt.title('Covid-19 in NYC: New Cases')
plt.xlabel('Date')
plt.ylabel('Number of New Cases (in thousands)')
plt.legend(['Schools Closure', 'Non-Essential Businesses Closure', 'Statewide Stay-at-Home Order',
            'Massive Funeral Crowd in Brooklyn', 'Reopening, Phase 1', 'Schools Reopen', 'Schools Close'], loc='best')

# create the graph
plt.plot(x_values, new_cases, color='#730af2', linewidth=2)

plt.show()
