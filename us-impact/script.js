// SET UP SVG CONTAINERS

const somData = [
  // ALABAMA
  0,
  0.15908,
  0.819875,
  1.611198,
  3.19792,
  3.19384,
  2.912393,
  2.52081,
  3.732268,
  4.221746,
  4.262535,
  7.081112,
  4.560301,
  7.562431,
  10.854169,
  10.109755,
  13.97255,
  18.32278,
  23.59691,
  25.57113,
  22.02446,
  20.20523,
  16.50764,
  12.21043,
  10.83173,
  11.84332,
  9.51626,
  9.85074,
  10.88272,
  9.64475,
  10.01594,
  11.87799,
  12.62649,
  13.87873,
  15.7571,
  20.04615,
  22.70565,
  // ALASKA
  0.01367,
  0.109358,
  0.820182,
  1.066237,
  1.202934,
  0.88853,
  0.505779,
  0.246055,
  0.259724,
  0.177706,
  0.205045,
  0.314403,
  1.202934,
  1.325961,
  1.339631,
  1.476327,
  2.74761,
  3.48577,
  5.75494,
  6.82118,
  9.37741,
  8.28384,
  6.54779,
  7.61402,
  6.21971,
  6.71182,
  7.57301,
  7.23127,
  7.96943,
  11.15447,
  15.14603,
  18.68648,
  21.44776,
  37.16791,
  37.72837,
  50.27715,
  55.96375,
  // ARIZONA
  0.009617,
  0.048085,
  0.637475,
  1.497517,
  1.950893,
  1.670624,
  2.108888,
  2.581499,
  3.155776,
  3.749287,
  3.628387,
  3.36323,
  6.855604,
  11.692995,
  16.732344,
  26.909962,
  33.515522,
  34.68468,
  30.14542,
  25.18438,
  24.52905,
  17.65284,
  9.81904,
  7.53704,
  5.30176,
  5.23993,
  4.18893,
  6.39948,
  5.75926,
  4.6162,
  5.93649,
  7.42164,
  8.78726,
  11.21489,
  14.7265,
  20.35111,
  30.3886,
  // ARKANSAS
  0.019882,
  0.185565,
  0.904631,
  1.153156,
  1.534228,
  1.570679,
  3.244081,
  2.173766,
  1.358604,
  2.322881,
  3.618525,
  3.578761,
  6.252891,
  7.92298,
  10.312134,
  13.698703,
  13.297749,
  13.17846,
  16.77379,
  17.04882,
  18.22517,
  17.45972,
  15.70016,
  9.93769,
  13.1884,
  14.36806,
  12.33679,
  21.23067,
  19.34519,
  19.12649,
  18.33452,
  20.63421,
  21.85695,
  22.33081,
  27.68901,
  36.74195,
  38.43192,
  // CALIFORNIA
  0.032648,
  0.120722,
  0.596018,
  1.565338,
  2.30764,
  1.992548,
  2.831276,
  2.92264,
  2.96035,
  3.176232,
  3.298473,
  3.922837,
  4.583392,
  4.928601,
  5.521836,
  8.724389,
  11.29372,
  14.24977,
  15.10393,
  17.5738,
  15.15632,
  11.25677,
  15.98518,
  13.06178,
  9.81418,
  8.51585,
  6.50128,
  5.90602,
  6.18517,
  5.83288,
  5.39808,
  5.78808,
  6.42561,
  7.606,
  8.64948,
  11.99831,
  18.67017,
  // COLORADO
  0.08162,
  0.39592,
  2.00218,
  3.99046,
  4.29608,
  4.29435,
  2.66204,
  5.95443,
  5.02714,
  3.94531,
  3.6449,
  3.22119,
  3.62927,
  2.0699,
  2.04559,
  2.52833,
  3.08922,
  2.92599,
  5.45953,
  6.03084,
  6.71849,
  5.50121,
  4.30129,
  3.38616,
  9.92579,
  3.37574,
  3.29586,
  5.14002,
  7.071,
  6.94771,
  8.19798,
  11.47995,
  14.48582,
  22.32087,
  34.80451,
  51.34634,
  59.9576,
  // CONNECTICUT
  0.01683,
  0.42914,
  2.39251,
  7.88716,
  16.71675,
  17.10942,
  20.2396,
  12.90219,
  11.4549,
  10.32175,
  10.50126,
  6.59414,
  4.7121,
  3.42749,
  2.74592,
  1.55387,
  1.82874,
  1.57912,
  1.51741,
  1.35192,
  4.03334,
  1.61277,
  1.50619,
  1.82314,
  2.57483,
  2.40934,
  2.47946,
  3.62664,
  3.04604,
  3.56213,
  4.8832,
  7.83107,
  9.03714,
  14.45886,
  19.40377,
  29.50674,
  35.96905,
  // DELAWARE
  0.04108,
  0.26701,
  1.02694,
  2.70086,
  8.37985,
  8.89333,
  12.66221,
  14.64421,
  12.37466,
  13.18595,
  11.94335,
  8.0615,
  5.90492,
  3.69699,
  4.03589,
  4.9396,
  7.71234,
  8.21554,
  5.98708,
  8.31824,
  7.85611,
  6.94213,
  6.1822,
  7.71234,
  2.64951,
  6.9524,
  8.34905,
  8.74955,
  6.45947,
  8.62632,
  9.13979,
  9.21168,
  9.88946,
  10.92667,
  13.18595,
  20.34374,
  28.7544,
  // FLORIDA
  0.01909,
  0.18065,
  0.95494,
  3.03803,
  3.64005,
  3.03291,
  2.93699,
  1.88195,
  2.39224,
  2.04025,
  2.5445,
  2.14641,
  3.2117,
  4.13731,
  7.84859,
  13.07959,
  25.64888,
  29.61765,
  38.67121,
  34.49758,
  33.29541,
  22.81898,
  21.76579,
  14.65005,
  10.88988,
  11.6502,
  8.24947,
  9.18393,
  8.65268,
  7.498,
  7.96965,
  9.08662,
  10.86846,
  11.1413,
  17.18803,
  17.65875,
  24.61433,
  // GEORGIA
  0.03767,
  0.23075,
  1.16601,
  3.60069,
  4.91456,
  5.4646,
  4.84487,
  4.2581,
  4.92304,
  4.33062,
  4.28258,
  4.39372,
  4.49921,
  4.82791,
  5.59364,
  9.59084,
  15.64786,
  17.91207,
  23.12049,
  23.841,
  24.20361,
  21.29424,
  22.39056,
  17.02202,
  15.38321,
  13.38743,
  11.14677,
  11.09497,
  9.55317,
  7.80604,
  7.90964,
  8.30522,
  9.33277,
  9.85738,
  11.1901,
  11.67797,
  15.91912,
  // HAWAII
  0.01413,
  0.16951,
  0.56502,
  1.26424,
  1.10886,
  0.69922,
  0.38845,
  0.15538,
  0.07769,
  0.0565,
  0.07063,
  0,
  0.0565,
  0.26132,
  0.49439,
  0.62859,
  0.67096,
  1.29955,
  1.27836,
  1.26424,
  3.52433,
  6.53308,
  9.87377,
  10.82019,
  12.16212,
  11.55472,
  7.69844,
  5.74204,
  4.76032,
  5.19821,
  4.93689,
  3.90572,
  4.31536,
  3.80684,
  4.8592,
  5.09227,
  3.7009,
  // IDAHO
  0,
  0.1287,
  0.90651,
  3.95061,
  2.58524,
  1.43252,
  1.27024,
  1.00164,
  0.91211,
  0.96807,
  1.02403,
  1.31501,
  1.59479,
  1.38775,
  2.46773,
  6.27845,
  9.66949,
  15.864,
  20.73232,
  20.16155,
  19.64114,
  17.64345,
  18.08552,
  13.92786,
  11.20273,
  10.10036,
  9.45685,
  10.47528,
  15.36038,
  18.61712,
  21.5437,
  25.83006,
  33.40114,
  34.34122,
  39.72435,
  49.74078,
  55.76742,
  // ILLINOIS
  0.02131,
  0.30777,
  1.66985,
  4.06966,
  6.88693,
  7.3478,
  8.8393,
  12.61381,
  14.16923,
  13.4661,
  11.63921,
  10.37499,
  7.04398,
  4.61181,
  3.29471,
  3.67429,
  4.2993,
  4.394,
  5.91864,
  7.08264,
  7.86864,
  9.09735,
  9.4722,
  10.49099,
  10.74273,
  9.99777,
  12.34235,
  9.91491,
  10.3884,
  11.10259,
  12.52543,
  17.87904,
  21.985,
  30.27821,
  49.8263,
  68.1962,
  65.05616,
  // INDIANA
  0.01782,
  0.09952,
  0.84073,
  3.55603,
  4.91963,
  4.73989,
  5.19442,
  7.12395,
  6.93382,
  5.27315,
  5.76779,
  4.65226,
  4.49777,
  3.93927,
  3.99571,
  3.29312,
  4.0581,
  4.73544,
  6.6917,
  8.20235,
  8.39396,
  8.55884,
  9.72933,
  8.48457,
  10.73494,
  9.43225,
  8.00479,
  9.51098,
  8.30335,
  10.30864,
  13.1502,
  17.8277,
  21.11934,
  27.00447,
  37.03088,
  53.09096,
  67.95085,
  // IOWA
  0.05071,
  0.08875,
  0.42788,
  1.37873,
  2.07919,
  2.76064,
  5.65122,
  10.20897,
  12.40543,
  8.29142,
  7.22646,
  8.33579,
  6.72251,
  6.57672,
  6.19955,
  7.48953,
  9.60993,
  8.63372,
  12.0029,
  12.34838,
  10.65587,
  10.26919,
  10.00295,
  11.60672,
  18.20245,
  23.50503,
  15.95527,
  15.67953,
  20.28164,
  20.17388,
  20.35137,
  23.36874,
  25.15,
  38.22736,
  63.09527,
  101.18951,
  86.4545,
  // KANSAS
  0.01716,
  0.09954,
  0.45996,
  1.31809,
  1.90161,
  1.65447,
  3.06867,
  6.0275,
  6.54238,
  4.54465,
  3.67623,
  2.73915,
  2.85929,
  2.20368,
  2.98286,
  4.42451,
  6.93368,
  9.01722,
  11.37879,
  10.88451,
  9.49434,
  9.77238,
  9.71402,
  11.4749,
  13.8914,
  13.74037,
  11.91083,
  11.87651,
  14.95204,
  15.52527,
  16.1191,
  17.32735,
  18.44978,
  30.72446,
  42.7417,
  61.35281,
  65.30707,
  // KENTUCKY
  0.02462,
  0.06491,
  0.46557,
  1.16839,
  1.52652,
  2.18682,
  2.35469,
  2.7464,
  3.17839,
  2.45542,
  2.12639,
  1.90927,
  3.24778,
  2.59195,
  2.70611,
  2.99037,
  2.96799,
  4.43855,
  5.88002,
  8.42497,
  8.58165,
  7.67737,
  8.70699,
  7.69752,
  8.26829,
  8.94649,
  6.78653,
  8.25709,
  8.32872,
  9.55083,
  13.40295,
  11.83838,
  14.21545,
  20.67519,
  21.54589,
  27.08121,
  34.89065,
  // LOUISIANA
  0.04087,
  0.80236,
  4.11505,
  14.72425,
  19.64596,
  9.14,
  6.89856,
  4.86578,
  5.70255,
  6.10266,
  6.48555,
  4.94322,
  5.93702,
  6.25969,
  8.95286,
  10.28439,
  17.52282,
  22.44238,
  31.01234,
  32.78054,
  27.60071,
  27.45873,
  17.62393,
  11.5772,
  10.35968,
  10.78559,
  10.25642,
  8.35701,
  8.42799,
  7.23198,
  7.47936,
  8.08812,
  9.10344,
  7.31372,
  9.5186,
  17.18725,
  26.56173,
  // MAINE
  0.00744,
  0.3794,
  0.76625,
  1.64409,
  1.36883,
  1.75568,
  1.04894,
  1.17541,
  1.01175,
  1.29444,
  2.03093,
  2.03093,
  1.71104,
  1.48042,
  1.30188,
  1.30932,
  1.63665,
  1.04894,
  0.85552,
  0.94479,
  1.06382,
  0.78113,
  0.72161,
  0.98943,
  1.10846,
  1.36883,
  1.05638,
  1.27212,
  1.62921,
  1.39859,
  1.30188,
  1.2498,
  1.48042,
  2.87901,
  5.47533,
  8.8007,
  8.81557,
  // MARYLAND
  0.01489,
  0.15714,
  0.78238,
  2.89628,
  6.3748,
  7.60708,
  8.19263,
  9.93271,
  12.62389,
  10.79945,
  12.61727,
  10.21887,
  10.1709,
  7.17703,
  5.01515,
  4.21458,
  4.37668,
  5.00192,
  6.97523,
  8.55487,
  10.48848,
  9.63994,
  8.52675,
  6.73043,
  6.34172,
  6.53194,
  6.72546,
  7.34574,
  5.42702,
  6.13661,
  6.51209,
  6.89749,
  7.21507,
  9.30086,
  11.89444,
  16.97741,
  25.33545,
  // MASSACHUSETTS
  0.15234,
  0.31919,
  3.03083,
  9.50163,
  14.47225,
  19.20928,
  20.08269,
  23.47768,
  16.70801,
  12.27566,
  11.46463,
  6.98005,
  5.05041,
  3.08741,
  1.9572,
  1.55096,
  1.58723,
  1.62786,
  1.64382,
  2.0486,
  2.49111,
  3.09467,
  2.87849,
  2.60138,
  3.10482,
  3.43707,
  2.81465,
  3.45303,
  3.95212,
  5.22016,
  5.50888,
  6.2996,
  8.04062,
  12.0914,
  13.79325,
  21.60463,
  24.24518,
  // MICHIGAN
  0.01202,
  0.32242,
  2.52532,
  7.94544,
  10.7271,
  7.76921,
  6.03593,
  6.09601,
  4.27262,
  3.94118,
  3.93317,
  2.5073,
  2.22993,
  1.25665,
  1.12348,
  1.69022,
  2.37212,
  3.01196,
  4.16447,
  4.1104,
  4.9465,
  4.54798,
  4.96953,
  4.31067,
  5.26792,
  4.44284,
  5.13074,
  5.17981,
  4.91146,
  5.98887,
  6.78492,
  9.98512,
  11.59724,
  19.72593,
  27.21677,
  43.22882,
  50.50238,
  // MINNESOTA
  0.01596,
  0.14185,
  0.4557,
  0.70217,
  0.88658,
  1.18802,
  1.82636,
  3.89032,
  7.49872,
  7.21678,
  8.44913,
  8.41722,
  5.89755,
  5.39574,
  4.1829,
  4.34071,
  5.47376,
  5.23616,
  7.41892,
  7.75583,
  8.8144,
  8.77362,
  7.71859,
  7.65121,
  9.01123,
  10.16556,
  7.31608,
  7.93137,
  11.15321,
  12.74551,
  14.08957,
  17.43553,
  18.38063,
  27.21986,
  43.20849,
  63.58216,
  84.45232,
  // MISSISSIPPI
  0.00336,
  0.16464,
  1.46162,
  2.32515,
  3.63893,
  4.5831,
  5.13751,
  5.5844,
  6.28665,
  6.038,
  5.84312,
  7.2241,
  7.35178,
  6.46137,
  7.25098,
  13.02018,
  14.29364,
  16.19879,
  20.85245,
  27.74055,
  32.00781,
  22.91888,
  18.76922,
  18.35594,
  17.62681,
  14.85477,
  10.77231,
  12.13985,
  11.34016,
  12.01553,
  13.85347,
  18.7289,
  15.52678,
  18.34586,
  18.54074,
  23.91009,
  28.42264,
  // MISSOURI
  0.00326,
  0.04236,
  0.77231,
  2.17029,
  2.77804,
  2.56133,
  1.97151,
  2.02202,
  2.89861,
  1.59024,
  1.66682,
  2.17192,
  2.25502,
  2.17192,
  2.47335,
  4.09455,
  4.66319,
  6.05465,
  7.2066,
  11.85839,
  18.14115,
  12.29994,
  12.07998,
  12.9305,
  12.77571,
  14.72278,
  14.63317,
  17.50407,
  16.256,
  15.64336,
  15.91383,
  21.84466,
  19.49188,
  25.52535,
  33.08715,
  47.03762,
  53.86621,
  // MONTANA
  0.00936,
  0.14035,
  0.51461,
  1.5906,
  1.05728,
  0.57075,
  0.25262,
  0.10292,
  0.02807,
  0.05614,
  0.15906,
  0.05614,
  0.50525,
  0.22456,
  0.8608,
  1.38476,
  2.61981,
  3.58353,
  7.15771,
  6.35305,
  8.45826,
  7.37291,
  7.53197,
  6.22206,
  8.0185,
  8.8138,
  7.41033,
  9.20678,
  14.92359,
  21.12693,
  33.15937,
  39.25979,
  45.9216,
  50.64663,
  56.42893,
  58.91775,
  84.66679,
  // NEBRASKA
  0.0517,
  0.11373,
  0.21195,
  0.89433,
  1.71112,
  2.52791,
  5.46937,
  11.1507,
  15.03819,
  11.5074,
  10.38561,
  9.49128,
  9.59467,
  6.19311,
  5.68649,
  4.81284,
  5.71751,
  6.05353,
  7.81118,
  8.70551,
  10.07026,
  10.62341,
  9.50678,
  8.72618,
  9.0622,
  12.24147,
  9.8428,
  10.57688,
  17.12152,
  17.85559,
  15.93252,
  28.79434,
  29.96266,
  36.88467,
  57.11308,
  73.55739,
  86.53293,
  // NEVADA
  0.01299,
  0.29219,
  1.05514,
  3.36996,
  3.2401,
  2.8083,
  2.87972,
  2.56481,
  2.49338,
  2.37975,
  2.45442,
  3.094,
  2.86349,
  4.24978,
  5.44453,
  9.03526,
  15.82387,
  16.78811,
  22.76183,
  25.9857,
  22.4177,
  21.85928,
  16.53488,
  16.01867,
  11.8046,
  9.74951,
  7.54183,
  6.65226,
  8.44762,
  10.43129,
  11.07411,
  13.28504,
  16.17126,
  19.86912,
  23.16766,
  31.86527,
  42.13098,
  // NEW HAMPSHIRE
  0.02942,
  0.27947,
  0.83841,
  2.3608,
  2.50053,
  2.88297,
  3.37572,
  3.50074,
  5.12609,
  3.96408,
  4.06704,
  3.31688,
  3.60371,
  2.44905,
  1.77244,
  1.38265,
  1.35323,
  1.11053,
  1.22085,
  1.31646,
  1.66212,
  1.45619,
  1.31646,
  0.94873,
  1.05905,
  1.12524,
  1.66212,
  1.77244,
  1.69154,
  2.00778,
  3.20656,
  4.00085,
  4.39799,
  5.67768,
  8.29588,
  14.09858,
  21.09272,
  // NEW JERSEY
  0.0304,
  0.80273,
  6.90595,
  21.06913,
  28.63821,
  27.34686,
  27.77693,
  21.01171,
  16.86859,
  10.21032,
  9.87144,
  7.14126,
  5.30838,
  3.69954,
  2.57932,
  2.3519,
  2.43183,
  2.1211,
  2.54554,
  1.56043,
  3.47099,
  3.07469,
  3.25708,
  2.17627,
  2.34852,
  2.657,
  2.7482,
  3.31788,
  3.59258,
  4.8828,
  6.06157,
  6.51979,
  8.58572,
  12.48904,
  14.98167,
  23.13956,
  30.38327,
  // NEW MEXICO
  0.02861,
  0.1383,
  0.48168,
  1.27335,
  2.7947,
  2.89962,
  3.72944,
  4.92172,
  5.16017,
  4.8168,
  4.62126,
  4.25404,
  4.71665,
  4.83587,
  3.74852,
  4.9551,
  6.33337,
  8.25532,
  8.9993,
  9.65744,
  10.61126,
  6.60521,
  5.78969,
  4.59742,
  4.62126,
  4.25404,
  2.94254,
  3.67221,
  4.88833,
  6.85321,
  10.68757,
  16.83018,
  20.97453,
  27.37944,
  30.92765,
  45.84065,
  71.97535,
  // NEW YORK
  0.1573,
  1.96571,
  17.01796,
  28.33569,
  34.7268,
  32.04915,
  21.1663,
  21.0306,
  11.87289,
  8.00984,
  6.8918,
  5.28181,
  4.31798,
  2.96038,
  2.50237,
  2.39288,
  2.33325,
  2.34353,
  2.7049,
  2.53013,
  2.40213,
  2.34302,
  2.31937,
  2.24278,
  2.22479,
  2.55789,
  2.46947,
  2.75065,
  2.87094,
  3.6929,
  5.17589,
  4.83767,
  5.48177,
  7.02185,
  8.528,
  14.98029,
  17.31662,
  // NORTH CAROLINA
  0.01335,
  0.07818,
  0.51392,
  1.16418,
  1.71051,
  1.72958,
  2.04327,
  2.766,
  2.7536,
  2.96527,
  4.15042,
  4.34016,
  6.249,
  7.16527,
  8.3018,
  8.5764,
  10.449,
  10.68546,
  13.4219,
  12.84029,
  12.68201,
  10.5577,
  9.11225,
  8.65744,
  10.65209,
  10.6149,
  8.14734,
  8.41145,
  8.21218,
  9.15324,
  11.02966,
  12.17286,
  12.02698,
  13.69459,
  14.37918,
  14.31339,
  19.99412,
  // NORTH DAKOTA
  0.01312,
  0.2362,
  0.43304,
  1.40409,
  1.44345,
  1.62716,
  4.14664,
  4.69778,
  3.98918,
  4.4747,
  6.78422,
  3.30682,
  2.95252,
  3.59551,
  2.79505,
  2.62446,
  3.46429,
  5.41951,
  7.84713,
  10.82589,
  10.60281,
  11.49513,
  13.04356,
  14.05397,
  20.44453,
  24.00067,
  23.80384,
  29.91883,
  35.79761,
  36.30938,
  43.90719,
  58.7485,
  71.14907,
  85.87228,
  119.66218,
  118.10063,
  123.53326,
  // OHIO
  0.00428,
  0.09753,
  0.63991,
  1.74094,
  2.23285,
  2.33294,
  5.05,
  2.68883,
  3.2911,
  3.13797,
  2.88645,
  2.95232,
  2.57847,
  2.12249,
  2.44074,
  3.63415,
  5.39135,
  5.97394,
  7.72857,
  7.93816,
  7.73627,
  6.34009,
  6.48724,
  5.31008,
  5.49743,
  6.82858,
  5.67623,
  5.89866,
  4.81731,
  5.82252,
  7.42829,
  9.57644,
  12.14379,
  16.18003,
  22.25492,
  34.68359,
  43.47041,
  // OKLAHOMA
  0.00758,
  0.10867,
  0.51049,
  1.59465,
  2.03438,
  1.7008,
  1.66794,
  1.51884,
  1.79936,
  1.59718,
  1.81452,
  1.49104,
  1.60982,
  1.81705,
  4.36698,
  6.55552,
  6.54794,
  10.00007,
  12.49693,
  11.4431,
  19.63876,
  14.3064,
  11.88283,
  11.53913,
  12.33519,
  13.8414,
  14.33672,
  16.72491,
  20.03047,
  18.0062,
  19.02718,
  20.77347,
  21.60238,
  19.30517,
  25.91882,
  39.44179,
  50.29857,
  // OREGON
  0.04979,
  0.15174,
  0.54057,
  1.20918,
  1.17362,
  0.98394,
  0.92704,
  0.90807,
  1.13568,
  1.16176,
  0.80138,
  0.63778,
  0.91992,
  1.80903,
  2.67679,
  2.84987,
  4.09224,
  4.49056,
  5.50295,
  5.22555,
  5.73293,
  4.96475,
  4.9197,
  4.4218,
  3.78402,
  3.73423,
  3.1249,
  3.33354,
  4.27955,
  4.73477,
  5.60253,
  5.71159,
  5.72108,
  7.21003,
  10.00299,
  15.00568,
  17.16086,
  // PENNSYLVANIA
  0.01718,
  0.12732,
  1.17326,
  4.16263,
  8.75801,
  7.42619,
  7.27856,
  6.80363,
  5.58663,
  5.24997,
  4.49618,
  2.11842,
  2.95032,
  2.52929,
  2.21059,
  2.67537,
  3.27996,
  3.61584,
  4.24153,
  4.5118,
  5.11639,
  4.1267,
  4.2884,
  3.61897,
  3.17607,
  4.25246,
  3.85018,
  4.49071,
  3.98844,
  4.81488,
  5.79207,
  6.91143,
  8.01985,
  10.55149,
  12.74333,
  21.0108,
  29.13532,
  // RHODE ISLAND
  0.02832,
  0.36815,
  1.1422,
  4.64431,
  10.10043,
  19.92711,
  22.82508,
  22.32478,
  18.0203,
  14.02732,
  14.67866,
  8.7128,
  7.84435,
  5.06909,
  3.84194,
  3.50211,
  2.84134,
  2.85078,
  4.41776,
  4.12513,
  7.5706,
  6.23961,
  5.93754,
  5.95642,
  6.77767,
  5.22957,
  6.03194,
  6.66439,
  7.76883,
  5.69211,
  11.4975,
  12.18719,
  22.91004,
  26.01568,
  33.09542,
  48.60477,
  61.09343,
  // SOUTH CAROLINA
  0.02331,
  0.13401,
  0.00583,
  2.13257,
  2.40448,
  2.2122,
  1.91504,
  2.28795,
  2.03352,
  2.03352,
  2.31126,
  2.73661,
  4.30593,
  6.67351,
  9.88985,
  14.42885,
  20.63622,
  21.28881,
  25.89384,
  24.15166,
  20.98,
  17.50923,
  13.43731,
  9.89567,
  9.63542,
  13.04209,
  8.88571,
  15.86416,
  12.53905,
  9.25668,
  11.00663,
  11.19891,
  10.55798,
  11.30768,
  11.90394,
  15.64857,
  18.99115,
  // SOUTH DAKOTA
  0.09043,
  0.06782,
  0.36172,
  1.34515,
  3.18767,
  9.76647,
  7.29094,
  5.57277,
  5.15453,
  10.02646,
  5.17714,
  6.13796,
  5.13192,
  4.72498,
  5.01888,
  4.1824,
  4.67977,
  5.00758,
  4.04676,
  5.0754,
  6.12665,
  6.64663,
  7.05357,
  8.97521,
  16.9896,
  24.22402,
  16.92177,
  20.93462,
  27.25344,
  34.35222,
  36.04779,
  47.80373,
  58.42929,
  76.71883,
  83.10547,
  98.02647,
  87.98871,
  // TENNESSEE
  0.02489,
  0.19915,
  1.17584,
  2.76461,
  2.61964,
  2.38389,
  2.93447,
  3.61537,
  4.92153,
  3.81159,
  3.31226,
  3.97998,
  5.03868,
  4.71507,
  6.57327,
  7.62171,
  12.96789,
  15.66954,
  20.4256,
  22.61913,
  23.25904,
  19.73738,
  17.80742,
  15.61536,
  14.64892,
  15.18046,
  12.72628,
  14.50102,
  13.77033,
  14.47906,
  18.45025,
  18.28918,
  26.38679,
  26.3209,
  19.99656,
  39.99605,
  45.50184,
  // TEXAS
  0.00621,
  0.41385,
  0.43213,
  1.12878,
  1.91786,
  2.14686,
  1.89303,
  2.11858,
  2.51863,
  2.918,
  2.90283,
  2.58933,
  3.49843,
  4.0223,
  6.30021,
  11.05881,
  15.19526,
  18.75059,
  21.48926,
  23.61335,
  17.5825,
  19.09857,
  15.89536,
  16.89343,
  12.13207,
  9.52204,
  8.43637,
  10.00487,
  15.55393,
  9.85726,
  10.28629,
  10.29388,
  12.379,
  14.44309,
  16.9293,
  21.53547,
  23.35332,
  // UTAH
  0.0156,
  0.2277,
  1.01062,
  2.0961,
  2.81351,
  2.20527,
  2.89773,
  3.30634,
  3.28139,
  3.19717,
  3.50909,
  3.26579,
  5.90151,
  7.60771,
  8.06935,
  11.02635,
  12.15237,
  12.74502,
  14.00205,
  13.26904,
  11.21974,
  10.04068,
  7.82605,
  7.97889,
  8.03192,
  8.63704,
  8.39999,
  14.46993,
  20.1531,
  21.61912,
  25.36839,
  27.03404,
  29.79453,
  35.63054,
  44.75105,
  57.73625,
  77.34038,
  // VERMONT
  0.03205,
  0.32052,
  2.17953,
  2.88467,
  4.64752,
  2.24363,
  0.91348,
  0.65706,
  0.8013,
  0.25641,
  0.28847,
  0.38462,
  0.83335,
  1.34618,
  0.40065,
  0.89745,
  0.57693,
  0.72117,
  0.84937,
  0.83335,
  0.48078,
  0.60899,
  0.62501,
  0.84937,
  0.78527,
  0.81732,
  0.38462,
  0.70514,
  0.30449,
  0.4968,
  1.25002,
  1.10579,
  1.61862,
  2.2276,
  2.74043,
  6.68281,
  11.47456,
  // VIRGINIA
  0.01992,
  0.09021,
  0.4288,
  1.45978,
  2.7368,
  3.33547,
  4.37935,
  5.33418,
  6.27613,
  6.94978,
  6.98141,
  8.16002,
  7.2954,
  5.45368,
  4.09348,
  4.23524,
  4.28211,
  4.86438,
  7.47348,
  7.74645,
  8.62748,
  7.84721,
  8.41659,
  6.8666,
  7.25791,
  7.85658,
  7.53206,
  7.42896,
  6.4296,
  5.32129,
  7.12083,
  7.26142,
  6.88652,
  7.6703,
  8.31115,
  9.1746,
  12.29568,
  // WASHINGTON
  0.50821,
  1.20685,
  2.4045,
  4.43604,
  3.96985,
  1.91073,
  2.21934,
  2.067,
  2.50036,
  2.02498,
  1.76496,
  2.16287,
  2.58047,
  2.69209,
  3.16879,
  4.16946,
  4.96921,
  5.81755,
  7.52735,
  7.48008,
  7.60877,
  6.71579,
  5.80704,
  5.31853,
  4.352,
  4.14057,
  3.42881,
  3.58639,
  3.99218,
  5.09265,
  4.92456,
  5.69148,
  5.84512,
  6.86549,
  10.06974,
  14.78287,
  18.44412,
  // WEST VIRGINIA
  0,
  0.0279,
  0.39617,
  0.78677,
  1.70745,
  1.20526,
  1.35034,
  0.80351,
  0.90394,
  0.82025,
  0.8872,
  1.74651,
  1.03786,
  0.66959,
  1.04902,
  1.45635,
  2.18732,
  3.30888,
  4.61458,
  5.28416,
  4.54762,
  4.95495,
  4.80987,
  4.5811,
  3.78875,
  6.51732,
  6.13789,
  7.56634,
  6.86328,
  6.80748,
  7.22597,
  8.86646,
  8.21919,
  11.14306,
  13.86047,
  18.99398,
  31.2028,
  // WISCONSIN
  0.01202,
  0.25247,
  0.94806,
  1.757,
  1.98371,
  1.70032,
  2.02149,
  3.09493,
  4.05501,
  3.53804,
  4.48266,
  5.30534,
  5.01165,
  3.49338,
  3.34911,
  4.03783,
  6.03012,
  7.16195,
  9.82235,
  10.77213,
  10.66393,
  9.73991,
  9.32084,
  8.63385,
  8.42431,
  8.10314,
  12.0654,
  16.94309,
  23.32014,
  28.91746,
  29.04627,
  36.69943,
  41.72138,
  50.86189,
  61.78344,
  77.45901,
  75.19192,
  // WYOMING
  0.01728,
  0.29373,
  0.65658,
  1.62416,
  1.53777,
  0.98487,
  0.62202,
  1.4341,
  1.17493,
  0.7948,
  1.36499,
  1.01942,
  0.72569,
  1.45138,
  1.95245,
  2.52264,
  3.12738,
  3.36928,
  3.73212,
  4.82066,
  5.07983,
  4.00858,
  3.07555,
  5.40812,
  3.90491,
  2.90276,
  3.88763,
  6.51394,
  9.53765,
  11.78383,
  16.18981,
  19.19625,
  27.31707,
  36.31909,
  49.26057,
  75.54094,
  88.18869,
];

const MapColumns = 37, // INCREMENT ME
  MapRows = 50;

const margin = { top: 100, right: 50, bottom: 100, left: 50 };

const initialHoneycombWidth = 1000;
const initialHoneycombHeight = 1200;
const maxHoneycombRadius = d3.min([
  initialHoneycombWidth / (Math.sqrt(3) * MapColumns),
  initialHoneycombHeight / (MapRows * 1.5),
]);

const honeycombWidth = MapColumns * maxHoneycombRadius * Math.sqrt(3);
const honeycombHeight =
  MapRows * 1.5 * maxHoneycombRadius + 0.5 * maxHoneycombRadius;

const svg = d3
  .select("#beehive-chart")
  .append("svg")
  .attr("width", honeycombWidth + margin.left + margin.right)
  .attr("height", honeycombHeight + margin.top + margin.bottom)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

const fontSize = (honeycombWidth * 62.5) / 800;
d3.select("html").style("font-size", fontSize + "%");

// the linearGradient element must be nested inside this
const defs = svg.append("defs");

// CALCULATE HONEYCOMB MEASUREMENTS AND ADD TO ARRAY

const SQRT3 = Math.sqrt(3),
  calculatedHoneycombWidth = SQRT3 * maxHoneycombRadius,
  calculatedHoneycombHeight = 2 * maxHoneycombRadius;

const honeycombSides = [
  [0, -1],
  [SQRT3 / 2, 0.5],
  [0, 1],
  [-SQRT3 / 2, 0.5],
  [-SQRT3 / 2, -0.5],
  [0, -1],
  [SQRT3 / 2, -0.5],
];

const honeycombPath =
  "m" +
  honeycombSides
    .map((p) =>
      [p[0] * maxHoneycombRadius, p[1] * maxHoneycombRadius].join(",")
    )
    .join("l") +
  "z";

const points = [];
for (let i = 0; i < MapRows; i++) {
  for (let j = 0; j < MapColumns; j++) {
    let a;
    const b = (3 * i * maxHoneycombRadius) / 2;
    if (i % 2 === 0) {
      a = SQRT3 * j * maxHoneycombRadius;
    } else {
      a = SQRT3 * (j - 0.5) * maxHoneycombRadius;
    }
    points.push({ x: a, y: b });
  }
}

// CREATE CONTINUOUS COLOR SCALE

const gradientColors = ["#E8E8E8", "#000"]; // gray to black
const gradientColorRange = d3.range(0, 1, 1.0 / (gradientColors.length - 1));
gradientColorRange.push(1);

const createColorGradient = d3.scale
  .linear()
  .domain(gradientColorRange)
  .range(gradientColors)
  .interpolate(d3.interpolateHcl);

const mapDataValuesToGradientScale = d3.scale
  .linear()
  .domain(d3.extent(somData))
  .range([0, 2]);

// CREATE COLOR GRADIENT

defs
  .append("linearGradient")
  .attr("id", "color-gradient")
  .attr("x1", "0%")
  .attr("y1", "0%")
  .attr("x2", "100%")
  .attr("y2", "0%")
  .selectAll("stop")
  .data(gradientColors)
  .enter()
  .append("stop")
  .attr("offset", (d, i) => {
    return i / (gradientColors.length - 1);
  })
  .attr("stop-color", (d) => {
    return d;
  });

// CREATE HEATMAP

svg
  .append("text")
  .attr("class", "beehive-title")
  .attr("x", honeycombWidth / 2 - 4)
  .attr("y", -30)
  .text("New Confirmed Cases Per Week");

let hexCounter = 0;
const states = [
  "Alabama",
  "Alaska",
  "Arizona",
  "Arkansas",
  "California",
  "Colorado",
  "Connecticut",
  "Delaware",
  "Florida",
  "Georgia",
  "Hawaii",
  "Idaho",
  "Illinois",
  "Indiana",
  "Iowa",
  "Kansas",
  "Kentucky",
  "Louisiana",
  "Maine",
  "Maryland",
  "Massachusetts",
  "Michigan",
  "Minnesota",
  "Mississippi",
  "Missouri",
  "Montana",
  "Nebraska",
  "Nevada",
  "New Hampshire",
  "New Jersey",
  "New Mexico",
  "New York",
  "North Carolina",
  "North Dakota",
  "Ohio",
  "Oklahoma",
  "Oregon",
  "Pennsylvania",
  "Rhode Island",
  "South Carolina",
  "South Dakota",
  "Tennessee",
  "Texas",
  "Utah",
  "Vermont",
  "Virginia",
  "Washington",
  "West Virginia",
  "Wisconsin",
  "Wyoming",
];

svg
  .append("g")
  .selectAll(".honeycomb")
  .data(points)
  .enter()
  .append("path")
  .attr("id", () => {
    hexCounter++;
    let mappedVal = hexCounter / MapColumns;

    return mappedVal % 1 === 0
      ? states[mappedVal - 1]
      : states[Math.floor(mappedVal)];
  })
  .attr("class", "honeycomb")
  .attr("d", (d) => {
    return "M" + d.x + "," + d.y + honeycombPath;
  })
  .style("stroke", "#fff")
  .style("stroke-width", "1px")
  .style("fill", "white")
  .on("mouseover", mouseonHoneycomb)
  .on("mouseout", mouseoutHoneycomb);

// CREATE LEGEND

const legendWidth = honeycombWidth * 0.6,
  legendHeight = 10;

const legendContainer = svg
  .append("g")
  .attr("class", "legendWrapper")
  .attr(
    "transform",
    "translate(" +
      (honeycombWidth / 2 - 10) +
      "," +
      (honeycombHeight + 50) +
      ")"
  );

legendContainer
  .append("rect")
  .attr("class", "legendBar")
  .attr("x", -legendWidth / 2)
  .attr("y", 10)
  .attr("width", legendWidth)
  .attr("height", legendHeight)
  .style("fill", "none");

legendContainer
  .append("text")
  .attr("class", "legendTitle")
  .attr("x", 0)
  .attr("y", -2)
  .text("Number of New Cases Per Capita");

const xAxisScale = d3.scale.linear().range([0, legendWidth]).domain([0, 100]);

const xAxis = d3.svg.axis().orient("bottom").ticks(5).scale(xAxisScale);

legendContainer
  .append("g")
  .attr("class", "axis")
  .attr(
    "transform",
    "translate(" + -legendWidth / 2 + "," + (10 + legendHeight) + ")"
  )
  .call(xAxis);

// MOUSE INTERACTIONS

function mouseonHoneycomb(d) {
  const el = d3
    .select(this)
    .transition()
    .duration(10)
    .style("fill-opacity", 0.3);
}

function mouseoutHoneycomb(d) {
  const el = d3
    .select(this)
    .transition()
    .duration(1500)
    .style("fill-opacity", 1);
}

function createGradient() {
  svg.select(".legendBar").style("fill", "url(#color-gradient)");
  svg
    .selectAll(".honeycomb")
    .transition()
    .duration(1000)
    .style("fill", (d, i) => {
      return createColorGradient(mapDataValuesToGradientScale(somData[i]));
    });
}

// SETUP
createGradient();
