# React Study

* ReactJS 규칙 
1. HTML을 직접 작성하지 않는다


* JSX란?

   => HTML을 REACTJS스타일로 처리함 이때 변화를 주기위해서 쓰는게 Babel이다

* Function
    
    function 네임(){return();} == const 네임 = () => ();

    두개가 동일함!!
    
* State -> array (useState를 사용하면 해당 컴포넌트 전체가 재생성된다.)
  
  값이 바뀔때마다 새로 렌더링 해야하는 문제가 있기때문에, setState로 자동으로 render하는것을 도와준다.

    state를 수정하는 방법

    * setCounter(변수 + 1) == setCounter((인자) => 인자 + 1)
    1. 왼쪽 방식은 useState에서 설정한 변수값을 직접적으로 건드리는 방식
    2. 오른쪽 방식은 useState에서 설정한 함수를 통해서 return을 받아서 변수를 수정하는 방식

    후자의 방식을 채택하는 것이 좋은점은 인자를 넣었을때 확실히 지금 현재의 값임을 보장한다.(현재 state를 바탕으로 다음 state를 계산하고자 할때!)

* Prop Types[타입 검사]

  => Debug를 좀더 편하게끔 하기위한 장치



# ReactJS 시작

