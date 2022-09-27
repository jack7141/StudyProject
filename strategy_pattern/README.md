# The strategy pattern
전략패턴

## 용어 정리
* 전략 패턴(strategy pattern) 또는 정책 패턴(policy pattern) - 실행 중에 알고리즘을 선택할 수 있게 하는 행위 소프트웨어 디자인 패턴이다. 전략 패턴은 특정한 계열의 알고리즘들을 정의하고 각 알고리즘을 캡슐화하며 이 알고리즘들을 해당 계열 안에서 상호 교체가 가능하게 만든다.
> 한 과일 매장은 상황에 따라 다른 가격 할인 정책을 적용하고 있습니다. 제일 먼저 온 손님에게 10%를 할인해주고 마지막 손님은 20% 그리고 신선도가 떨어진 과일에 대해서는 20% 할인을 해주고 있습니다. 이러한 상황을 가정하고 이를 구현하는 예시


## 장점
* 전략패턴을 적용할때의 이점은 컨텍스트 코드의 변경 없이 새로운 전략을 추가할 수 있다는 점입니다.


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
   [Code Link]: <https://www.youtube.com/watch?v=WQ8bNdxREHU&t=800s>
