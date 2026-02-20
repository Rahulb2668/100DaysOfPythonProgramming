from dotenv import load_dotenv
import os
import requests

load_dotenv()

STOCK_NAME= "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT="https://www.alphavantage.co/query"
NEWS_ENDPOINT="https://newsapi.org/v2/everything"

alphaventage_api_key=os.getenv("ALPHAVENTAGE_API_KEY")
new_api_key=os.getenv("NEWS_API")

# Get Stock price of yesterday
stock_params = {
"function":"TIME_SERIES_DAILY",
"symbol":STOCK_NAME,
"apikey":alphaventage_api_key
}

news_params = {
    'q':STOCK_NAME,
    'searchIn': {'title':COMPANY_NAME},
    'apiKey':new_api_key
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items() ]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

# Day before yesterday closing price

day_before_yesterday_data = data_list[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data['4. close']

print(yesterday_closing_price, day_before_yesterday_data_closing_price)
# Finding the difference between the closing prices
diff_close_price = abs(float(yesterday_closing_price) - float(day_before_yesterday_data_closing_price))
diff_percentage = (diff_close_price / float(yesterday_closing_price))*100
print(diff_percentage)


if diff_percentage > .15:
    response = requests.get(NEWS_ENDPOINT, news_params)
    response.raise_for_status()
    news_articles = response.json()['articles'][:3]
    formatted_news = [f"Headline: {article["title"]}  \n Description:{article["description"]} \nMore:{article["url"]}" for article in news_articles]


    # Send Message