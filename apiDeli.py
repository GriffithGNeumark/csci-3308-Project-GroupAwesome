import urllib2
import json

deli_api = 'YmEwNDkzOTJhNTJjZGM1NmIzYTBlY2QxMGQ5ZTRmODhk'

def menu_search(merchant_id):
        api_key = deli_api
        url = 'https://api.delivery.com/merchant/' + merchant_id + '/menu?client_id=' + api_key
        obj = urllib2.urlopen(url)
        data = json.load(obj)

        for item in data['menu']:
                for item2 in item['children']:
					for item3 in item2['children']:
						print item3['name']
        	
def deli_search(query):
        api_key = deli_api
        url = 'https://api.delivery.com/merchant/search/delivery?client_id=' + api_key + "&address=" + query
        obj = urllib2.urlopen(url)
        data = json.load(obj)

        for item in data['merchants']:
                menu_search(item['id'])


def main():
        Loc = raw_input("Where would you like to search")
        deli_search(Loc)

main()
