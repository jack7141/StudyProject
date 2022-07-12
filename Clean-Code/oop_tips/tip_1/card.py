from dataclasses import dataclass


@dataclass
class CreditCart:
    number: str
    expiry_month: int
    expiry_year: int

