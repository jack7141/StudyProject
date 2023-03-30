from selenium import webdriver
import time

def get_html():
    # webdriver 설정
    options = webdriver.ChromeOptions()
    options.add_argument('headless') # 브라우저 창을 띄우지 않고 실행
    options.add_argument('disable-gpu') # GPU 사용 안함
    options.add_argument('lang=ko_KR') # 언어 설정

    driver = webdriver.Chrome('chromedriver', options=options) # 드라이버 생성
    driver.implicitly_wait(3) # 암묵적 대기

    # 페이지 이동
    url = 'https://search.shopping.naver.com/allmall'
    driver.get(url)

    # 페이지 스크롤 다운
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # 페이지 소스 받아오기
    html = driver.page_source
    # 드라이버 종료
    driver.quit()

    return html