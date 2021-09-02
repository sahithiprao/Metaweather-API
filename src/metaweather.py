import concurrent.futures
import requests

meta_weather_urls = [
    'https://www.metaweather.com/api/location/2487610/',
    'https://www.metaweather.com/api/location/2442047/',
    'https://www.metaweather.com/api/location/2366355/'
]


def get_avg_max_temp(api_url):
    try:
        response = requests.get(api_url).json()
        max_temps = [response['consolidated_weather'][i]['max_temp'] for i in range(6)]
        avg_temp = round(sum(max_temps) / len(max_temps), 2)
        return f'{response["title"]} Average Max Temp: {avg_temp}'
    except Exception as e:
        return e


with concurrent.futures.ThreadPoolExecutor() as executor:
    try:
        results = executor.map(get_avg_max_temp, meta_weather_urls)

        for result in results:
            print(result)

    except Exception as e:
        print(e)
