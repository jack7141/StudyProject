from bs4 import BeautifulSoup
from code_test.link_price.crawling.web_crawler import get_html
from code_test.link_price.crawling.behavior.file_cache import load_cache, save_cache
from code_test.link_price.crawling.behavior.create_csv import create_csv
from code_test.link_price.crawling.behavior.factory import extract_mall_info

def execute(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    malls = soup.find_all('li', {'class': 'mallListItem_item_mall__HUZQH'})
    data = [extract_mall_info(mall) for mall in malls]
    create_csv(data)

if __name__ == "__main__":

    html_data = load_cache('html_data')

    if html_data is None:
        html_data = get_html()
        save_cache('html_data', html_data)

    execute(html_data=html_data)