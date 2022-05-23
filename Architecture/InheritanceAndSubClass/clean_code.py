
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
        super(Tank, self).__init__(rank, size, life)
        self.attack_type = attack_type

    def show_status(self):
        super().show_status()
        print(f'공격 타입 : {self.attack_type}')

class SiegeTank(Tank):
    def __init__(self, rank, size, life, attack_type, damage, SiegeTank_damage):
        super(SiegeTank, self).__init__(rank, size, life, attack_type, damage)
        self.SiegeTank_damage = SiegeTank_damage

    def show_status(self):
        super(SiegeTank, self).show_status()
        print('시즈모드 데미지: {}'.format(self.SiegeTank_damage))
"""
위와 같이 super를 사용하여 부모클래스의 메소드들을 오버라이드하고, 내가 추가하고 싶은 부분을 추가해주면된다.

@super 사용법
1. super(자신의 클래스명, self).<부모클래스에서 가져올 메서드명>
2. super().부모클래스에서 가져올 메서드명
"""
tank_1 = Tank('시즈탱크', 'Big', 100, '원거리 공격')
tank_1.show_status()
print(Tank.__dict__)
# print(help(Tank))
print(help(SiegeTank))
"""
@print
    이름: Tank
    등급: 시즈탱크
    사이즈: Big
    라이프: 100
    공격 타입: 원거리 공격
"""
