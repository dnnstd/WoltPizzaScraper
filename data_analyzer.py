import pandas as pd

def analyze_best_prices(csv_file, pizza_type):
    df = pd.read_csv(csv_file)
    df["RESTAURANT"] = df["RESTAURANT"].str.replace("-", " ")
    df["PRICE"] = df["PRICE"].str.replace("€Beliebt", "€")

    results = df[df["PIZZA"].str.contains(pizza_type)]
    cleaned_df = results.drop_duplicates()

    return cleaned_df.sort_values("PRICE", ascending=True)