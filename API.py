from requests_html import HTMLSession

s = HTMLSession()
DEFAULT_USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"

def geturl(city):
    return (f"https://www.google.com/search?q={city}+weather")

def getBasic(r):
    location = r.html.find("span.BBwThe", first=True).text
    today = r.html.find("div#wob_dts", first=True).text
    summary = r.html.find("span#wob_dc", first=True).text
    precipitation = r.html.find("span#wob_pp", first=True).text
    humidity = r.html.find("span#wob_hm", first=True).text
    elements = r.html.find(".wob_t", first=False)
    weekday = r.html.find("div.Z1VzSb", first=False)
    weeklst = [element.text for element in weekday]
    basedata = [element.text for element in elements]
    return basedata, weeklst, location, today, summary, precipitation, humidity

def getWeather(city=None):
    if city:
        url = geturl(city)
        r = s.get(url, headers={'User-Agent': DEFAULT_USER_AGENT})
        basedata, weeklst, location, today, summary, precipitation, humidity = getBasic(r)
        temp = basedata[0]
        wind = basedata[6]
        datalst = []
        weekdict = {}
        gap = 0
        for i in range(8, len(basedata), 2):
            datalst.append(basedata[i])
        for i in range(0, len(weeklst) - 1):
            weekdict[weeklst[i]] = {"max": datalst[gap] + " F", "min": datalst[gap + 1] + " F"}
            gap += 2
        data = {
            "location": location,
            "current": {
                "day": today,
                "summary": summary,
                "temperature": temp + " F",
                "precipitation": precipitation,
                "humidity": humidity,
                "wind": wind
            },
            "weeklyforecast": weekdict
        }
        return data
    return {
        "message": "No city name Provided",
        "syntax1": "/api/weather/<City Name>",
        "syntax2": "/api/weather?city=<City Name>",
        "Request Type": "GET"
    }

def getWeatherF(city=None):
    if city:
        url = geturl(city)
        r = s.get(url, headers={'User-Agent': DEFAULT_USER_AGENT})
        basedata, weeklst, location, today, summary, precipitation, humidity = getBasic(r)
        temp = basedata[1]
        wind = basedata[7]
        datalst = []
        weekdict = {}
        gap = 0
        for i in range(9, len(basedata), 2):
            datalst.append(basedata[i])
        for i in range(0, len(weeklst) - 1):
            weekdict[weeklst[i]] = {"max": datalst[gap] + " C", "min": datalst[gap + 1] + " C"}
            gap += 2
        data = {
            "location": location,
            "current": {
                "day": today,
                "summary": summary,
                "temperature": temp + " C",
                "precipitation": precipitation,
                "humidity": humidity,
                "wind": wind
            },
            "weeklyforecast": weekdict
        }
        return data
    return {
        "message": "No city name Provided",
        "syntax1": "/api/weather/<City Name>",
        "syntax2": "/api/weather?city=<City Name>",
        "Request Type": "GET"
    }