import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
import unittest
from ..src.pizza_gui import PizzaPriceGUI


class TestGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = PizzaPriceGUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_gui_initialization(self):
        self.assertIsNotNone(self.app.root)
        self.assertEqual(self.app.root.title(), "Pizza Price Comparison")

    def test_search_functionality(self):
        # Test with valid pizza type
        self.app.pizza_entry.insert(0, "Margherita")
        self.app.search_pizzas()
        self.assertEqual(len(self.app.tree.get_children()), 3)

    def test_invalid_search(self):
        # Test with invalid pizza type
        self.app.pizza_entry.insert(0, "Invalid Pizza")
        self.app.search_pizzas()
        self.assertEqual(len(self.app.tree.get_children()), 0)

if __name__ == '__main__':
    unittest.main()