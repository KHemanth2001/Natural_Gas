# Cores Data Extractor

This Python script utilizes the Selenium library to extract data from the website [https://www.cores.es/en/estadisticas](https://www.cores.es/en/estadisticas) provided by Cores (Spanish Corporation of Strategic Reserves). The website offers statistical data on various energy-related topics.

## Prerequisites

1. Python 3.x installed on your system.
2. Install required packages by running `pip install selenium`.

## Webdriver Setup

1. Download the appropriate WebDriver for your browser:
   - Chrome: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - Firefox: [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

2. Place the WebDriver executable in the same directory as the Python script.

## Configuration

Open the Python script `cores_data_extractor.py` and modify the following variables as per your environment:

```python
output_csv_file = "output_data.csv"
```

Set the `output_csv_file` variable to the desired name for the CSV file where the extracted data will be stored. By default, it will be saved in the same directory as the script.

## Running the Script

Run the Python script `cores_data_extractor.py`:

```bash
python cores_data_extractor.py
```

The script will use Selenium to navigate to the [https://www.cores.es/en/estadisticas](https://www.cores.es/en/estadisticas) website, extract data from the tables, and dynamically store the data in the specified CSV file.

## Important Notes

- Ensure that you have the necessary permissions to access and extract data from the website.
- Always comply with the terms of service and usage policies of the website.
- Use this script responsibly and avoid causing any load or strain on the website's server.

Feel free to explore and modify the script according to your specific requirements for data extraction. Happy coding!
