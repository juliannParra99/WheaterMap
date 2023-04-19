import httpx
from fastapi import FastAPI

app = FastAPI()


@app.get("/weather/{city}")
async def get_weather(city: str):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": "048eca2c0e9a0036b2f9449ce17842ff",
        "units": "metric"
    }
    #recupero los datos de la url, y envio los parametros que necesito
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }

@app.get("/forecast/{city}")
async def get_forecast(city: str):
    # Definimos la URL base de la API del clima
    url = "https://api.openweathermap.org/data/2.5/forecast"
    # Definimos los parámetros que se enviarán a la API, incluyendo la ciudad, el ID de la API y la unidad de medidaGIT
    params = {
        "q": city,
        "appid": "048eca2c0e9a0036b2f9449ce17842ff",
        "units": "metric"
    }

    # Abrimos una conexión asíncrona con la API utilizando la biblioteca HTTPX
    async with httpx.AsyncClient() as client:
        # Enviamos una solicitud GET a la API con la URL y los parámetros definidos anteriormente
        response = await client.get(url, params=params)
        # Verificamos si la solicitud fue exitosa (código de estado HTTP 200) o no
        response.raise_for_status()
        # Convertimos la respuesta de la API de formato JSON a un objeto de Python
        data = response.json()
    # Creamos una lista vacía que almacenará la información del pronóstico del clima para los próximos días
    forecast = []
    # Iteramos sobre cada elemento en la lista de pronósticos proporcionada por la API
    for item in data["list"]:
        # Extraemos la fecha y hora del pronóstico y la temperatura del objeto de pronóstico actual
        forecast.append({
            "datetime": item["dt_txt"],
            "temperature": item["main"]["temp"],
            "description": item["weather"][0]["description"]
        })
    # Devolvemos un objeto JSON que incluye el nombre de la ciudad y la lista de pronósticos del clima
    return {
        "city": data["city"]["name"],
        "forecast": forecast
    }

