"""
출처 - https://www.youtube.com/watch?v=-rf_wzK6vPU
"""
class PaymentHandler(Protocol):
    def handle_payment(self, amount: int) -> None:
        ...

class WooriCheckPaymentHandler:
    def handle_payment(self, amount: int) -> None:
        print(f'결재금액 ${amount/100:.2f}을 우리 체크 결재합니다.')

class KakaoPaymentHandler:
    def handle_payment(self, amount: int) -> None:
        print(f'결재금액 ${amount/100:.2f}을 카카오페이로 결재합니다.')

PRICES = {
    'burger': 10_00,
    'fries':5_00,
    'drink': 2_00,
    'salad':15_00,
}

def order_food(items: list[str], payment_handler: PaymentHandler):
    total = sum(PRICES[item] for item in items)
    print(f'Your order is ${total/100:.2f}.')
    payment_handler.handle_payment(total)
    print('결재 감사합니다.')

def main() -> None:
    order_food(['burger', 'fries', 'drink'], WooriCheckPaymentHandler())
    order_food(['burger', 'fries', 'drink'], KakaoPaymentHandler())

if __name__ == '__main__':
    main()

"""
CODE SMELL

class WooriCheckPaymentHandler:
    def handle_payment(self, amount: int) -> None:
        print(f'결재금액 ${amount/100:.2f}을 우리 체크 결재합니다.')

PRICES = {
    'burger': 10_00,
    'fries':5_00,
    'drink': 2_00,
    'salad':15_00,
}

# 함수 타입에 payment_handler: PaymentHandler를 명시해주어서, 인스턴스를 불러오는 수고를 덜어준다.
또한 확장성을 위해서 인터페이스용으로 PaymentHandler를 만들고, 필요한 클래스를 만들어서 유지보수에 좋게 수정해준다.
def order_food(items: list[str]):
    total = sum(PRICES[item] for item in items)
    print(f'Your order is ${total/100:.2f}.')
    payment_handler = WooriCheckPaymentHandler()
    payment_handler.handle_payment(total)
    print('결재 감사합니다.')

def main() -> None:
    order_food(['burger', 'fries', 'drink'])

"""
