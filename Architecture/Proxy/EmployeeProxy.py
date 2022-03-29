class EmployeeProxy(object):
    """
    * Employee 클래스의 인스턴스를 카운팅하기 위해서 만들어진 Proxy 클래스(대리자)
    """

    # Count of Employee
    count = 0
    # __init__과의 차이는 __new__ 메소드는 메모리에 객체를 할당하지만 
    # __init__ 메소드는 메모리에는 할당하지 않는다. 
    def __new__(cls, *args):
        """
        new 메소드를 활용하여, 메모리에 올려준다.
        """
        instance = object.__new__(cls)
        cls.incr_count()
        return instance
    
    def __init__(self, employee):
        self.employee = employee

    # 클래스 메소드를 사용하는 이유는 => 클래스가 생성될때 인스턴스의 갯수를 증가를 확인하기 위해서 생성자가 아닌 
    # 클래스 최상위 속성에 두었기 때문에 클래스의 최상위 속성으로 접근하기 위해서 classmethod를 사용했다.
    @classmethod
    def incr_count(cls):
        """
        * employee 클래스 인스턴스 count UP
        """
        cls.count += 1

    @classmethod        
    def decr_count(cls):
        """
        * employee 클래스 인스턴스 count down
        """
        cls.count -= 1

    @classmethod        
    def get_count(cls):
        """
        * employee 클래스 인스턴스 count
        """
        return cls.count 

    def __str__(self):
        return str(self.employee)


    def __getattr__(self, name):
        """
        * 메소드는 인스턴스 속성으로 존재하지 않을때 (즉, 인스턴스 딕셔너리에 없을때)만 호출된다.
        다시말해, 존재하는 속성에 접근할 때는 호출되지 않는다.
        """
        return getattr(self.employee, name)

    def __del__(self):
        """
        * 소멸자
        """
        # 소멸되면 인스턴스 카운트를 하나 줄여준다.
        self.decr_count()