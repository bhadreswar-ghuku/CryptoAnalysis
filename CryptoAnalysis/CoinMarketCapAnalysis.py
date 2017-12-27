import requests
from DateUtils import date_string_today


class CoinMarketCapAnalysis:
    email = ""
    password = ""
    coin_info_url = "https://api.coinmarketcap.com/v1/ticker/?limit=1377"
    global_market_info_url = "https://api.coinmarketcap.com/v1/global/"
    data = []
    comma = ","
    daily_market_snap_file_name = "../Data/coinmarketdata/daily_market_snap"
    global_market_snap_file_name = "../Data/coinmarketdata/global_market_data"
    top_coins = 50
    coins_headers = "rank,id,symbol,price_usd,price_btc,24h_volume_usd,market_cap_usd,percent_change_1h," \
                    "percent_change_24h,percent_change_7d "
    global_market_headers = "date,total_market_cap,total_1d_vol,bitcoin_percent,active_currencies,active_assets," \
                            "active_markets "

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def crawl_top_coins(self):
        page = requests.get(self.coin_info_url)
        json_result = page.json()
        self.data.append(self.coins_headers)
        for coin in json_result:
            coin_detail = self.print_coin(coin)
            if coin_detail != '':
                self.data.append(coin_detail)

    def print_coin(self, coin):
        text = ""
        try:
            text += coin["rank"] + self.comma
            text += coin["id"] + self.comma
            text += coin["symbol"] + self.comma
            text += coin["price_usd"] + self.comma
            text += coin["price_btc"] + self.comma
            text += "$" + str(float(coin["24h_volume_usd"]) / 1000000) + "m" + self.comma
            text += "$" + str(float(coin["market_cap_usd"]) / 1000000000) + "b" + self.comma
            text += coin["percent_change_1h"] + self.comma
            text += coin["percent_change_24h"] + self.comma
            text += coin["percent_change_7d"]
        except Exception as e:
            text = ""
        return text

    def persist_coin_daily_data(self):
        today_data_file = self.daily_market_snap_file_name + '_' + date_string_today()
        try:
            with open(today_data_file, 'w') as f:
                for line in self.data:
                    f.write(line)
                    f.write("\n")
            f.close()
        except FileNotFoundError as e:
            print(self.daily_market_snap_file_name + " not found error : " + str(e))

    def top_n_coins_stat(self):
        for i in range(0, self.top_coins + 1):
            print(self.data[i])

    def persist_global_market_data(self, data):
        try:
            with open(self.global_market_snap_file_name, 'a') as f:
                f.write(data)
                f.write("\n")
                f.close()
        except FileNotFoundError as e:
            print(self.daily_market_snap_file_name + " not found error : " + str(e))

    def crawl_global_market_data(self):
        page = requests.get(self.global_market_info_url)
        json_result = page.json()
        data = ''
        try:
            data += date_string_today() + self.comma
            data += str(json_result['total_market_cap_usd']) + self.comma
            data += str(json_result['total_24h_volume_usd']) + self.comma
            data += str(json_result['bitcoin_percentage_of_market_cap']) + self.comma
            data += str(json_result['active_currencies']) + self.comma
            data += str(json_result['active_assets']) + self.comma
            data += str(json_result['active_markets'])
        except Exception as e:
            data = str(e)
        if data != '':
            print(self.global_market_headers)
            print(data)
            print("\n")
            self.persist_global_market_data(data)

if __name__ == '__main__':
    coinMarketCapAnalysis = CoinMarketCapAnalysis("", "")
    coinMarketCapAnalysis.crawl_global_market_data()
    coinMarketCapAnalysis.crawl_top_coins()
    coinMarketCapAnalysis.top_n_coins_stat()
    coinMarketCapAnalysis.persist_coin_daily_data()
