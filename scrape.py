from bs4 import BeautifulSoup
import requests

# Get the HTML souce from the website link
source = requests.get('https://egypt.souq.com/eg-en/dell-xps-15-7590-15-6-inch-4k-uhd-3840x2160-oled-infinityedge-anti-reflective-display-intel-i7-9750h-9th-gen-nvidia-gtx-1650-4gb-gddr5-32gb-ddr4-ram-1tb-ssd-pcie-nvme-fingerprint-reader-wi-fi-ax-bluetooth-5-0-english-backlit-keyboard-windows-1-131826972/i/').text

# Parse the XML using the lxml library
soup = BeautifulSoup(source, 'lxml')

# Get the product title
title = soup.find('div', class_='product-title').h1.text
print(title)

# Get currency
currency = soup.find('span', class_='currency-text').text
print(currency)

# Get and trim the product price without the currency
price = soup.find('h3', class_='price').text
stringPrice = price.strip().split(currency)[0].strip()
print(stringPrice)

# Convert The number to float to use in your logic
floatPrice = float(stringPrice.strip().replace(',',''))
print(floatPrice)

# Get the product image src
image = soup.find('div', class_='img-bucket').img['src']
print(image)

