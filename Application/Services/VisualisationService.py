import seaborn as sns
import matplotlib.pyplot as plt

def AvarageTemperatureVisualisation(weatherData):
    groupedData = weatherData.groupby(["Location"])['Temperature_C'].mean
    
    plt.figure(figsize=(10,6))
    sns.scatterplot(x="Date_Time", y='Temperature_C', hue='Location', data=groupedData)
    
    plt.title('Avarage Temperatures')
    plt.ylabel('Temperature (°C)')
    plt.xlabel('Date')
    plt.show()
    

def AvarageHumidityVisualisation(weatherData):
    groupedData = weatherData.groupby(["Location"])['Humidity_pct'].mean
    
    plt.figure(figsize=(10,6))
    sns.scatterplot(x="Date_Time", y='Humidity_pct', hue='Location', data=groupedData)
    
    plt.title('Avarage Humidity')
    plt.ylabel('Humidity (%)')
    plt.xlabel('Date')
    plt.show()
    

def AvaragePrecipitationVisualisation(weatherData):
    groupedData = weatherData.groupby(["Location"])['Precipitation_mm'].mean
    
    plt.figure(figsize=(10,6))
    sns.scatterplot(x="Date_Time", y='Precipitation_mm', hue='Location', data=groupedData)
    
    plt.title('Avarage Precipitation')
    plt.ylabel('Precipitation (mm)')
    plt.xlabel('Date')
    plt.show()
    

def AvarageWindSpeedVisualisation(weatherData):
    groupedData = weatherData.groupby(["Location"])['Wind_Speed_kmh'].mean
    
    plt.figure(figsize=(10,6))
    sns.scatterplot(x="Date_Time", y='Wind_Speed_kmh', hue='Location', data=groupedData)
    
    plt.title('Avarage Wind Speed')
    plt.ylabel('Wind Speed (kmh)')
    plt.xlabel('Date')
    plt.show()



def CityTemperatureVisualisation(weatherData, cityName):
    dataForCity = weatherData[weatherData['city_name'] == cityName]
    
    sns.scatterplot(x="Date_Time", y='Temperature_C', hue='Location', data=dataForCity)
    
    plt.title('Avarage Temperatures')
    plt.ylabel('Temperature (°C)')
    plt.xlabel('Date')
    plt.show()
    

def CityHumidityVisualisation(weatherData, cityName):
    dataForCity = weatherData[weatherData['city_name'] == cityName]
    
    plt.figure(figsize=(10,6))
    sns.scatterplot(x="Date_Time", y='Humidity_pct', data=dataForCity)
    
    plt.title(f'Humidity for {cityName}')
    plt.ylabel('Humidity (%)')
    plt.xlabel('Date')
    plt.show()
    

def CityPrecipitationVisualisation(weatherData, cityName):
    dataForCity = weatherData[weatherData['city_name'] == cityName]
    
    plt.figure(figsize=(10,6))
    sns.scatterplot(x="Date_Time", y='Precipitation_mm', data=dataForCity)
    
    plt.title(f'Precipitation for {cityName}')
    plt.ylabel('Precipitation (mm)')
    plt.xlabel('Date')
    plt.show()
    

def CityWindSpeedVisualisation(weatherData, cityName):
    dataForCity = weatherData[weatherData['city_name'] == cityName]
    
    plt.figure(figsize=(10,6))
    sns.scatterplot(x="Date_Time", y='Wind_Speed_kmh', data=dataForCity)
    
    plt.title('Avarage Wind Speed')
    plt.ylabel('Wind Speed (kmh)')
    plt.xlabel('Date')
    plt.show()
    

def CityDependencyBetweenHumidityAndPrecipitation(weatherData, cityName):
    dataForCity = weatherData[weatherData['city_name'] == cityName]
    
    plt.figure(figsize=(10,6))
    sns.scatterplot(x=" Precipitation_mm", y='Humidity_pct', data=dataForCity)
    
    plt.title('Avarage Wind Speed')
    plt.ylabel(' Precipitation (mm)')
    plt.xlabel('Humidity (%)')
    plt.show()