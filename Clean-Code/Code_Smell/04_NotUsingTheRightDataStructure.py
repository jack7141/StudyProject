"""
* 출처 - https://www.youtube.com/watch?v=zmWf_cHyo8s&t=571s
"""
import datetime
from dataclasses import dataclass
from enum import Enum, auto
from random import *
from string import *
from typing import Optional, Tuple


class FuelType(Enum):
    """자동차 연료 타입"""

    ELECTORIC = auto()
    PETROL = auto()

class RegistryStatus(Enum):
    """구매 방법"""

    ONLINE = auto()
    CONNECTION_ERROR = auto()
    OFFLINE = auto()

taxes = {FuelType.ELECTORIC: 0.02, FuelType.PETROL: 0.05}

@dataclass
class VehicleInfoMissingError(Exception):
    """자동차 정보 누락 에러 클래스"""

    brand: str
    model: str
    message: str = "자동차 정보 누락"

@dataclass
class VehicleModelInfo:
    """자동차 기본 모델 정보"""

    brand: str
    model: str
    catalogue_price: int
    # 클래스 내부에 default를 지정하여,
    # main에서 add_vehicle_model_info를 호출할 시, 파라미터를 줄인다.
    fuel_type: FuelType = FuelType.ELECTORIC
    launch_year: int = datetime.datetime.now().year

    @property
    def tax(self) -> float:
        """자동차 등록시 세금 타임"""
        tax_percentage = taxes[self.fuel_type]
        return tax_percentage * self.catalogue_price

    def get_info_str(self) -> str:
        """instance representation"""
        return f"brand: {self.brand} - type: {self.model} - tax: {self.tax}"

@dataclass
class Vehicle:
    """자동차 클래스"""

    vehicle_id: str
    license_plate: str
    info: VehicleModelInfo

    def to_string(self) -> str:
        """instance representation"""
        info_str = self.info.get_info_str()
        return f'ID: {self.vehicle_id}, License plate: {self.license_plate}, info: {info_str}'

@dataclass
class VehicleRegistry:
    """자동차 기본 등록 시스템"""

    def __init__(self) -> None:
        # 리스트 형식에서 튜블 dict으로 수정함
        self.vehicle_model: dict[Tuple[str, str], VehicleModelInfo] = {}
        self.online = True


    def add_vehicle_model_info(
            self,
            model_info: VehicleModelInfo
    ) -> None:
        """VehicleModelInfo object to a list"""
        # 리스트 형식에서 튜블 dict으로 수정함
        self.vehicle_model[(model_info.brand, model_info.model)] = model_info

    def generate_vehicle_id(self, length: int) -> str:
        """random vehicle id 생성"""
        return "".join(choices(ascii_uppercase, k=length))

    def generate_vehicle_license(self, _id: str) -> str:
        """generating a vehicle license number"""
        return f'{_id[:2]}-{"".join(choices(digits, k=2))}-{"".join(choices(ascii_uppercase, k=2))}'

    def find_model_info(self, brand: str, model: str) -> Optional[VehicleModelInfo]:
        """자동차 모델을 검출합니다. brand, info 키를 가지고 데이터를 찾을 수 있으며, None값도 허용되고, None도 반환될 수 있다
        print(self.vehicle_model.keys())
        >>> dict_keys([('Ferrai', 'Califonia'), ('Lambo', 'Urus'), ('Porsh', 'Frog'), ('Bentely', 'Model 3')])
        {
        ('Ferrai', 'Califonia'): VehicleModelInfo(brand='Ferrai', model='Califonia', catalogue_price=100000000, fuel_type=<FuelType.ELECTORIC: 1>, launch_year=2022),
        ('Lambo', 'Urus'): VehicleModelInfo(brand='Lambo', model='Urus', catalogue_price=600000000, fuel_type=<FuelType.ELECTORIC: 1>, launch_year=2022),
        ('Porsh', 'Frog'): VehicleModelInfo(brand='Porsh', model='Frog', catalogue_price=300000000, fuel_type=<FuelType.ELECTORIC: 1>, launch_year=2022),
        ('Bentely', 'Model 3'): VehicleModelInfo(brand='Bentely', model='Model 3', catalogue_price=600000000, fuel_type=<FuelType.ELECTORIC: 1>, launch_year=2022)
        }
        print(self.vehicle_model.get('Ferrai','Califonia'))
        >>> (VehicleModelInfo(brand='Ferrai', model='Califonia', catalogue_price=100000000, fuel_type=<FuelType.ELECTORIC: 1>, launch_year=2022)
        """
        return self.vehicle_model.get((brand, model))

    def register_vehicle(self, brand: str, model: str) -> Vehicle:
        """자동차를 새로 등록합니다."""
        """
        vehicle_model = self.find_model_info(brand, model)

        if not vehicle_model:
            raise VehicleInfoMissingError(brand, model)
        """
        # python 3.8부터 가능합니다.
        # 변수 := 표현식
        # 표현식의 결과를 변수에 할당하고, 동시에 반환합니다. 즉, 변수 = 표현식을 하고, return 변수 기능을 합니다.
        if not (vehicle_model := self.find_model_info(brand, model)):
            raise VehicleInfoMissingError(brand, model)

        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, vehicle_model)

    def online_status(self) -> RegistryStatus:
        """온라인 구매시 등록"""
        return (
            RegistryStatus.OFFLINE
            if not self.online
            else RegistryStatus.CONNECTION_ERROR
            if len(self.vehicle_model) == 0
            else RegistryStatus.ONLINE
        )


if __name__ == '__main__':

    # create registry instance
    registry = VehicleRegistry()

    # 자동차 등록
    registry.add_vehicle_model_info(VehicleModelInfo("Ferrai", "Califonia", 100_000_000))
    registry.add_vehicle_model_info(VehicleModelInfo("Lambo", "Urus", 600_000_000))
    registry.add_vehicle_model_info(VehicleModelInfo("Porsh", "Frog", 300_000_000))
    registry.add_vehicle_model_info(VehicleModelInfo("Bentely", "Model 3", 600_000_000))

    # 온라인 등록 확인
    print(f"Registry Status: {registry.online_status()}")

    # 새로운 자동차 등록
    vehicle = registry.register_vehicle("Ferrai", "Califonia")

    # 자동차 디버깅
    print(vehicle.to_string())