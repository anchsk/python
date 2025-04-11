from bs4 import BeautifulSoup

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')

# print(soup.prettify())
tag_object = soup.title
print(tag_object, '\n', 'Tag object type: ', type(tag_object))

parent_tag = tag_object.parent
print(parent_tag)
# <head><title>Page Title</title></head>

tag_object = soup.h3
child_tag = tag_object.b
print(child_tag)
# <b id="boldest">Lebron James</b>

sibling_1 = tag_object.next_sibling
sibling_2 = sibling_1.next_sibling
print(sibling_1, sibling_2)

print(child_tag.attrs)
# {'id': 'boldest'}


# Navigable string
tag_string = child_tag.string
print('tag_string type: ', type(tag_string))
# <class 'bs4.element.NavigableString'>

unicode_string = str(tag_string)
print(unicode_string)

table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, 'html5lib')
table_rows = table_bs.find_all('tr')
print(table_rows)

for i, row in enumerate(table_rows):
    print("row", i, "is", row)
    cells = row.find_all('td')
    for j, cell in enumerate(cells):
        print('colunm', j, "cell", cell)

list_input = table_bs.find_all(name=["tr", "td"])
print('list_input: ', list_input[0])

# .find_all(name=["tr", "td"])
# (id="flight")
# (href=True)
# (href=False)

# (string="Florida")


# .find 

