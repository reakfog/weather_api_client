import click

from api_client.core import get_city_weather_tomorrow, get_city_woeid


@click.command()
@click.argument("city")
def main(city):
    """
    Here is the MetaWeather API Client, which allows you to
    find out the weather forecast in the city you specified.
    It is extremely simple to use it:

    1. enter the city you are interested in

    2. find out the rain forecast for tomorrow

    More at https://www.metaweather.com/api.
    """
    woeid = get_city_woeid(city=city)
    forecast = get_city_weather_tomorrow(woeid=woeid, city=city)
    print(forecast)


if __name__ == "__main__":
    main()
