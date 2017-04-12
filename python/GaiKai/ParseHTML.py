"""
 pip install lxml and pip install requests.
 pip install json


"""

from lxml import html
import requests
import json

#page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
page = requests.get('http://www.metacritic.com/game/playstation-3')

tree = html.fromstring(page.content)


#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')



print 'Buyers: ', buyers
print 'Prices: ', prices

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
parsed_json = json.loads(json_string)






json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print json.dumps("\"foo\bar")

