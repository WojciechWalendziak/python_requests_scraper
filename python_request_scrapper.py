import requests
import lxml
import csv
import pandas as pd
import openpyxl

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

try:
    table_to_excel = pd.DataFrame(data)

except:
    print('data frame failed')

try:
    table_to_excel.to_csv('wig20_index_csv.csv', index=False)

except:
    print('save to csv failed')

try:
    table_to_excel.to_excel('wig20_index_excel.xlsx', sheet_name='current_stock_data')
    
except:
    print('save to excel failed')
