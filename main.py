from config import URLS
from data_fetcher import scrape_pizza_data
from data_writer import write_pizza_data
from data_analyzer import analyze_best_prices

def main():
    scraped_data = []
    for url in URLS:
        restaurant_name, pizzas, prices = scrape_pizza_data(url)

        for pizza, price in zip(pizzas, prices):
            print(f"{restaurant_name}: {pizza.text} = {price.text}")
            scraped_data.append([restaurant_name, pizza.text, price.text])


    write_pizza_data("pizza_prices.csv", scraped_data)

    pizza_type = input("\n" + "Enter the Pizza Type to search for: ")
    results = analyze_best_prices("pizza_prices.csv", pizza_type)
    print(results)

if __name__ == "__main__":
    main()