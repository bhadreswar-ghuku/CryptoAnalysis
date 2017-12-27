import requests


class CurrencyConversion:

    market_info_url = "http://www.apilayer.net/api/live?access_key=f82d383b519ffa073647ab088339fe69&format=1" \
                      "&currencies=INR "

    def get_usd_inr_rate(self):
        page = requests.get(self.market_info_url)
        json_result = page.json()
        return json_result['quotes']['USDINR']

if __name__ == '__main__':
    currencyConversion = CurrencyConversion()
    inr = currencyConversion.get_usd_inr_rate()
    print("Current USD/INR Rate : " + str(inr))
