# The Bridge Pattern
브릿지 패턴

## 용어 정리
* 구현부에서 추상층을 분리하여 각자 독립적으로 변형이 가능하고 확장이 가능하도록 합니다. 즉 기능과 구현에 대해서 두 개를 별도의 클래스로 구현을 합니다.


## 장점
* 구현할 인터페이스에 완전히 결합시키지 않았기 때문에 구현과 추상화된 부분을 분리시킬 수 있습니다
* 추상화된 부분과 실제 구현 부분을 독립적으로 확장할 수 있습니다
* 추상화된 부분을 구현한 구상 클래스를 변경해도 클라이언트 쪽에는 영향을 미치지 않습니다.

## 단점
* 디자인이 복잡해진다.


## 사용된 언어
[python] 3.8이상 
 
## Code reference link
[Code Link] 해당 링크에서 코드를 확인할 수 있습니다.

## installation virtualenv
```sh
$ pip3 install virtualenv
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [fount logo]: <https://fount.co/wp-content/uploads/2017/07/fount-ci@2x.png>
   [python]: <https://www.python.org/>
   [Django]: <https://www.djangoproject.com/>
   [Django Rest Framework]: <http://www.django-rest-framework.org/>
   [Django Rest Swagger]: <https://django-rest-swagger.readthedocs.io>
   [Code Link]: <https://www.youtube.com/watch?v=t0mCrXHsLbI>
