from Architecture.Proxy.EmployeeProxy import EmployeeProxy
from DesignPatterns.factory_pattern import Engineer
from DesignPatterns.factory_pattern import Accountant
from DesignPatterns.factory_pattern import Admin
class EmployeeProxyFactory(object):
    """인스턴스 카운트 프록시를 위한 Employee 팩토리 클래스"""
    
    @classmethod
    def create(cls, name, *args):
        name = name.lower().strip()

        if name == 'engineer':
            return EmployeeProxy(Engineer(*args))
        elif name == 'accountant':
            return EmployeeProxy(Accountant(*args))
        elif name == 'admin':
            return EmployeeProxy(Admin(*args))

if __name__ == '__main__':
    factory = EmployeeProxyFactory()
    engineer = factory.create('engineer','sam',25,'M')
    print(engineer)
    admin = factory.create('admin','sam',25,'M')
    print(admin)
    print(EmployeeProxy.get_count())
    del engineer
    print(EmployeeProxy.get_count())
    del admin
    print(EmployeeProxy.get_count())