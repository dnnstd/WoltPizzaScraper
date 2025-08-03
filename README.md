# Berlin Pizza Price Tracker
==========================

A Python-based web scraper that tracks and compares pizza prices across various restaurants in Berlin. This project was developed as part of a university assignment to demonstrate web scraping concepts and data analysis techniques.

## Overview
--------

This project creates a comprehensive database of pizza prices from multiple Berlin restaurants listed on Wolt, allowing users to compare prices and find the best deals. The system includes both CLI and GUI interfaces, though the GUI functionality is still in development.

## Features
------------

✨ Web scraping of Wolt restaurant listings
✨ Price comparison across multiple establishments
✨ Data persistence in CSV format
✨ Command-line interface for searching specific pizza types
✨ Partial GUI implementation (work in progress)

## Technical Requirements
-----------------------

### Dependencies

* Python 3.x
* `requests` for HTTP requests
* `beautifulsoup4` for HTML parsing
* `pandas` for data manipulation
* `tkinter` for GUI (built into Python)

### Installation

```bash
pip install -r requirements.txt
```

## Usage
-----

### Command Line Interface

1. Run the script:
   ```bash
python main.py
```
2. Enter a pizza type when prompted
3. View sorted price comparisons in the console

### GUI Interface (Limited Functionality)

⚠️ **Important:** Due to current limitations, the GUI must be launched from `main.py`. Direct GUI execution is not supported.

```bash
python main.py
```

## Implementation Details
----------------------

The project consists of four main modules:

1. **Data Fetcher**
    * Scrapes Wolt restaurant pages
    * Extracts pizza names and prices
    * Handles pagination and rate limiting

2. **Data Writer**
    * Creates and maintains CSV storage
    * Ensures data consistency
    * Manages file operations

3. **Data Analyzer**
    * Processes price comparisons
    * Filters by pizza type
    * Sorts results by price

4. **GUI Interface**
    * Provides visual interface
    * Displays searchable results
    * Shows price comparisons in tabular format

## Known Limitations
-------------------

1. GUI Integration
    - Currently requires initial launch via main.py
    - Full integration pending
    - Some UI elements may not respond as expected

2. Web Scraping
    - Relies on stable Wolt website structure
    - May break if Wolt changes their layout
    - Rate limiting not implemented

## Future Improvements
--------------------

1. Complete GUI Integration
2. Error Handling
3. Rate Limiting
4. Restaurant Filtering
5. Visual Price Trends

## Academic Context
-----------------

This project demonstrates key programming concepts:
- Web scraping with BeautifulSoup
- Data processing with Pandas
- GUI development with Tkinter
- Modular program design
- Error handling and debugging

## License
-------

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgments
---------------

Special thanks to:
- University instructors for guidance
- Open-source contributors whose code inspired parts of this project
- Wolt for providing accessible restaurant data