from fastapi import APIRouter , Depends
from app.services.model_service import predict_car_price
from pydantic import BaseModel
from app.core.dependencies import get_current_user,get_api_key

app = APIRouter()

class CarFeatures(BaseModel):
    company: str
    year: int
    owner: str
    fuel: str
    seller_type: str
    transmission: str
    km_driven: float
    mileage_mpg: float
    engine_cc: float
    max_power_bhp: float
    torque_nm: float
    seats: float

@app.post('/predict')
def predict_price(data:CarFeatures , user=Depends(get_current_user) ,_=Depends(get_api_key) ):
    prediction = predict_car_price(data.model_dump())
    return {'Predicted Price':f"{prediction:,.2f}"}
