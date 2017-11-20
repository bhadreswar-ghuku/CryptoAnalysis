from twilio.rest import Client


def send_phone_message(content):

    # Find these values at https://twilio.com/user/account
    account_sid = "***********"
    auth_token = "***********"

    client = Client(account_sid, auth_token)
    client.api.account.messages.create(
        to="***********",
        from_="***********",
        body=content)
