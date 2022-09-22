import string
import random
import logging
from dataclasses import dataclass

logger = logging.getLogger()

@dataclass
class VehicleInfo:
    brand: str
    electric: bool
    catalogue_price: int

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self):
        logger.info(f"============================================")
        logger.info(f"Registration complete. Vehicle Information:")
        logger.info(f"Brand: {self.brand}")
        logger.info(f"Payable tax: {self.compute_tax()}")


@dataclass
class Vehicle:
    """자동차 클래스

    __init__
        id: 자동차 ID
        license_plate: 자동차 번호
        info: VehicleInfo class(자동차 정보 클래스)

    """
    id: str
    license_plate: str
    info: VehicleInfo

    def print(self):
        # VehicleInfo dataclass의 내부 print() 함수 콜
        self.info.print()
        logger.info(f"Id: {self.id}")
        logger.info(f"License plate: {self.license_plate}")
        logger.info(f"============================================")


class VehicleRegistry:
    """자동차 id, 번호판을 생성합니다.
    """
    vehicle_info = dict()

    def __init__(self):
        self.add_vehicle_info("BMW 5", True, 60_000)
        self.add_vehicle_info("Tesla Model 3", True, 100_000)
        self.add_vehicle_info("Volkswagen ID3", False, 20_000)

    def add_vehicle_info(self, brand, electric, catalogue_price):
        """
        self.vehicle_info[brand]

        Example

        vehicle_info = {
                BMW 5 : VehicleInfo(brand='BMW 5', electric=True, catalogue_price=60000)
                Tesla Model 3 : VehicleInfo(brand='Tesla Model 3', electric=True, catalogue_price=60000)
                Volkswagen ID3 : VehicleInfo(brand='Volkswagen ID3', electric=True, catalogue_price=60000)
        }
        """

        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f'{id[:2]}-{"".join(random.choices(string.digits, k=2))}-{"".join(random.choices(string.ascii_uppercase, k=2))}'

    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Application:
    """Entry Point"""
    def register_vehicle(self, brand: string):
        registry = VehicleRegistry()
        return registry.create_vehicle(brand)



if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s-%(levelname)s] %(message)s',
                        level=logging.INFO)

    app = Application()
    vehicle = app.register_vehicle('Volkswagen ID3')
    vehicle.print()

"""
[로그 정보]
[2022-09-22 22:36:41,773-INFO] ============================================
[2022-09-22 22:36:41,773-INFO] Registration complete. Vehicle Information:
[2022-09-22 22:36:41,773-INFO] Brand: Tesla Model 3
[2022-09-22 22:36:41,773-INFO] Payable tax: 2000.0
[2022-09-22 22:36:41,773-INFO] Id: PGQCRHEJPNUE
[2022-09-22 22:36:41,773-INFO] License plate: PG-27-QT
[2022-09-22 22:36:41,773-INFO] ============================================

"""