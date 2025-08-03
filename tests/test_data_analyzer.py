import unittest
import pandas as pd
from ..src.data_analyzer import analyze_best_prices
from ..src.config import OUTPUT_FILE

class TestDataAnalyzer(unittest.TestCase):
    def setUp(self):
        # Create a sample CSV file for testing
        self.test_data = [
            ["Pizza Hut", "Margherita", "€12.99"],
            ["Domino's", "Margherita", "€11.99"],
            ["Pizza Nostra", "Margherita", "€13.50"],
            ["Pizza Hut", "Quattro Formaggi", "€14.99"],
            ["Domino's", "Quattro Formaggi", "€13.99"]
        ]
        pd.DataFrame(self.test_data, columns=["RESTAURANT", "PIZZA", "PRICE"]).to_csv(OUTPUT_FILE, index=False)

    def tearDown(self):
        # Clean up the test file
        import os
        if os.path.exists(OUTPUT_FILE):
            os.remove(OUTPUT_FILE)

    def test_analyze_best_prices_margherita(self):
        results = analyze_best_prices(OUTPUT_FILE, "Margherita")
        self.assertEqual(len(results), 3)  # Should find 3 Margherita pizzas
        self.assertEqual(results.iloc[0]["RESTAURANT"], "Domino's")  # Should be cheapest
        self.assertEqual(results.iloc[0]["PRICE"], "€11.99")

    def test_analyze_best_prices_quattro_formaggi(self):
        results = analyze_best_prices(OUTPUT_FILE, "Quattro Formaggi")
        self.assertEqual(len(results), 2)  # Should find 2 Quattro Formaggi pizzas
        self.assertEqual(results.iloc[0]["RESTAURANT"], "Domino's")  # Should be cheapest
        self.assertEqual(results.iloc[0]["PRICE"], "€13.99")

    def test_analyze_best_prices_invalid_pizza(self):
        results = analyze_best_prices(OUTPUT_FILE, "Invalid Pizza")
        self.assertEqual(len(results), 0)  # Should find no matches

if __name__ == '__main__':
    unittest.main()