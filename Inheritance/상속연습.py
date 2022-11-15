# coding=utf-8
class AccountNumberSearch(object):
    def test(self):
        # 얘는 Admin을 상속을 받지도 않았는데,,,,,어ㄸ허게 get_account_pk 얘를 알지?
        # super()로 올라왔을경우 self는 자기 자신이 되고 self에서 가져와서
        return super().test()

    def dddd(self, payload):
        return super().dddd(**payload)

    def double(self):
        return self.get_search_results()

class Admin:
    def get_account_pk(self):
        return 'get_account_pkasldkfjasdf'

    def get_search_results(self):
        return "Admin get_search_results"

    def test(self):
        return "AMIDN TEST"

    def dddd(self, a=None, b=None):
        return a, b

class MixinTesterClass(AccountNumberSearch, Admin):
    """"""
    def test(self):
        return super().test()



if __name__ == "__main__":
    a = MixinTesterClass()
    payload = {
        'a': 123,
        'b': 567
    }
    print(a.test())
    print(a.dddd(payload))
    print(a.double())
    # mro를 통해서 다음에 위치한 클래스를 보고, super()를 사용했을때, 어디로 이동하게되는지 확인할 수 있다.
    print(MixinTesterClass.__mro__)
