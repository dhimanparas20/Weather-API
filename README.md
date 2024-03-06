# Weather API

## Description
Weather API is a Flask-based backend project that provides weather data for any city or postal code. It scrapes weather data from Google's weather page and transforms it into an API. The API supports retrieving weather information in both Celsius and Fahrenheit units.

## Usage

### Endpoints

#### Celsius Unit
1. Get weather by city name:
   - `GET http://127.0.0.1:5000/api/weather/<city>`
   - `GET http://127.0.0.1:5000/api/weather?city=<city>`

2. Get weather by postal code:
   - `GET http://127.0.0.1:5000/api/weather/<postal_code>`
   - `GET http://127.0.0.1:5000/api/weather?city=<postal_code>`

#### Fahrenheit Unit
1. Get weather by city name:
   - `GET http://127.0.0.1:5000/api/weatherf/<city>`
   - `GET http://127.0.0.1:5000/api/weatherf?city=<city>`

2. Get weather by postal code:
   - `GET http://127.0.0.1:5000/api/weatherf/<postal_code>`
   - `GET http://127.0.0.1:5000/api/weatherf?city=<postal_code>`

### Response Format
The API returns weather data in the following JSON format:

```json
{
    "location": "City, State",
    "current": {
        "day": "Day, Time",
        "summary": "Weather Summary",
        "temperature": "Temperature",
        "precipitation": "Precipitation",
        "humidity": "Humidity",
        "wind": "Wind Speed"
    },
    "weeklyforecast": {
        "Day": {
            "max": "Maximum Temperature",
            "min": "Minimum Temperature"
        },
        ...
    }
}
```
## Deployment
```sh
git clone https://github.com/dhimanparas20/Weather-API.git
```
```sh
cd Weather-API
```
```sh
pip3 install requirements.txt
```
```sh
python3 app.py
```
### or
[This API is deployed on Vercel for general use.](https://weather-iota-tan.vercel.app)


## License
This project is open-source and free to use in any project. However, if you use it, please provide proper attribution or mention this project. For any suggested changes or improvements, please feel free to reach out.
