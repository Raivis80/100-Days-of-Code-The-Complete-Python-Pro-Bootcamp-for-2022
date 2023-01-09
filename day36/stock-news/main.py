import os
import requests
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")


def api_call(*args, **kwargs):
    parameters = kwargs.get("parameters")
    endpoint = kwargs.get("endpoint")

    response = requests.get(endpoint, parameters)
    response.raise_for_status()
    return response.json()


def get_stock():
    parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY
    }

    data = api_call(endpoint=STOCK_ENDPOINT, parameters=parameters)
    data_daily = data['Time Series (Daily)']

    for i, (day, value) in zip(range(2), data_daily.items()):
        if i == 0:
            day_one = float(value['4. close'])
            date_one = day
        else:
            day_two = float(value['4. close'])
            date_two = day

    return day_one, day_two, date_one, date_two


def get_percentage(day_one, day_two):
    difference = (abs(day_one - day_two))
    if day_one == day_two or difference < 2:
        return
    if day_one < day_two:
        operator = "🔺"
    else:
        operator = "🔻"
    return f"TSLA: {operator + str(round((difference / day_two) * 100.0, 2))}%"


def get_news(from_date, to_date):
    parameters = {
        "q": "Tesla",
        "from_param": from_date,
        "to": to_date,
        "apikey": NEWS_API_KEY,
    }

    data = api_call(endpoint=NEWS_ENDPOINT, parameters=parameters)
    return [{"headline": article['title'], "brief": article["description"], "url": article["url"]} for article in data["articles"][:3]]


def send_email(news, percentage):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="rp42dev@gmail.com", password=EMAIL_PASSWORD)
        connection.sendmail(from_addr="rp42dev@gmail.com", to_addrs="edgarstattoo@gmail.com",
                            msg=f"Subject:{percentage} News\n\n{news['headline']}\n\n{news['brief']}\n\n{news['url']}".encode('utf-8'))


def main():
    stock = get_stock()
    percentage = get_percentage(stock[0], stock[1])
    if not percentage:
        return

    articles = get_news(stock[2], stock[3])
    for article in articles:
        send_email(article, percentage)


if __name__ == "__main__":
    main()
