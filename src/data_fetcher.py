import requests
from bs4 import BeautifulSoup

def scrape_pizza_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    restaurant_name = url.split("/")[-1]
    prices = soup.find_all("div", class_="r1c06vh9")
    pizzas = soup.find_all("h3", class_="tj9ydql")

    return restaurant_name, pizzas, prices