import argparse

import requests
from KoinexAnalysis import KoinexAnalysis
from SendEmail import send_multiple_email


class BitBnsAnalysis:
    ticker_url = ''
    coins = []

    def __init__(self, ticker_url, coins):
        self.ticker_url = ticker_url
        self.coins = coins

    def current_rate(self):
        page = requests.get(self.ticker_url)
        json_result = page.json()
        price_dict = {}
        for item in json_result:
            key, value = item.popitem()
            if key in coins:
                price_dict[key] = value['lastTradePrice']
        return price_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', required=True)
    parser.add_argument('--password', required=True)
    args = parser.parse_args()
    coins = ['BTC', 'XRP', 'ETH']
    bitBnsAnalysis = BitBnsAnalysis("https://bitbns.com/order/getTickerAll", coins)
    bitbns_rate = bitBnsAnalysis.current_rate()
    koinexAnalysis = KoinexAnalysis("", "", "https://koinex.in/api/ticker", "../Data", coins, [])
    koinex_rate = koinexAnalysis.current_rate()
    diff_threshold = 5
    msg = 'Diff threshold is ' + str(diff_threshold) + '%\n'
    for coin in coins:
        msg += coin + '\tbitbns : ' + str(bitbns_rate[coin]) + '\tkoinex : ' + str(koinex_rate[coin]) + '\n'
        diff = abs(float(bitbns_rate[coin]) - float(koinex_rate[coin]))
        percent = (diff * 100) / bitbns_rate[coin]
        if percent > diff_threshold:
            msg += "Invest in : " + coin + '\n'
    print(msg)
    recipient_list = ['ghuku17@gmail.com', 'siddh.ag45@gmail.com']
    send_multiple_email("BitBns vs Koinex Analysis", msg, args.email, recipient_list, args.password)

