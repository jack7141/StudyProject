## 환경
---
    1. AWS EC2
    2. DB: MYSQL
    3. DockerFile 이용
    4. FastAPI 이용

## 설치
---
    1. git clone
    2. 가상환경 구축
    3. pip install -r requirements.txt

## EC2 주소
---

    * http://18.208.137.166

    [Swagger 주소]
    *  http://18.208.137.166/docs


## API 명세
---
    Method          URL           Description

    POST             /              회사 생성
    GET              /              회사 List 

    GET           /search/company_name_ko/{name} 한국회사 검색
    GET           /search/company_name_en/{name} 미국회사 검색
    GET           /search/company_name_ja/{name} 일본회사 검색

