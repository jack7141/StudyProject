class Transmission(object):
    """
    * 자동차 트랜스미션 클래스를 정의한다.
    """
    def __init__(self, gear, torque) -> None:
        self.gear = gear
        self.torque = torque
        self.gear_pos = 0

    def shift_up(self):
        """
        * 기어 업!
        """
        if self.gear_pos == self.gear:
            print('기어를 올릴 수 없습니다.')
        else:
            self.gear_pos += 1
            print(f'Shift up to gear -> {self.gear_pos}')

    def shift_down(self):
        """
        * 기어 다운!
        """
        if self.gear_pos == -1:
            print('후진 상태입니다. 더 기어를 내릴 수 없습니다.')
        else:
            self.gear_pos -= 1
            print(f'Shifted down to gear -> {self.gear_pos}')

    def shift_reverse(self):
        """
        * 후진
        """
        print('후진')
        self.gear_pos = -1

    def shift_to(self, gear):
        """
        * 기어를 변동합니다.
        """
        self.gear_pos = gear
        print(f'현재 기어를 {self.gear_pos}로 변동합니다.')
