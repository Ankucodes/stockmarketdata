from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class stockmarket(BaseModel):
    vol_moving_avg: object 
    adj_close_rolling_med: object
