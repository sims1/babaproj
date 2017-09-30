
The program is to calcualte metrics of stocks, then pick stock based on algorithms

1. ./calculateMetrics.py
required options:
        [ -i folderName / stockFileName ]
optional options:
        [ -o output folder name, if not specified, auto generate a name with time stamp]
        [ -f if output folder exist, overwrite it ]

calculate
    EMA21、EMA60、EMA200
    STD21、STD60、STD200
    VAR21、VAR60、VAR200
P.S. EMA = [currentDayClose × 2 + previousDayEMA ×（N-1)] / (N+1)
    the std/var for the first N days is marked as 0

2. ./sliceStockByDate -i stockFile/stockFolder -d 20001030 => stocksByDate_{date}.csv
required options:
        [ -i input file/folder name ]
optional options:
        [ -d date, if not specified, pick the latest date ]
        [ -o output file name, if not specified, default name is stocksByDate_{date}.csv']
        [ -f if output file exist, overwrite it ]

3. ./stockFilter.py -i inputFile -s -ema
required options:
        [ -i input file/folder name ]
        [ -s strategy, current one is -ema, which is
            close >= EMA21 && close >= EMA60 && close >= EMA200, and
            close <= EMA21 * 1.10 ]


