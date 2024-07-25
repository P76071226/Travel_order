from fastapi import FastAPI, HTTPException, status
from models.order import Order
from services.order_service import OrderService
from validators.order_validator import OrderValidator
from custom_exceptions import ValidationErrorWithCode

app = FastAPI()

validator = OrderValidator()
order_service = OrderService(validator)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/orders")
def create_order(order: Order):
    try:
        result = order_service.create_order(order)
        return result
    except ValidationErrorWithCode as e:
        raise HTTPException(status_code=e.code, detail=e.message)
        
