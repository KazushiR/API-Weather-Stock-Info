import json, requests, sys
from pprint import pprint
from twilio.rest import Client
from datetime import datetime, timedelta
#! python3
#Weather Data
APPID = "Token is HERE"
location = "97222"
url =f'http://api.openweathermap.org/data/2.5/weather?zip={location},US&APPID=Token is HERE'
response = requests.get(url)
response.raise_for_status()
weatherData = json.loads(response.text)

for i, v in weatherData.items():
    if i == "main":
        data = v        
for i, v in data.items():
    if i == "temp":
        temp = v
    elif i == "feels_like":
        feels = v
tempf = round(int(temp)*(9/5)-459.67)
feelsf = round(int(feels)*(9/5)-459.67)

#stock information
API_URL = "https://www.alphavantage.co/query"
currenttime = (datetime.now()-timedelta(days=1)).strftime('%Y-%m-%d')
companys = ["SPY", "QQQ", "ROBO"]
stock_prices =[]
for company in companys:
    data = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": company,
        "apikey": "PHONE NUMBER",
        }

    stockresponse = requests.get(API_URL, data)
    response_json = stockresponse.json()
    for k, v in response_json.items():
        if k == 'Time Series (Daily)':
            stockdata = v
    for k, v in stockdata.items():
        if k == currenttime:
            price = v
    for k, v in price.items():
        if k == '4. close':
            final = float(v)
            stock_prices.append(final)

#texting
accountSID = "Token is HERE"
authToken  = "Token is HERE"
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+PHONE NUMBER'
myCellPhone = '+PHONE NUMBER'
message = twilioCli.messages.create(body = f"""\n\nThe current temperature right now is {tempf} Fahrenheit, but it will feel like it is {feelsf} fahrenheit. These temperatures are not accurate but is close to what it actually is.
                                    \n Now, let's look at the open stock prices today.\n\nThe stock price for {companys[0]} is {stock_prices[0]}\n\nThe stock price for {companys[1]} is {stock_prices[1]}\n\nThe stock price for {companys[2]} is {stock_prices[2]}.\n\nIf you want to know different ETF, let me know but if you want more information on individual stocks, please let me know as I can give a lot of information. My minutes are limited on this account so I do not know how many minutes I have left. I might purchase a monthly plan as it is cheap.""",
                                     from_ = myTwilioNumber, to = myCellPhone)

