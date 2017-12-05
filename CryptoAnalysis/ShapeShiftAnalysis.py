import requests
from KoinexAnalysis import KoinexAnalysis


class ShapeShiftAnalysis:
    email = ""
    password = ""
    market_info_url = "https://shapeshift.io/marketinfo/"
    coins_url = "https://shapeshift.io/getcoins"
    file_name = ""
    crypto_coins = ["btc", "eth", "ltc", "xrp", "bch", "gnt", "omg"]
    intervals = []
    data = {}
    message = ""
    is_report_ready = False
    iteration = 1

    def __init__(self, email, password, file_name):
        self.email = email
        self.password = password
        self.file_name = file_name

    def crawl_data(self):
        size = len(self.crypto_coins)
        # print("size : " + str(size))
        for i in range(0, size):
            for j in range(0, size):
                if i != j:
                    # print("i = " + str(i) + ", j = " + str(j))
                    pre_coin = self.crypto_coins[i]
                    post_coin = self.crypto_coins[j]
                    page = requests.get(self.market_info_url + pre_coin + "_" + post_coin)
                    json_result = page.json()
                    output = ""
                    output += str(json_result["pair"]) + ","
                    output += str(json_result["rate"]) + ","
                    output += str(json_result["minerFee"]) + ","
                    output += str(json_result["limit"]) + ","
                    output += str(json_result["minimum"]) + ","
                    output += str(json_result["maxLimit"])
                    print(output)

    def get_coins(self):
        page = requests.get(self.coins_url)
        json_result = page.json()
        total = 0
        available = 0
        available_list = []
        for entry in json_result:
            detail = json_result[entry]
            if detail["status"] == "available":
                available += 1
                available_list.append(entry + "(" + detail["name"] + ")")
            total += 1
        print("total coins : " + str(total))
        print("available coins : " + str(available))
        print("available coins list :" + str(available_list))
koinex_ticker_url = "https://koinex.in/api/ticker"
koinex_data_file = "../Data/koinex_crypto_trading_report.csv"
koinex_crypto_coins = ["BTC", "ETH", "XRP", "LTC", "BCH"]
analysis_intervals = [1, 2, 5, 10, 20, 30, 1 * 60, 2 * 60, 6 * 60, 12 * 60]

if __name__ == '__main__':
    koinexAnalysis = KoinexAnalysis("", "", koinex_ticker_url, koinex_data_file, koinex_crypto_coins, analysis_intervals)
    koinex_rate = koinexAnalysis.current_rate()
    shapeShiftAnalysis = ShapeShiftAnalysis("", "", "")
    shapeShiftAnalysis.crawl_data()
    shapeShiftAnalysis.get_coins()

