import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# Get the webpage content
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Save the entire HTML content to a file
with open("flipkart_search_results.html", "w", encoding='utf-8') as file:
    file.write(soup.prettify())

# Extract relevant data
data = []
spans = soup.select("div.KzDlHZ")

for span in spans:
    if span.string:
        data.append(span.string)

# Save the extracted data to a CSV file
with open("flipkart_data.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Text"])
    for item in data:
        writer.writerow([item])

print("Data has been extracted and saved successfully.")
