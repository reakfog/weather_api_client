# Weather API client

## Summary
1. [Task](#task)
2. [Launch](#launch)
3. [Examples](#examples)

## <a name='task'>Task</a>

### D. Build a command line API client

Using the [Metaweather API](https://www.metaweather.com/api/), make a command line tool that receives a city name as argument
and says whether it’s going to rain tomorrow in this city or not. Here again, packaging and tests
are optional, but always appreciated. This can be done quite shortly if you’re on a schedule and
stick to the minimum.

## <a name='launch'>Launch</a>
You need to install Python 3 on your local machine and meet the following conditions:
1. Clone the repository to your local machine
2. In the project root directory, install and run the virtual environment
    - `python3 -m venv venv`
    - `source venv/bin/activate`
4. Install requirements:
    - `pip install -r requirements.txt`
5. Run script:
    - get help: `python3 openweather_cli.py --help`
    - get weather forecast for city: `python3 openweather_cli.py CITY`

## <a name='examples'>Examples</a>

`python3 openweather_cli.py --help`  
![Get help](https://github.com/reakfog/weather_api_client/blob/main/screenshots/get_help.png)

`python3 openweather_cli.py --singapore`  
![Get rainy forecast](https://github.com/reakfog/weather_api_client/blob/main/screenshots/get_rainy_forecast.png)

`python3 openweather_cli.py 'new york'`  
![Get not rainy forecast](https://github.com/reakfog/weather_api_client/blob/main/screenshots/get_not_rainy_forecast.png)