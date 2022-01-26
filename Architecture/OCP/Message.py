'''
# 좋지 못한 예시

class Message:
    """Message 추상 클래스"""
    def __init__(self, data):
        self.data = data

class FirstGradeMessage(Message):
    """FirstGrade에 대한 메세지 처리 클래스"""

class SecondGradeMessage(Message):
    """SecondGrade에 대한 메세지 처리 클래스"""

class ThirdGradeMessage(Message):
    """ThirdGrade에 대한 메세지 처리 클래스"""

class DefaultGradeMessage(Message):
    """DefaultGrade에 대한 메세지 처리 클래스"""

class GradeMessageClassification():
    """Grade에 따른 메세지 분류 클래스"""
    def __init__(self, data):
        self.data = data

    def classification(self):
        if(self.data['grade'] == 1):
            return FirstGrade(self.data)
        elif(self.data['grade'] == 2):
            return SecondGrade(self.data)
        elif(self.data['grade'] == 3):
            return ThirdGrade(self.data)
        else:
            return DefaultGrade(self.data)

* 이 경우 FourGradeMessage가 추가되면, elif문을 추가해야한다. 즉, 위 방법은 기존의 코드를 수정하는 방식이기 때문에 닫혀있지 못한 예시가
된다.
이를 방지하기 위해 하단의 방식으로 재구성하여 설게한다.
'''


'''
* 아래의 코드에서 시사하는 바는 최상위 class와 __subclass__메소드를 사용하여 같은 작업을 할 시 분개를 태워 손쉽게 OCP하게 만들어준다.
'''
class Message:
    '''
    * Message 추상 클래스
    '''
    def __init__(self, Grade):
        self.grade = Grade

    # @staticmethod
    # def is_collect_grade_message(**data: dict):
    #     return False


class FirstGradeMessage(Message):
    '''
    * 1학년 메세지 처리 클래스
    '''

    @staticmethod
    def is_collect_grade_message(**data: dict):
        return data['grade'] == 1

class SecondGradeMessage(Message):
    '''
    * 2학년 메세지 처리 클래스
    '''

    @staticmethod
    def is_collect_grade_message(**data: dict):
        return data['grade'] == 2

class ThirdGradeMessage(Message):
    '''
    * 3학년 메세지 처리 클래스
    '''

    @staticmethod
    def is_collect_grade_message(**data: dict):
        return data['grade'] == 3

class DefaultGradeMessage(Message):
    '''
    * DefaultGrade에 대한 메세지 처리 클래스
    '''


class GradeMessageClassification:
    '''
    * Grade에 따른 메세지 분류 클래스
    '''

    def __init__(self, data):
        self.data = data

    def classification(self):
        '''
        * 클래스의 메소드 __subclasses__를 사용하면, 상속받은 클래스를 모두 확인할 수 있다.
        '''
        for grade_message_subcls in Message.__subclasses__():
            try:
                if grade_message_subcls.is_collect_grade_message(grade=self.data):
                    return grade_message_subcls(self.data)
            except KeyError:
                continue

            return DefaultGradeMessage(self.data)




