from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import util

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/get_companies_names')
def get_companies_names():
    response = JSONResponse({
        'companies': util.get_companies_names()
    })
    return response

@app.post('/predict', response_class=JSONResponse)
async def predict_price(request: Request):
    form = await request.form()
    company = form.get('company')
    ram = float(form.get('ram'))
    battery = float(form.get('battery'))
    display = float(form.get('display'))
    external_memory = float(form.get('externalMemory'))
    inbuilt_memory = float(form.get('inbuiltMemory'))
    android = float(form.get('androidVersion'))
    fast_charging = float(form.get('fastCharging'))
    t_rear = float(form.get('totalRearMP'))
    n_rear = float(form.get('numRearCameras'))
    m_rear = float(form.get('maxRearMP'))
    t_front = float(form.get('totalFrontMP'))
    n_front = float(form.get('numFrontCameras'))
    m_front = float(form.get('maxFrontMP'))
    width = float(form.get('screenWidth'))
    height = float(form.get('screenHeight'))
    p_speed = float(form.get('processorSpeed'))

    price_prediction = util.get_phone_price(company, ram, battery, display, external_memory, inbuilt_memory, android, fast_charging, t_rear, n_rear, m_rear, t_front, n_front, m_front, width, height, p_speed)

    return {'predicted_price': price_prediction}

@app.get('/predict_phone_price')
async def read_item(request: Request):
    return templates.TemplateResponse(
        'main.html', {'request': request}
    )

if __name__ == "__main__":
    util.load_saved()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
