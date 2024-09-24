import pandas as pd

def ReadJsonAndReturnWeatherData():
    weatherDataFrame = pd.read_json('WeatherData.json')
    weatherDataFrame.groupby("Location")
    
    return weatherDataFrame