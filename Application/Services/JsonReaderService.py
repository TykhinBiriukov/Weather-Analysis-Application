import pandas as pd

def ReadJsonAndReturnWeatherData():
    weatherDataFrame = pd.read_json('WeatherData.json')
    print(weatherDataFrame)
    weatherDataFrame.groupby("Location")
    return weatherDataFrame