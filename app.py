# import relevant libraries
from fastapi import FastAPI  , File, UploadFile, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import numpy as np
import keras

# make app
app = FastAPI()


# load pretrained model
model = keras.models.load_model("LSTM.h5")


# get method
@app.get("/ping")
async def ping():

    return "Hello, this is Fahad's API"

# pydantic schema for the data
class Item(BaseModel):

    v1: float
    v2: float
    v3: float
    v4: float

# define the response message
class ResponseMessage(BaseModel):

    message: list

# post method
@app.post("/ping", response_model=ResponseMessage)
async def create_item(item: Item):

    # convert the input to array
    x = np.array([item.v1, item.v2, item.v3, item.v4])

    # reshape the array
    x = x.reshape(1,-1,1)

    # make prediction
    output = model.predict(x)
    a  = output.ravel().tolist()

    # return output
    return {"message": a}




