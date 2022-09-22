# Dependency inversion
의존성 주입

## 용어 정리
* 결합도 - 모듈과 모듈간의 상호 의존정도
> 결합도는 모듈 내부가 아닌 `외부의 모듈`과의 연관도 또는 모듈 간의 상호의존성을 나타내는 정도
* 응집도 - 모듈 내부의 기능적인 집중정도
> 작은 기능 단위들을 `모듈화`하여 유지 보수와 타 프로그램에서의 코드 재사용성을 손쉽게 하고자함

## 목적
* 결합도는 낮추고 응집도를 높여서, 유지 보수가 쉽고 변경에 용이하게 한다.


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
   [Code Link]: <https://www.youtube.com/watch?v=Kv5jhbSkqLE>
