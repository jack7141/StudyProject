
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
    pass
"""
Tank 클래스는 Unit 클래스를 상속받아 Unit에서 지정한 Method를 모두 활용할 수 있다.
이때, Tank class에서 __init__ 정보를 추가 하고싶다면 어떻게 해야할까?
"""
tank_1 = Tank('시즈탱크', 'Big', 100)
tank_1.show_status()

"""
@print
    이름: Tank
    등급: 시즈탱크
    사이즈: Big
    라이프: 100
"""
