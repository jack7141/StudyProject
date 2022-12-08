from multiprocessing import Pool

from rest_framework import serializers

# 바이트
# b'20221207A5654389 010                                                                01MSFT        211000                                                      '


class TestSerializer(serializers.Serializer):
    test = serializers.CharField(default="test")


class ProviderMixin(serializers.Serializer):
    base_amt = serializers.CharField(default=0, help_text="입출금 원금")

    def make_module(self):
        return

    def func(self, payload_test):
        ser = TestSerializer(data=payload_test)
        ser.is_valid(raise_exception=True)
        return ser.data

    def test(self):
        payload_test = {'test': 1}
        p = Pool(processes=1)
        ret = p.apply_async(self.func, (payload_test,))
        return ret.get(timeout=5)

    def to_representation(self, instance):
        instance = super().to_representation(instance)
        print(self.test())
        return instance


if __name__ == "__main__":
    payload = {'base_amt': 1}

    serializer = ProviderMixin(data=payload)
    serializer.is_valid(raise_exception=True)
    print(serializer.data)

