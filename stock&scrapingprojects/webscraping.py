from bs4 import BeautifulSoup
import requests

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, 'html5lib')

# print(soup.prettify())

tag_object = soup.title
tag_object = soup.h3
tag_child =tag_object.b
# print(tag_child.parent)
# sibling = tag_child.next_sibling
# print("tag object:",tag_object)

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, 'html5lib')
table_rows = table_bs.find_all('tr')
# print(table_rows[0])
for i,row in enumerate(table_rows):
    # print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        # print('colunm',j,"cell",cell)
        a = 1
        
url = "http://www.ibm.com"
data = requests.get(url).text
soup = BeautifulSoup(data, 'html5lib')
for link in soup.find_all('a', href=True):
    print(link.get('href'))
for link in soup.find_all('img'):
    print(link)
    print(link.get('src'))

print("1"==1)