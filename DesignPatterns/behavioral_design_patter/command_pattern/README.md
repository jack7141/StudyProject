# The command pattern
커멘드 패턴

## 용어 정리
* 커멘드 패턴(command pattern)
> 구성 요소
1. command
 * 객체의 행동을 제어하기 위한 명령을 위한 인터페이스를 선언한다.
 * execute()라는 단 하나의 메서드를 선언한다.
 * 되돌리기(undo)와 재실행하기(redo) 명령들을 지원해야 하는 경우도 있다.

2. ConcreteCommend
 * Command의 인터페이스를 실제로 구현한다.
 * 수신자(Receiver)를 필요로 한다.

3. Reciver
 * 명령을 받아들이는 객체이다.
 * 요구 사항을 수행하기 위해 어떤 일을 처리해야 하는 지 알고 있는 객체이다.

4. Client
 * ConcreteCommand를 생성하고 Receiver를 설정한다.
 * Command 객체를 초기화한다.

5. Invoker
 * 실행할 명령을 가지고 있다.
 * Command의 execute() 메서드를 호출함으로써 Command 객체에서 특정 작업을 수행해 달라는 요구를 한다.



## 사용 효과
* 객체의 행동을 별도의 클래스에 캡슐화해서 행동 객체에 확장성을 부여한다.
* 각각의 커맨드들은 특정 객체에 의존하지 않도록 만들어지므로 재활용성이 매우 높다
* 어떤 작업을 요청한 쪽하고 그 작업을 처리한 쪽을 분리시킬 수 있다.

## 사용예
* 스케줄러, 스레드 풀, 작업 큐
* 포토샵의 히스토리(작업내역) 기능
* 프로그램의 undo/redo 기능


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
