
"""@author: akanksha
"""

#Library imports
import uvicorn
from fastapi import FastAPI, Form, Request
from stockmarket import stockmarket
import numpy as np
import pickle
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
#Create the app object

app = FastAPI()

pickle_in = open("model.pkl","rb")
try:
    regr_model=pickle.load(pickle_in)
except EOFError:
    print()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

@app.get('/')
def read_form():
    return 'hello world'

@app.get(path="/predict", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})




#Expose the prediction functionality, make a prediction from the passed

@app.post(path='/predict')
def predict_volume(vol_moving_avg: int = Form(...),adj_close_rolling_med: int = Form(...)):
    
    trading_volume = regr_model.predict(np.array([[vol_moving_avg, adj_close_rolling_med]],dtype=object))
    return {"trading_volume": np.min(trading_volume)}
    



# Running the API with uvicorn
#   
if __name__ == '__main__':
    uvicorn.run(app)
    
    #host='127.0.0.1', port=8000
#uvicorn app:app --reload
