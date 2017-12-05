import requests


class CoinMarketCapAnalysis:
    email = ""
    password = ""
    market_info_url = "https://api.coinmarketcap.com/v1/ticker/?limit=40"
    file_name = ""
    intervals = []
    data = {}
    message = ""
    is_report_ready = False
    iteration = 1
    comma = ","

    def __init__(self, email, password, file_name):
        self.email = email
        self.password = password
        self.file_name = file_name

    def crawl_top_coins(self):
        page = requests.get(self.market_info_url)
        json_result = page.json()
        print("rank,id,symbol,price_usd,price_btc,24h_volume_usd,market_cap_usd,percent_change_1h,percent_change_24h,"
              "percent_change_7d")
        for coin in json_result:
            print(self.print_coin(coin))

    def print_coin(self, coin):
        text = ""
        text += coin["rank"] + self.comma
        text += coin["id"] + self.comma
        text += coin["symbol"] + self.comma
        text += coin["price_usd"] + self.comma
        text += coin["price_btc"] + self.comma
        text += coin["24h_volume_usd"] + self.comma
        text += coin["market_cap_usd"] + self.comma
        text += coin["percent_change_1h"] + self.comma
        text += coin["percent_change_24h"] + self.comma
        text += coin["percent_change_7d"]
        return text


if __name__ == '__main__':
    coinMarketCapAnalysis = CoinMarketCapAnalysis("", "", "")
    coinMarketCapAnalysis.crawl_top_coins()
