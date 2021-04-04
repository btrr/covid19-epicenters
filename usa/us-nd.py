import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['2/28/2020', '2/29/2020', '3/1/2020', '3/2/2020', '3/3/2020', '3/4/2020', '3/5/2020', '3/6/2020', '3/7/2020', '3/8/2020', '3/9/2020', '3/10/2020', '3/11/2020', '3/12/2020', '3/13/2020', '3/14/2020', '3/15/2020', '3/16/2020', '3/17/2020', '3/18/2020', '3/19/2020', '3/20/2020', '3/21/2020', '3/22/2020', '3/23/2020', '3/24/2020', '3/25/2020', '3/26/2020', '3/27/2020', '3/28/2020', '3/29/2020', '3/30/2020', '3/31/2020', '4/1/2020', '4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020', '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020', '4/26/2020', '4/27/2020', '4/28/2020', '4/29/2020', '4/30/2020', '5/1/2020', '5/2/2020', '5/3/2020', '5/4/2020', '5/5/2020', '5/6/2020', '5/7/2020', '5/8/2020', '5/9/2020', '5/10/2020', '5/11/2020', '5/12/2020', '5/13/2020', '5/14/2020', '5/15/2020', '5/16/2020', '5/17/2020', '5/18/2020', '5/19/2020', '5/20/2020', '5/21/2020', '5/22/2020', '5/23/2020', '5/24/2020', '5/25/2020', '5/26/2020', '5/27/2020', '5/28/2020', '5/29/2020', '5/30/2020', '5/31/2020', '6/1/2020', '6/2/2020', '6/3/2020', '6/4/2020', '6/5/2020', '6/6/2020', '6/7/2020', '6/8/2020', '6/9/2020', '6/10/2020', '6/11/2020', '6/12/2020', '6/13/2020', '6/14/2020', '6/15/2020', '6/16/2020', '6/17/2020', '6/18/2020', '6/19/2020', '6/20/2020', '6/21/2020', '6/22/2020', '6/23/2020', '6/24/2020', '6/25/2020', '6/26/2020', '6/27/2020', '6/28/2020', '6/29/2020', '6/30/2020', '7/01/2020', '7/02/2020',
         '7/03/2020', '7/04/2020', '7/05/2020', '7/06/2020', '7/07/2020', '7/08/2020', '7/09/2020', '7/10/2020', '7/11/2020', '7/12/2020', '7/13/2020', '7/14/2020', '7/15/2020', '7/16/2020', '7/17/2020', '7/18/2020', '7/19/2020', '7/20/2020', '7/21/2020', '7/22/2020', '7/23/2020', '7/24/2020', '7/25/2020', '7/26/2020', '7/27/2020', '7/28/2020', '7/29/2020', '7/30/2020', '7/31/2020', '8/01/2020', '8/02/2020', '8/03/2020', '8/04/2020', '8/05/2020', '8/06/2020', '8/07/2020', '8/08/2020', '8/09/2020', '8/10/2020', '8/11/2020', '8/12/2020', '8/13/2020', '8/14/2020', '8/15/2020', '8/16/2020', '8/17/2020', '8/18/2020', '8/19/2020', '8/20/2020', '8/21/2020', '8/22/2020', '8/23/2020', '8/24/2020', '8/25/2020', '8/26/2020', '8/27/2020', '8/28/2020', '8/29/2020', '8/30/2020', '8/31/2020', '9/01/2020', '9/02/2020', '9/3/2020', '9/4/2020', '9/5/2020', '9/6/2020', '9/7/2020', '9/08/2020', '9/09/2020', '9/10/2020', '9/11/2020', '9/12/2020', '9/13/2020', '9/14/2020', '9/15/2020', '9/16/2020', '9/17/2020', '9/18/2020', '9/19/2020', '9/20/2020', '9/21/2020', '9/22/2020', '9/23/2020', '9/24/2020', '9/25/2020', '9/26/2020', '9/27/2020', '9/28/2020', '9/29/2020', '9/30/2020', '10/01/2020', '10/02/2020', '10/03/2020', '10/04/2020', '10/05/2020', '10/06/2020', '10/07/2020', '10/08/2020', '10/09/2020', '10/10/2020', '10/11/2020', '10/12/2020', '10/13/2020', '10/14/2020', '10/15/2020', '10/16/2020', '10/17/2020', '10/18/2020', '10/19/2020', '10/20/2020', '10/21/2020', '10/22/2020', '10/23/2020', '10/24/2020', '10/25/2020', '10/26/2020', '10/27/2020', '10/28/2020', '10/29/2020', '10/30/2020', '10/31/2020', '11/01/2020', '11/02/2020', '11/03/2020', '11/04/2020', '11/05/2020', '11/06/2020', '11/07/2020', '11/08/2020', '11/09/2020', '11/10/2020', '11/11/2020', '11/12/2020', '11/13/2020', '11/14/2020', '11/15/2020', '11/16/2020', '11/17/2020', '11/18/2020', '11/19/2020', '11/20/2020', '11/21/2020', '11/22/2020', '11/23/2020', '11/24/2020', '11/25/2020', '11/26/2020', '11/27/2020', '11/28/2020', '11/29/2020', '11/30/2020', '12/01/2020', '12/02/2020', '12/03/2020', '12/04/2020', '12/05/2020', '12/06/2020', '12/07/2020', '12/08/2020', '12/09/2020', '12/10/2020', '12/11/2020', '12/12/2020', '12/13/2020', '12/14/2020', '12/15/2020', '12/16/2020', '12/17/2020', '12/18/2020', '12/19/2020', '12/20/2020', '12/21/2020', '12/22/2020', '12/23/2020', '12/24/2020', '12/25/2020', '12/26/2020', '12/27/2020', '12/28/2020', '12/29/2020', '12/30/2020', '12/31/2020', '01/01/2021', '01/02/2021', '01/03/2021', '01/04/2021', '01/05/2021', '01/06/2021', '01/07/2021', '01/08/2021', '01/09/2021', '01/10/2021', '01/11/2021', '01/12/2021', '01/13/2021', '01/14/2021', '01/15/2021', '01/16/2021', '01/17/2021', '01/18/2021', '01/19/2021', '01/20/2021', '01/21/2021', '01/22/2021', '01/23/2021', '01/24/2021', '01/25/2021', '01/26/2021', '01/27/2021', '01/28/2021', '01/29/2021', '01/30/2021', '01/31/2021', '02/01/2021', '02/02/2021', '02/03/2021', '02/04/2021', '02/05/2021', '02/06/2021', '02/07/2021', '02/08/2021', '02/09/2021', '02/10/2021', '02/11/2021', '02/12/2021', '02/13/2021', '02/14/2021', '02/15/2021', '02/16/2021', '02/17/2021', '02/18/2021', '02/19/2021', '02/20/2021', '02/21/2021', '02/22/2021', '02/23/2021', '02/24/2021', '02/25/2021', '02/26/2021', '02/27/2021', '02/28/2021', '03/01/2021', '03/02/2021', '03/03/2021', '03/04/2021', '03/05/2021', '03/06/2021', '03/07/2021', '03/08/2021', '03/09/2021', '03/10/2021', '03/11/2021', '03/12/2021', '03/13/2021', '03/14/2021', '03/15/2021', '03/16/2021', '03/17/2021', '03/18/2021', '03/19/2021', '03/20/2021', '03/21/2021', '03/22/2021', '03/23/2021', '03/24/2021', '03/25/2021', '03/26/2021', '03/27/2021', '03/28/2021', '03/29/2021', '03/30/2021', '03/31/2021', '04/01/2021', '04/02/2021']

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
    ticker.FuncFormatter(lambda x, pos: format(int(x))))

# nationwide lockdown lifted
plt.axvline(dt.datetime(2020, 5, 1), linestyle='--',
            color='black', linewidth=1, label='lift')

# new cases by day
new_deaths = [0, 1, 1, 4, 3, 2, 0, 3, 5, 2, 5, 5, 6, 4, 8, 7, 6, 14, 21, 26, 52, 55, 68, 110, 111, 162, 225, 253, 433, 447, 392, 554, 821, 940, 1075, 1186, 1352, 1175, 1214, 1926, 1936, 1856, 2078, 1909, 1483, 1462, 2378, 2438, 2141, 2080, 1743, 1631, 1646, 2585, 2160, 1998, 1903, 1815, 1197, 1239, 2166, 2549, 2070, 1794, 1668, 1105, 889, 2456, 1729, 2922, 1734, 1516, 945, 840, 1581, 1715, 1868, 1524, 1231, 785, 792, 1425, 1528, 1286, 1262, 1089, 646, 504, 634, 1379, 1216, 1175, 979, 605, 478, 1039, 1004, 909, 849, 723, 450, 491, 926, 861, 812, 758, 654, 345, 384, 739, 742, 694, 682, 550, 283, 292, 766, 688, 644, 599, 506, 250, 338, 613, 670,
              671, 610, 273, 212, 244, 902, 810, 874, 839, 735, 476, 284, 785, 873, 924, 936, 879, 512, 390, 1039, 1103, 1082, 1150, 985, 552, 1079, 1144, 1449, 1231, 1323, 1207, 462, 505, 1265, 1328, 1248, 1287, 1109, 554, 432, 1334, 1486, 1149, 1234, 1190, 616, 400, 1205, 1369, 1122, 1113, 1013, 554, 339, 1145, 1260, 1118, 1009, 1007, 434, 399, 1021, 1016, 1066, 979, 903, 442, 224, 354, 1044, 1134, 1004, 808, 383, 397, 1027, 1007, 852, 902, 716, 311, 309, 826, 1140, 909, 883, 846, 301, 257, 745, 1017, 861, 820, 745, 363, 341, 626, 899, 950, 919, 643, 464, 283, 731, 848, 888, 864, 775, 404, 436, 827, 1131, 966, 908, 865, 366, 435, 906, 1008, 1034, 914, 905, 414, 460, 1090, 1075, 1132, 1160, 1045, 471, 600, 1366, 1462, 1115, 1227, 1281, 661, 656, 1510, 1756, 1956, 1809, 1406, 883, 915, 2019, 2165, 1257, 1316, 1156, 817, 1107, 2388, 2662, 2647, 2436, 2275, 1080, 1331, 2617, 3043, 2787, 2806, 2326, 1410, 1408, 2824, 3331, 3304, 2681, 2644, 1508, 1486, 3037, 3251, 2790, 1397, 1356, 1330, 1509, 3268, 3572, 3171, 2444, 2252, 1370, 1608, 3424, 3670, 3916, 3555, 3437, 2004, 1706, 4013, 3824, 3690, 3531, 3555, 1916, 1345, 2095, 4137, 3865, 3787, 3321, 1910, 1612, 3547, 3907, 3759, 3304, 2823, 1949, 1549, 3275, 3477, 4955, 3399, 2817, 1396, 1283, 2766, 3152, 3735, 5369, 3296, 1282, 1073, 1298, 2256, 2530, 2333, 1968, 1240, 1278, 2165, 2321, 3027, 2024, 1744, 1073, 1208, 1662, 2271, 1680, 2089, 1553, 749, 562, 1623, 1385, 1477, 1626, 746, 509, 649, 1040, 1089, 1494, 1374, 735, 438, 863, 800, 1281, 1236, 1252, 798, 531, 511, 843, 1090, 877, 923]

# text labels
plt.title('Covid-19 in the United States: New Confirmed Deaths')
plt.xlabel('Date')
plt.ylabel('Number of New Deaths')
plt.legend(['Nationwide Stay-at-Home Ends'], loc='upper left')

# create the graph
plt.plot(x_values, new_deaths, color='#f22d0a', linewidth=2)

plt.show()
