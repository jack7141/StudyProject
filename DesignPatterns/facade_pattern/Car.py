from DesignPatterns.facade_pattern.Brake import Brake
from DesignPatterns.facade_pattern.Engine import Engine
from DesignPatterns.facade_pattern.Frame import Frame
from DesignPatterns.facade_pattern.Suspension import Suspension
from DesignPatterns.facade_pattern.Transmission import Transmission
from DesignPatterns.facade_pattern.WheelAssembly import WheelAssembly


class Car(object):
    """
    * 자동차 구성 - 퍼사드 패턴
    """
    def __init__(self, model, manufacturer) -> None:
        self.engine = Engine('BMW 330e', 85, 5000, 1.3)
        self.frame = Frame(385, 170)
        self.wheel_assemblies = []

        for i in range(4):
            self.wheel_assemblies.append(WheelAssembly(Brake(i+1), Suspension(1000)))
            self.transmission = Transmission(5, 115)
            self.model = model
            self.manufacturer = manufacturer
            # 점화 장치
            self.ignition = False

    def start(self):
        """
        * 시동 ON
        """
        print('자동차 운행 시작')
        # 점화 장치
        self.ignition = True
        # self.park_brake.release()
        self.engine.start()
        self.transmission.shift_up()
        print('시동이 걸렸습니다.')

    def stop(self):
        print('운행을 종료합니다.')
        # 감속
        for wheel_a in self.wheel_assemblies:
            wheel_a.apply_brakes()

        # Move to 2nd gear and then 1st
        self.transmission.shift_to(2)
        self.transmission.shift_to(1)
        self.engine.stop()

        # shift to neutral
        self.transmission.shift_to(0)

        # Engage parking brake
        print('자동차 운행종료 완료')


if __name__ == '__main__':
    car = Car('람보르기니', '이탈리아')
    print(car)
    print(car.start())
    print(car.stop())