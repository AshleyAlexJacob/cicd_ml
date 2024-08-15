from fastapi import FastAPI
from fastapi.responses import JSONResponse
import joblib
import uvicorn
from models.input import Input
import pandas as pd

app = FastAPI()


def load_model(path: str = None):
    path = path if path is not None else "model_v1.0.pkl"
    return joblib.load(path)


model = load_model("model_v1.0.pkl")


@app.post("/predict")
def predict(data: Input):
    try:
        data_dict = data.model_dump()
        model_input = pd.DataFrame([data_dict])
        prediction = model.predict(model_input)[0]
        return JSONResponse({"result": prediction}, 200)
    except Exception as e:
        return JSONResponse({"error": f"Internal Server {e}"}, 404)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
