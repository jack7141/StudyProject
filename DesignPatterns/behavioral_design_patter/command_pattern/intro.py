"""
요구 사항
명령어 형태로 사칙연산을 수행하고 그 결과를 출력하라

결과
result = 0
result + 20 = 20
result - 10 = 10
result * 10 = 100
result / 10 = 10

구현 순서 사칙연산을 수행하는 명령어 클래스를 만든다.
"""
from abc import ABCMeta, abstractmethod


class AbstarctOperationCommand(metaclass=ABCMeta):
    """객체의 행동을 제어하기 위해 명령 인터페이스를 선언한다."""
    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value

    @abstractmethod
    def execute(self):
        pass

class AddOperationCommand(AbstarctOperationCommand):

    def __init__(self, receiver, value):
        AbstarctOperationCommand.__init__(self, receiver, value)

    def execute(self):
        self.receiver.add(self.value)


class SubstractOperationCommand(AbstarctOperationCommand):

    def __init__(self, receiver, value):
        AbstarctOperationCommand.__init__(self, receiver, value)

    def execute(self):
        self.receiver.substarct(self.value)

class MultiplyOperationCommand(AbstarctOperationCommand):

    def __init__(self, receiver, value):
        AbstarctOperationCommand.__init__(self, receiver, value)

    def execute(self):
        self.receiver.multiply(self.value)


class DivideOperationCommand(AbstarctOperationCommand):

    def __init__(self, receiver, value):
        AbstarctOperationCommand.__init__(self, receiver, value)

    def execute(self):
        self.receiver.divide(self.value)

class OperationCommandReceiver:
    """Receiver의 역할, 사칙연산의 연산 명령 객체를 받아들인다.
    """
    def __init__(self):
        self.result = 0

    def get_result(self):
        return self.result

    def add(self, value):
        self.result += value

    def substract(self, value):
        self.result -= value

    def multiply(self, value):
        self.result *= value

    def divide(self, value):
        self.result /= value

if __name__=='__main__':
    """사칙연산 명령을 생성하고 OperationCommandReceiver 객체를 설정한다.
    """
    receiver = OperationCommandReceiver()

    result = receiver.get_result()

    print('result=', result)

    add_command = AddOperationCommand(receiver, 20)
    add_command.execute()

    result = receiver.get_result()
    print('result=', result)

    add_command = DivideOperationCommand(receiver, 10)
    add_command.execute()

    result = receiver.get_result()
    print('result=', result)

    add_command = MultiplyOperationCommand(receiver, 20)
    add_command.execute()

    result = receiver.get_result()
    print('result=', result)
    """
    결과 
        result= 0
        result= 20
        result= 2.0
        result= 40.0
    """
