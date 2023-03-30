def get_mall_info(mall):
    etc_divs = mall.find_all('div', {'class': 'mallListItem_etc__d1uj4'})
    store_info = etc_divs[0].get_text().split(' ')
    mall_rank = "None"
    store_point = 0
    if len(etc_divs) > 1:
        mall_rank = store_info[0][:-5]
        store_point = store_info[1]
    etc = etc_divs[-1].get_text().split(' ')
    items = etc[1]
    category = etc[0][:-4]
    return mall_rank, store_point, items, category


def check_naver_pay(mall):
    naver_pay = "N"
    naver_pay_plus = "N"

    npay = mall.find('span', {'class': 'mallListItem_ico_npay__XwDQC'})
    if npay is not None:
        naver_pay = "Y"

    npay_plus = mall.find('span', {'class': 'mallListItem_ico_npay_plus__LhnFO'})
    if npay_plus is not None:
        naver_pay_plus = "Y"

    return naver_pay, naver_pay_plus

def extract_mall_info(mall):
    title = mall.find('strong', {'class': 'mallListItem_title__zS_zf'}).get_text()
    desc = mall.find('p', {'class': 'mallListItem_desc__FIARs'}).get_text()
    thumbnail = mall.find('img')['src']
    naver_pay, naver_pay_plus = check_naver_pay(mall)
    mall_rank, store_point, items, category = get_mall_info(mall)
    return [title, mall_rank, items, store_point, category, naver_pay,  naver_pay_plus, desc, thumbnail]