"""
factory Patter 테스트용 스크립트이며 패키지 밖에서 사용해야함
"""
from DesignPatterns.factory_pattern.Accountant import Accountant as accountant
from DesignPatterns.factory_pattern.Admin import Admin as admin

if __name__ == '__main__':
    """
    Error : TypeError: get_role() missing 1 required positional argument: 'self'
    인스턴스를 불러서 사용해야함;;
    """
    a1 = accountant(name='회계사', gender='man', age='21')
    # Accountant - 회계사, 21 years old man
    print(a1)
    # accountant
    print(a1.get_role())

    admin1 = admin(name='관리자', gender='여성', age='32')
    # Admin - 관리자, 32 years old 여성
    print(admin1)
    # administration
    print(admin1.get_role())


