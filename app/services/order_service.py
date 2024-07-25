from models.order import Order
from validators.order_validator import OrderValidator

class OrderService:
    def __init__(self, validator: OrderValidator):
        self.validator = validator

    def create_order(self, order: Order):
        self.validator.validate(order)
        if order.currency == "USD":
            order.price = str(float(order.price) * 31)
            order.currency = "TWD"
        return order

