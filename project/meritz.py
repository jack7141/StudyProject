
from Common import ConVar
from Lib import UtilLib

year = int(input("보험료 계산 년도를 넣어주세요: "))

def soultion(n: int) -> float:
    # 변수 조정
    ConVar.qx_list.insert(0,1)

    # 당해년도
    # 보험료 수입의 현재가치
    insurance_current_price = 1
    
    # 사망보험금 지급액 현재가치
    current_value = ConVar.insurance_price/ConVar.annual_interest_rate*ConVar.qx_list[1]

    for i in range(1, n):
        insurance_current_price += 1/(ConVar.annual_interest_rate**i)*UtilLib.factorial_iteravice(i)
        current_value += ConVar.insurance_price/(ConVar.annual_interest_rate**(i+1))*ConVar.qx_list[i+1]*UtilLib.factorial_iteravice(i)

    return current_value/insurance_current_price

print('='*80)
print("[Start Program]")
print(f"{year}년일때 보험료 - {soultion(year)}")
print('='*80)

