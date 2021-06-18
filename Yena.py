import urllib.request
import xml.dom.minidom as minidom

def get_data(xml_url):
    try:
        web_file = urllib.request.urlopen(xml_url)
        return web_file.read()
    except:
        pass


def get_currencies_dictionary(xml_content):

    dom = minidom.parseString(xml_content)
    dom.normalize()

    elements = dom.getElementsByTagName("Valute")
    currency_dict = {}

    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Value':
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data.replace(',', '.'))
                if child.tagName == 'CharCode':
                    if child.firstChild.nodeType == 3:
                        char_code = child.firstChild.data
        currency_dict[char_code] = value
    return currency_dict

def print_JPY_to_RUB_course(dict):
    for key in dict.keys():
        if key == 'JPY':
            print('Курс японской иены (JPY): 100 ¥ =', round(dict[key],2),'₽')


if __name__ == '__main__':
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    db_path = './ currencies.db'
    currency_dict = get_currencies_dictionary(get_data(url))
    print_JPY_to_RUB_course(currency_dict)