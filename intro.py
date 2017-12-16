import requests
import xml.etree.ElementTree as ET
from db import DB

class Aggregate(object):
    def aggregate(self):
        database = DB()
        sources = database.get_sources()
        finalitems = []
        for url,category in sources:
            items = self.fetch_items(url)
            finalitems.extend(items)
            database.insert_news(items, category)

        print(len(finalitems))

    def fetch_items(self, url):
        items = []
        res = requests.get(url)
        content = res.text
        root = ET.fromstring(content)
        for child in root:
            #there is only one child for root --> channel
            for item in child.findall('item'):
                i = {}
                for elem in item:
                    if elem.tag == 'title':
                        i['title'] = str(elem.text).encode('utf-8').decode()
                    if elem.tag == 'description':
                        i['description'] = str(elem.text).encode('utf-8').decode()
                    if elem.tag == 'link':
                        i['link'] = str(elem.text).encode('utf-8').decode()
                if i:
                    items.append(i)
        return items


if __name__=='__main__':
    aggregator = Aggregate()
    aggregator.aggregate()
