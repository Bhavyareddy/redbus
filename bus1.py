import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.redbus.in/Booking/SelectBus.aspx?fromCityId=124&toCityId=122&doj=24-Aug-2016&busType=Any&opId=0'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,"html5lib")
table = soup.find('ul', attrs={'class': 'DropList FBorder XSmall Hide'})
# import pdb; pdb.set_trace()
list_of_rows = []
for row in table.findAll('li'):
    for cell in row.findAll('a'):
    	list_of_cells = []
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
# import pdb; pdb.set_trace()
    
    list_of_rows.append(list_of_cells)

# outfile = open("./inmates.csv", "wb")
# writer = csv.writer(outfile)
# writer.writerows(list_of_rows)
print list_of_rows
