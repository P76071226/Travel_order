from models.order import Order
from interfaces.validator_interface import ValidatorInterface
from custom_exceptions import ValidationErrorWithCode

class OrderValidator(ValidatorInterface):
    def validate(self, order: Order):
        self.validate_name_characters(order.name)
        self.validate_name_capitalization(order.name)
        self.validate_price(order.price)
        self.validate_currency(order.currency)
    
    def validate_name_characters(self, name: str):
        if not all(ord(char) < 128 for char in name):  # Check for non-ASCII characters
            raise ValidationErrorWithCode("Name contains Non-English characters", 400)
    
    def validate_name_capitalization(self, name: str):
        if not name[0].isupper():
            raise ValidationErrorWithCode("Name is not Capitalized", 400)
    
    def validate_price(self, price: str):
        price_float = float(price)
        if price_float > 2000:
            raise ValidationErrorWithCode("Price is over 2000", 400)
    
    def validate_currency(self, currency: str):
        valid_currencies = {'USD', 'TWD'}
        if currency not in valid_currencies:
            raise ValidationErrorWithCode("Currency format is wrong", 400)

