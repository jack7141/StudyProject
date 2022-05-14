FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN apt update && apt install nano
# 현재 디렉토리 > 도커 컨테이너 DRF로 마운트
ADD . /DRF

WORKDIR /DRF

RUN pip install -r requirements.txt && pip install django-filter

#CMD ["python manage.py runserver --settings=conf.settings.local"]
