import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

dates = ['4/2/2020', '4/3/2020', '4/4/2020', '4/5/2020', '4/6/2020', '4/7/2020', '4/8/2020', '4/9/2020', '4/10/2020', '4/11/2020', '4/12/2020', '4/13/2020', '4/14/2020', '4/15/2020', '4/16/2020', '4/17/2020', '4/18/2020', '4/19/2020', '4/20/2020', '4/21/2020', '4/22/2020', '4/23/2020', '4/24/2020', '4/25/2020', '4/26/2020', '4/27/2020', '4/28/2020', '4/29/2020', '4/30/2020', '5/1/2020', '5/2/2020', '5/3/2020', '5/4/2020', '5/5/2020', '5/6/2020', '5/7/2020', '5/8/2020', '5/9/2020', '5/10/2020', '5/11/2020', '5/12/2020', '5/13/2020', '5/14/2020', '5/15/2020', '5/16/2020', '5/17/2020', '5/18/2020', '5/19/2020', '5/20/2020', '5/21/2020', '5/22/2020', '5/23/2020', '5/24/2020', '5/25/2020', '5/26/2020', '5/27/2020', '5/28/2020', '5/29/2020', '5/30/2020', '5/31/2020', '6/1/2020', '6/2/2020', '6/3/2020', '6/4/2020', '6/5/2020', '6/6/2020', '6/7/2020', '6/8/2020', '6/9/2020', '6/10/2020', '6/11/2020', '6/12/2020', '6/13/2020', '6/14/2020', '6/15/2020', '6/16/2020', '6/17/2020', '6/18/2020', '6/19/2020', '6/20/2020', '6/21/2020', '6/22/2020', '6/23/2020', '6/24/2020', '6/25/2020', '6/26/2020', '6/27/2020', '6/28/2020', '6/30/2020', '7/01/2020', '7/02/2020']

# format dates
x_values = [dt.datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%m/%d")
ax.xaxis.set_major_formatter(formatter)

# create x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU), interval=5))
# minor tick = daily
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO, TU, WE, TH, FR, SA, SU)))

# format y-axis
ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(int(x), ',')))

# massive funeral in brooklyn
plt.axvline(dt.datetime(2020, 4, 29), color='black', linestyle='--', linewidth=2, label='funeral')

bronx = [736, 1422, 1055, 918, 942, 1261, 1478, 2317, 1807, 980, 1186, 643, 74, 1161, 1051, 1376, 1002, 859, 630, 637, 988, 781, 951, 1088, 761, 687, 462, 522, 587, 582, 548, 500, 374, 266, 348, 291, 270, 306, 235, 939, 118, 207, 269, 434, 310, 286, 145, 111, 144, 61, 205, 150, 188, 139, 105, 146, 197, 178, 189, 150, 68, 52, 120, 130, 88, 108, 100, 77, 66, 102, 87, 94, 83, 65, 71, 63, 93, 52, 51, 71, 86, 45, 62, 80, 68, 79, 64, 53, 102, 51, 83]

brooklyn = [1016, 2037, 1161, 1032, 914, 1801, 1345, 1828, 1438, 1196, 1420, 573, 148, 1067, 2029, 1220, 1230, 747, 727, 572, 924, 865, 1163, 1185, 681, 734, 417, 636, 616, 625, 682, 564, 474, 296, 502, 440, 398, 425, 434, 2029, 214, 267, 328, 457, 378, 422, 214, 202, 204, 161, 425, 236, 256, 177, 194, 249, 295, 273, 274, 215, 115, 98, 214, 156, 168, 205, 128, 140, 103, 130, 99, 131, 153, 100, 136, 105, 137, 78, 145, 87, 151, 59, 89, 70, 86, 96, 103, 114, 200, 135, 110]

manhattan = [376, 824, 559, 470, 440, 563, 608, 624, 715, 511, 719, 274, 35, 448, 1351, 413, 452, 350, 233, 213, 295, 308, 449, 449, 345, 453, 173, 165, 284, 242, 330, 199, 233, 162, 183, 192, 200, 180, 143, 461, 125, 118, 167, 218, 154, 192, 91, 79, 91, 62, 158, 140, 97, 110, 60, 111, 120, 103, 134, 80, 36, 39, 106, 80, 62, 71, 47, 56, 35, 67, 70, 68, 77, 25, 88, 35, 50, 41, 52, 49, 90, 52, 65, 52, 64, 62, 66, 46, 56, 46, 57]

queens = [1602, 2004, 1548, 1410, 1302, 1726, 1395, 1555, 1995, 1290, 1705, 719, 148, 1215, 1389, 1227, 1286, 1123, 858, 806, 1117, 1187, 1489, 1473, 725, 871, 465, 712, 745, 724, 681, 596, 540, 398, 449, 429, 437, 401, 421, 1339, 180, 279, 281, 406, 305, 404, 182, 165, 253, 156, 285, 149, 199, 190, 140, 182, 251, 191, 214, 175, 66, 95, 216, 115, 151, 177, 97, 144, 99, 123, 121, 128, 148, 78, 112, 108, 159, 101, 94, 82, 192, 80, 107, 80, 102, 121, 73, 111, 122, 89, 99]

staten = [270, 295, 238, 273, 223, 474, 777, 1196, 729, 331, 646, 194, 38, 268, 318, 344, 248, 341, 231, 180, 239, 177, 335, 242, 116, 149, 96, 115, 117, 109, 139, 102, 68, 66, 76, 69, 72, 83, 51, 128, 19, 16, 42, 41, 35, 70, 32, 19, 29, 26, 37, 41, 44, 30, 26, 39, 42, 38, 44, 30, 0, 12, 25, 30, 36, 41, 15, 17, 20, 16, 18, 18, 13, 16, 35, 13, 9, 4, 16, 15, 31, 13, 8, 10, 16, 38, 5, 16, 23, 18, 13]


# create the graph
plt.plot(x_values, bronx, color='#fc9403', linewidth=2)
plt.plot(x_values, brooklyn, color='#cefc03', linewidth=2)
plt.plot(x_values, manhattan, color='#2dfc03', linewidth=2)
plt.plot(x_values, queens, color='#5e03fc', linewidth=2)
plt.plot(x_values, staten, color='#ca03fc', linewidth=2)

# text labels
plt.title('Covid-19 in NYC: Confirmed Cases by Borough')
plt.xlabel('Date')
plt.ylabel('Percent')
plt.legend(['Massive Brooklyn Funeral', 'Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island'], loc='upper left')

plt.show()