import { useState } from "react";

function WeatherApp() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);
  const [forecast, setForecast] = useState(null);

  async function handleWeatherClick() {
    const response = await fetch(`/weather/${city}`);
    const data = await response.json();
    setWeather(data);
  }

  async function handleForecastClick() {
    const response = await fetch(`/forecast/${city}`);
    const data = await response.json();
    setForecast(data);
  }

  return (
    <div>
      <h1>Weather App</h1>
      <label htmlFor="city">City:</label>
      <input
        type="text"
        id="city"
        value={city}
        onChange={(e) => setCity(e.target.value)}
      />
      <br />
      <button onClick={handleWeatherClick}>Get Current Weather</button>
      <button onClick={handleForecastClick}>Get Weather Forecast</button>

      {weather && (
        <div>
          <h2>{weather.city}</h2>
          <p>Temperature: {weather.temperature}°C</p>
          <p>Description: {weather.description}</p>
        </div>
      )}

      {forecast && (
        <div>
          <h2>{forecast.city}</h2>
          <ul>
            {forecast.forecast.map((item) => (
              <li key={item.datetime}>
                <p>Date and time: {item.datetime}</p>
                <p>Temperature: {item.temperature}°C</p>
                <p>Description: {item.description}</p>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default WeatherApp;