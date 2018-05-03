import requests

from DateUtils import date_string_now
from FileHandler import read_data, write_data
from TrendAnalysis import trend_analysis, print_trend
from SendEmail import send_email


class KoinexAnalysis:
    email = ""
    password = ""
    koinex_ticker_url = ""
    file_name = ""
    crypto_coins = []
    intervals = []
    data = {}
    message = ""
    is_report_ready = False
    iteration = 1

    def __init__(self, email, password, ticker_url, data_file, coins, intervals):
        self.email = email
        self.password = password
        self.koinex_ticker_url = ticker_url
        self.file_name = data_file
        self.crypto_coins = coins
        self.intervals = intervals

    def crawl_data(self):
        if len(self.data) == 0:
            self.data = read_data(self.file_name)
        page = requests.get(self.koinex_ticker_url)
        json_result = page.json()
        crypto_stats = json_result["stats"]
        timestamp = date_string_now()
        self.is_report_ready = False
        self.message = ""
        for coin in self.crypto_coins:
            last_trading_price = float(crypto_stats[coin]["last_traded_price"])
            coin_key = coin + "_" + timestamp
            self.data[coin_key] = last_trading_price
            trend = trend_analysis(last_trading_price, coin, self.intervals, self.data)
            self.message += print_trend(coin, trend) + "\n"
        print("Koinex Data updated for timestamp : " + timestamp)
        self.is_report_ready = True
        if self.iteration % 5 == 0:
            write_data(self.data, self.file_name)
            print("Koinex Data flushed to file for iteration : " + str(self.iteration))
        self.iteration += 1

    def send_koinex_report(self):
        if self.is_report_ready:
            timestamp = date_string_now()
            title = "Koinex crypto report " + timestamp
            send_email(title, self.message, self.email, self.password)
            print("Sent koinex crypto report to email id : " + self.email + " for time : " + timestamp)
        else:
            print("Koinex crypto report isn't ready, Try after 1s")

    def current_rate(self):
        page = requests.get(self.koinex_ticker_url)
        json_result = page.json()
        prices = json_result["prices"]
        price_dict = {}
        for coin in self.crypto_coins:
            price_dict[coin] = prices[coin]
        return price_dict
