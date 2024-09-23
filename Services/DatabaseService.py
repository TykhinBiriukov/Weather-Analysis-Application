import sqlite3
import pandas as pd

def ConnectToDatabase(dbPath):
    connection = sqlite3.connect(dbPath)
    return connection

def ReadSQLAndReturnWeatherData(connection):
    readQuerty = "SELECT\
        f.date,\
        c.name AS city_name,\
        f.temp,\
        f.temp_min,\
        f.temp_max,\
        f.humidity,\
        f.wind_speed,\
        f.visibility,\
        f.pop,\
        f.rain\
    FROM Forecast f\
    JOIN City c ON f.city_id = c.id"
    
    weatherData = pd.read_sql(readQuerty, connection)
    # weatherData['date'] = pd.to_datetime(weatherData['date'])
    # print(weatherData)
    
    return weatherData
