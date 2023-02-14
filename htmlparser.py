from bs4 import BeautifulSoup
from  grammar_config import html_table

soup = BeautifulSoup(html_table, 'html.parser')
table = soup.find('table')

# Extract the headers from the table
headers = [header.text for header in table.find('thead').find_all('th')][4:]


# Extract the data from the table
rows = []
for row in table.find('tbody').find_all('tr'):
    cells = [cell.text.replace("\xa0","err") for cell in row.find_all('td')]
    rows.append(cells)
table=rows

def get_productions(grammar):
    productions=[]
    for i in grammar.split('\n')[:-1]:
        i=i.split(' ')
        del i[1]
        productions.append(i)
    return productions

# Print the results
# print(headers[4:])
# for row in rows:
#     print(row)

#can remove state column:  row[i] : i state
