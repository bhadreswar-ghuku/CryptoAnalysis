import time
import requests
import argparse
from DateUtils import date_string_now
from FileHandler import read_data, write_data
from TrendAnalysis import trend_analysis, print_trend
from SendEmail import send_email

koinex_ticker_url = "https://koinex.in/api/ticker"
file_name = "../Data/koinex_crypto_trading_report.csv"
crypto_coins = ["BTC", "ETH", "XRP", "LTC", "BCH"]
intervals = [1, 2, 5, 10, 20, 30, 1 * 60, 2 * 60, 6 * 60, 12 * 60]

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--email', required=True)
    parser.add_argument('--password', required=True)
    args = parser.parse_args()

    data = read_data(file_name)
    i = 0
    while True:
        page = requests.get(koinex_ticker_url)
        json_result = page.json()
        crypto_stats = json_result["stats"]
        timestamp = date_string_now()
        message = ""
        for coin in crypto_coins:
            last_trading_price = float(crypto_stats[coin]["last_traded_price"])
            coin_key = coin + "_" + timestamp
            data[coin_key] = last_trading_price
            trend = trend_analysis(last_trading_price, coin, intervals, data)
            message += str(trend) + "\n"
            print_trend(coin, trend)
        print("Data updated for timestamp : " + timestamp)

        if i % 5 == 0:
            write_data(data, file_name)
            print("Data flushed to file for iteration : " + str(i))
        i += 1
        # send_email("Koinex crypto update", message, args.email, args.password)
        time.sleep(60)
