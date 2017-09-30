
The program is to calcualte metrics of stocks, then pick stock based on algorithms

1. ./calculateMetrics.py [ -f folderName / -s stockFileName ]
calculate
    EMA21、EMA60、EMA200
    STD21、STD60、STD200
    VAR21、VAR60、VAR200
P.S. EMA = [currentDayClose × 2 + previousDayEMA ×（N-1)] / (N+1)
    the std/var for the first N days is marked as 0

2. ./pickStockByDate -d 20001030 => stocks_date.csv
    if no argument is specified, pick the newest


3. selecting stocks => output stocks_data.csv


