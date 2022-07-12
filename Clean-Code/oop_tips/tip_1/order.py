from datetime import datetime


@dataclasses
class Order:
    line_items: list[LineItem] = field(default_factory=list)
    status: OrderStatus = OrderStatus.OPEN

    @property
    def total(self)->int:
        return sum(item.total for item in self.line_items)

    def pay(self)->None:
        self.status = OrderStatus.PAID