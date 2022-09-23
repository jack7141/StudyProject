import logging

logger = logging.getLogger()

class LightBulb:

    def turn_on(self):
        logger.info(f"LightBulb: Turn On")

    def turn_off(self):
        logger.info(f"LightBulb: Turn Off")

class ElectricPowerSwitch:

    def __init__(self, l: LightBulb):
        self.lightBulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightBulb.turn_off()
            self.on = False
        else:
            self.lightBulb.turn_on()
            self.on = True


class Application:

    def start(self):
        l = LightBulb()
        switch = ElectricPowerSwitch(l)
        switch.press()
        switch.press()


if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s-%(levelname)s] %(message)s',
                        level=logging.INFO)
    app = Application()
    app.start()