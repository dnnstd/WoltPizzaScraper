# Berlin Pizza Price Tracker
=========================

A Python-based web scraper that tracks and compares pizza prices across various restaurants in Berlin. Developed as part of a university assignment focusing on web scraping concepts and data analysis techniques.

## Overview
--------

Creates a comprehensive database of pizza prices from multiple Berlin restaurants listed on Wolt, enabling price comparisons and deal discovery. Features both CLI and GUI interfaces, with GUI functionality currently in development.

## Features
------------

✨ Web scraping of Wolt restaurant listings
✨ Multi-establishment price comparison
✨ CSV data persistence
✨ CLI interface for pizza-specific searches
✨ Basic GUI implementation (WIP)

## Technical Requirements
-----------------------

### Dependencies

Python 3.x
• requests (HTTP requests)
• beautifulsoup4 (HTML parsing)
• pandas (data manipulation)
• tkinter (GUI)

### Installation

```bash
pip install -r requirements.txt
```

## Usage
-----

### Command Line Interface

Run the script:
```bash
python main.py
```
Enter pizza type when prompted
View sorted price comparisons in console

### GUI Interface (Limited Functionality)

⚠️ **Important:** Must be launched from `main.py`. Direct GUI execution unsupported.

```bash
python main.py
```

## Implementation Details
----------------------

Four main modules:

1. Data Fetcher
   - Wolt restaurant page scraping
   - Pizza name and price extraction
   - Pagination handling
   - Rate limiting implementation

2. Data Writer
   - CSV storage management
   - Data consistency maintenance
   - File operations handling

3. Data Analyzer
   - Price comparison processing
   - Pizza type filtering
   - Results sorting

4. GUI Interface
   - Visual interface provision
   - Searchable result display
   - Tabular price comparison view

## Known Limitations
-------------------

1. GUI Integration
   - Requires main.py launch
   - Full integration pending
   - Some UI elements unresponsive

2. Web Scraping
   - Dependent on Wolt structure
   - Vulnerable to layout changes
   - No rate limiting implemented

## Future Improvements
--------------------

1. Complete GUI Integration
2. Error Handling
3. Rate Limiting
4. Restaurant Filtering
5. Visual Price Trends

## Academic Context
-----------------

Demonstrates key programming concepts:
- BeautifulSoup web scraping
- Pandas data processing
- Tkinter GUI development
- Modular program design
- Error handling and debugging

## License
-------

MIT Licensed. See [LICENSE](LICENSE) for details.

## Acknowledgments
---------------

Thanks to:
- University instructor
- Open-source contributors
- Wolt for accessible data