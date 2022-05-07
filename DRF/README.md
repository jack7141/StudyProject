# Django DRF API for Custom Django Server
나만의 Django Template 만들기 
---
## Tech
* [Django] - Python web FrameWork
* [Django Rest Framework] - RESTFul Web API
## System Requirements
* [python] - 3.10
## Secrets.json File Setting
```sh
{
  "SECRET_KEY": '[https://djecrety.ir/]',
  "DATABASES": {
      "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "db-table-name",
        "USER": "root",
        "PASSWORD": "my-password",
        "HOST": "127.0.0.1",
        "PORT": "3306"
      }
    }
}
- Django Secret Key 발급 후 secrets.json에 추가
```
> 각 설정 파일의 정의는 `settings`폴더에 들어있으며, 비밀번호와 같은 노출되면 위험한 설정값의 경우 `프로젝트`폴더의 최상위 경로 `secrets.json` 파일에 정의 합니다.
## Server RUN
```
- local
$ python manage.py migrate --settings=[프로젝트명].settings.local
$ python manage.py runserver --settings=[프로젝트명].settings.local

- deploy
$ python manage.py migrate --settings=[프로젝트명].settings.deploy
$ python manage.py runserver --settings=[프로젝트명].settings.deploy
```

서버 실행 후, 사용하는 브라우저에 서버 주소를 입력하여 동작을 확인합니다.

```sh
http://127.0.0.1:8000
```

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [fount logo]: <https://fount.co/wp-content/uploads/2017/07/fount-ci@2x.png>
   [python]: <https://www.python.org/>
   [Django]: <https://www.djangoproject.com/>
   [Django Rest Framework]: <http://www.django-rest-framework.org/>
   [Django Rest Swagger]: <https://django-rest-swagger.readthedocs.io>