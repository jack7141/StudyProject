from datetime import datetime


class PaymentProcessor:
    def __init__(self, api_key: str)->None:
        self.api_key = api_key

    def _check_api_key(self)->bool:
        return self.api_key == 'b1013basd-ja903-asdf901014-asbdfi1b019'

    def charge(self, card: CreditCard, amount: int)->None:
        ...

    def validate_card(self, card: CreditCard)->bool:
        return (
            luhn_checksum(card.number)
            and datetime(card.expiry_year, card.expiry_month, 1) > datetime.now()
        )

def luhn_checksum(card_number: str)->bool:
    def digits_of(card_nr: str):
        return [int(d) for d in card_nr]