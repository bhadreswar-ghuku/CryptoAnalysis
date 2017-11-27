# This is for trend analysis of crypto-currency
# possibly it checks coin value of last 1m, 2m, 5m, 10m, 20m, 30m, 1h, 2h, 6h, 12h
from DateUtils import date_string_last_in_min

FLOAT_ROUNDING = 3


def trend_analysis(current, coin, intervals, data):
    trend_data = {}
    for interval in intervals:
        interval_timestamp = date_string_last_in_min(interval)
        key = coin + "_" + interval_timestamp
        if key in data:
            trend_data[interval] = data[key]
    return calculate_percent(current, trend_data)


def calculate_percent(current, data):
    trend = {}
    for point in data:
        diff = current - data[point]
        percent = (diff * 100) / current
        trend[point] = round(percent, FLOAT_ROUNDING)
    return trend


def print_trend(coin, data):
    coin_trend = "Trend for coin : " + coin + "\n"
    print("Printing trend for coin : " + coin)
    for key in sorted(data):
        trend = beautify_interval(key) + " : " + str(data[key]) + " %"
        coin_trend += trend + "\n"
        print(trend)
    return coin_trend


def beautify_interval(interval):
    if interval < 60:
        return str(interval) + "m"
    elif interval < 3600:
        return str(interval / 60) + "h"
    else:
        return str(interval / 3600) + "d"
