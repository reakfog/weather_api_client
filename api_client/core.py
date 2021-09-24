from datetime import date, timedelta
from json import loads

from requests import RequestException, get

from api_client.interface_text import (
    API_REQUEST_ERROR,
    CITIES_COUNT_ERROR,
    NO_FORECASTS_ERROR,
    NOT_RAINY_ANSWER,
    RAINY_ANSWER,
)
from api_client.settings import API_METHODS, API_URL, RAIN_STATES


def get_city_woeid(city):
    url = API_URL + API_METHODS["Location Search"]
    params = {"query": city}

    try:
        response = get(url=url, params=params)
        response = loads(response.text)
        if len(response) != 1:
            response[len(response)]
    except RequestException:
        exit(API_REQUEST_ERROR)
    except:
        exit(CITIES_COUNT_ERROR)
    woeid = response[0]["woeid"]
    return woeid


def get_city_weather_tomorrow(woeid, city):
    tomorrow_date = date.today() + timedelta(days=1)
    formatted_tomorrow_date = "{year}/{month}/{day}".format(
        year=tomorrow_date.year, month=tomorrow_date.month, day=tomorrow_date.day
    )
    api_method = API_METHODS["Location Day"].format(woeid=woeid, date=formatted_tomorrow_date)
    url = API_URL + api_method

    try:
        response = get(url=url)
        response = loads(response.text)
        weather_tomorrow = response[0]["weather_state_name"]
    except RequestException:
        return API_REQUEST_ERROR
    except:
        return NO_FORECASTS_ERROR

    city = " ".join([i.capitalize() for i in city.split()])
    if weather_tomorrow in RAIN_STATES:
        return RAINY_ANSWER.format(city=city)
    return NOT_RAINY_ANSWER.format(city=city)
