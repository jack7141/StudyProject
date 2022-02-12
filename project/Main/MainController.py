import argparse
from Common import ConVar
from Lib import UtilLib

parser = argparse.ArgumentParser(description='보험료 계산 프로그램입니다.')
parser.add_argument('-year', type=int, help="n 년일때 보험료를 계산합니다", required=True)
args = parser.parse_args()

class MainController:
    def __init__(self) -> None:
        self.year = args.year

    def run(self):
        print("-"*80)
        print('[Mertiz Coding Test Running]')

        # -year 인자 체크[존재 및 10이하 여야함]
        if self.arg_check():
            result = self.solution()
            print(f'{self.year}년일때 보험료는: {result}입니다.')
            print("-" * 80)

    def arg_check(self):
        if args.year is not None and args.year < 11:
            return True
        else :
            print(f'[arg_check] - year 값은 10이하여야 합니다.')
            return False

    def solution(self):
        # CSV 파일 Common 변수에 저장
        ConVar.qx_list = UtilLib.read_csv()

        # 당해년도
        # 보험료 수입의 현재가치
        insurance_current_price = 1
        # 사망보험금 지급액 현재가치
        current_value = ConVar.insurance_price/ConVar.annual_interest_rate*ConVar.qx_list[1]

        for i in range(1, self.year):
            insurance_current_price += 1/(ConVar.annual_interest_rate**i)*UtilLib.factorial_iteravice(i)
            current_value += ConVar.insurance_price/(ConVar.annual_interest_rate**(i+1))*ConVar.qx_list[i+1]*UtilLib.factorial_iteravice(i)

        return current_value/insurance_current_price