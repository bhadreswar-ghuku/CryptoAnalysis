import argparse
import time
from KoinexAnalysis import KoinexAnalysis

koinex_ticker_url = "https://koinex.in/api/ticker"
koinex_data_file = "../Data/koinex_crypto_trading_report.csv"
koinex_crypto_coins = ["BTC", "ETH", "XRP", "LTC", "BCH"]
analysis_intervals = [1, 2, 5, 10, 20, 30, 1 * 60, 2 * 60, 6 * 60, 12 * 60]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', required=True)
    parser.add_argument('--password', required=True)
    args = parser.parse_args()
    koinexAnalysis = KoinexAnalysis(args.email, args.password, koinex_ticker_url,
                                    koinex_data_file, koinex_crypto_coins, analysis_intervals)
    i = 0
    while True:
        try:
            koinexAnalysis.crawl_data()
            i += 1
            if i % 60 == 0:
                koinexAnalysis.send_koinex_report()
        except Exception as e:
            print("Got exception while crawling data or sending email : " + str(e))
        time.sleep(60)
