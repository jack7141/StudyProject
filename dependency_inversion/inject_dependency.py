"""
Mixin이 실제 내가 사용하는 프로젝트에서 좋은 예시가 될거같다.
"""
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger()

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Fan(Switchable):
    def turn_on(self):
        logger.info(f"Fan: Turn On")

    def turn_off(self):
        logger.info(f"Fan: Turn Off")


class LightBulb(Switchable):
    def turn_on(self):
        logger.info(f"LightBulb: Turn On")

    def turn_off(self):
        logger.info(f"LightBulb: Turn Off")


class ElectricPowerSwitch:

    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


class Application:

    def start(self):
        l = LightBulb()
        f = Fan()
        switch = ElectricPowerSwitch(f)
        switch.press()
        switch.press()


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s-%(levelname)s] %(message)s',
                        level=logging.INFO)
    app = Application()
    app.start()