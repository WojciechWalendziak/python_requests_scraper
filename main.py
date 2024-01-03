import requests
import lxml
import csv
import pandas as pd

website = requests.get('https://www.bankier.pl/gielda/notowania/akcje').text

from bs4 import BeautifulSoup
soup = BeautifulSoup(website, 'lxml')

table = soup.find('table')
table_rows = table.findAll('tr')

data = []
for tr in table_rows:
    td = tr.findAll('td')
    rows = [i.text for i in td]
    data.append(rows)

# Export the data to a CSV file
with open('twitter_accounts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print("Data has been saved to CSV file successfully!")
