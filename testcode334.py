import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "R2PF6OZGASOE2ALA"

## STEP 1: Get yesterday's closing stock price.
# TODO 1: Get yesterday's closing stock price.
# Hint: You can perform list comprehensions on Python dictionaries.
# e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
yesterday_data = data[next(iter(data))]  # Get the first (latest) item in the dictionary
yesterday_closing_price = yesterday_data["4. close"]
print("Yesterday's closing price:", yesterday_closing_price)

# TODO 2: Get the day before yesterday's closing stock price

# TODO 3: Find the positive difference between 1 and 2.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp

# TODO 4: Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

# TODO 5: If TODO4 percentage is greater than 5 then print("Get News").

## STEP 2: Use the News API to get articles related to the COMPANY_NAME.

# TODO 6: Use the News API to get articles related to the COMPANY_NAME.

# TODO 7: Use Python slice operator to create a list that contains the first 3 articles.
# Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

## STEP 3: Send each article as a separate message via Twilio.

# TODO 8: Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9: Send each article as a separate message via Twilio.

# Optional TODO: Format the message.
