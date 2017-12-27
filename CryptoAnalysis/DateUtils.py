import datetime

date_format = "{:%Y-%m-%d-%H-%M}"
day_format = "{:%Y-%m-%d}"


def date_string_now():
    return date_format.format(datetime.datetime.now())


def date_string_last_in_min(minutes):
    return date_format.format(datetime.datetime.now() - datetime.timedelta(minutes=minutes))


def date_string_today():
    return day_format.format(datetime.datetime.now())
