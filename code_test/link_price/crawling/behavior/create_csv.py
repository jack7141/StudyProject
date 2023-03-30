import csv
import os

current_dir = os.getcwd()
file_path = os.path.join(current_dir, './naver_store_data.csv')

def create_csv(data):
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['쇼핑몰명', '몰등급', '상품개수', '스토어찜수', '카테고리', '네이버페이', '네이버페이플러스', '몰설명', '로고이미지'])
        for row in data:
            writer.writerow(row)