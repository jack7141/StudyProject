import string
import random
import logging

logger = logging.getLogger()

class VehicleRegistry:
    """자동차 id, 번호판을 생성합니다.
    """
    def generate_vehicle_id(self, length):
        """자동차 번호를 난수의 알바벳으로 생성합니다.

        example

        >>> HWKQNMVHCOHA

        """
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        """자동차 번호를 난수의 알바벳과 숫자로 생성합니다.

        example

        >>> FG-21-KF

        """
        return f'{id[:2]}-{"".join(random.choices(string.digits, k=2))}-{"".join(random.choices(string.ascii_uppercase, k=2))}'


class Application:

    def register_vehicle(self, brand: string):
        registry = VehicleRegistry()
        vehicle_id = registry.generate_vehicle_id(12)
        license_plate = registry.generate_vehicle_license(vehicle_id)

        catalogue_price = 0
        if brand == "BMW 5":
            catalogue_price = 60_000
        elif brand == "Tesla Model 3":
            catalogue_price = 100_000
        elif brand == "Volkswagen ID3":
            catalogue_price = 20_000

        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        payable_tax = tax_percentage * catalogue_price
        logger.info(f"============================================")
        logger.info(f"Registration complete. Vehicle Information:")
        logger.info(f"Brand: {brand}")
        logger.info(f"Id: {vehicle_id}")
        logger.info(f"License plate: {license_plate}")
        logger.info(f"Payable tax: {payable_tax}")
        logger.info(f"============================================")

if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s-%(levelname)s] %(message)s',
                        level=logging.INFO)
    app = Application()
    app.register_vehicle('BMW 5')