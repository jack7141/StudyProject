
class Unit(object):
    def __init__(self, rank, size, life):
        # 상속받는 클래스의 이름을 가져온다
        self.name = self.__class__.__name__
        self.rank = rank
        self.size = size
        self.life = life

    def show_status(self):
        print(f'이름: {self.name}')
        print(f'등급: {self.rank}')
        print(f'사이즈: {self.size}')
        print(f'라이프: {self.life}')

class Tank(Unit):
    def __init__(self, rank, size, life, attack_type):
        # 상속받는 클래스의 이름을 가져온다
        self.name = self.__class__.__name__
        self.rank = rank
        self.size = size
        self.life = life
        self.attack_type = attack_type

    def show_status(self):
        print(f'이름: {self.name}')
        print(f'등급: {self.rank}')
        print(f'사이즈: {self.size}')
        print(f'라이프: {self.life}')
        print(f'공격 타입: {self.attack_type}')

"""
위와 같이 Tank클래스에 다시 메소드를 만들어서 처리하는 방법이 있지만, 
이는 클래스를 사용하는 의미가 전혀 없어진다.
"""
tank_1 = Tank('시즈탱크', 'Big', 100, '원거리 공격')
tank_1.show_status()

"""
@print
    이름: Tank
    등급: 시즈탱크
    사이즈: Big
    라이프: 100
    공격 타입: 원거리 공격
"""
