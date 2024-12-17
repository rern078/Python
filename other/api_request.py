# import requests
# import json

# # Function to get stock data
# def get_stock_data():
#       url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
#       response = requests.get(url)

#       if response.status_code == 200:
#             data = response.json()
#             last_refreshed = data['Meta Data']['3. Last Refreshed']
#             price = data['Time Series (5min)'][last_refreshed]['1. open']
#             return price 
#       else:
#             return None
      
#       stock_price = {}
#       price = get_stock_data()
#       symbol = "IBM"
#       if price is not None:
#             stock_price[symbol] = price

#       print(f"{symbol}: {price}")



# get request **************************
# import requests

# # Replace 'API_KEY' with your actual API key from NewsAPI
# API_KEY = '3805f6bbabcb42b3a0c08a489baf603d'
# url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"
# response = requests.get(url)
# print(response.status_code)

# get data **************************
import json
import requests

def fetch_and_print_articles(api_url):
    response = requests.get(api_url)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        
        for index, article in enumerate(articles[:3], start=1):
            print(f"Article {index}:\n{json.dumps(article, sort_keys=True, indent=4)}\n")
    else:
        print(f"Error: {response.status_code}")

API_KEY = '3805f6bbabcb42b3a0c08a489baf603d'
api_endpoint = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"

fetch_and_print_articles(api_endpoint)

def jprint(obj):
    print(json.dumps(obj, sort_keys=True, indent=4))

# Example usage:
# jprint(response.json())

# How to connect Api in python **************************
import requests

url = "http://api.example.com/data"
response = requests.get(url)
data = response.json()  # Assuming the response is in JSON format
print(data)

# How to get data from Api in python **************************
import requests

# Define the API endpoint
url = "https://api.example.com/items"

# Send a GET request
response = requests.get(url)

# Convert the response to JSON format
items = response.json()

# Use the data
for item in items:
    print(item)

#     How to Create a FastAPI in Python? **************************
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Run the server
# Command to run: `uvicorn filename:app --reload`