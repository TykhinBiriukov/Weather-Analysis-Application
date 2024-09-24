import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def AvarageTemperatureVisualisation(weatherData):
    groupedData = weatherData.groupby("Location")["Temperature_C"].mean().sort_values().reset_index()
    
    axis = sns.barplot(x="Location", y="Temperature_C", data=groupedData, hue="Temperature_C", legend=False, palette="seismic")
    
    for bar in axis.patches:
        bar.set_edgecolor('black')
        bar.set_linewidth(0.5)
    
    plt.title("Avarage Temperatures")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.xlabel("Cities")
    plt.show()


def AvarageHumidityVisualisation(weatherData):
    groupedData = weatherData.groupby(["Location"])["Humidity_pct"].mean().sort_values().reset_index()
    
    axis = sns.barplot(x="Location", y="Humidity_pct", data=groupedData, hue="Humidity_pct", legend=False, palette="crest")
    
    for bar in axis.patches:
        bar.set_edgecolor('black')
        bar.set_linewidth(0.5)
        
    plt.title("Avarage Humidity")
    plt.ylabel("Humidity (%)")
    plt.xlabel("Cities")
    plt.xticks(rotation=45)
    plt.show()
    

def AvaragePrecipitationVisualisation(weatherData):
    groupedData = weatherData.groupby(["Location"])["Precipitation_mm"].mean().sort_values().reset_index()
    
    axis = sns.barplot(x="Location", y="Precipitation_mm", data=groupedData, hue="Precipitation_mm", legend=False, palette="mako_r")
    
    for bar in axis.patches:
        bar.set_edgecolor('black')
        bar.set_linewidth(0.5)
        
    plt.title("Avarage Precipitation")
    plt.ylabel("Precipitation (mm)")
    plt.xticks(rotation=45)
    plt.xlabel("Cities")
    plt.show()
    

def AvarageWindSpeedVisualisation(weatherData):
    groupedData = weatherData.groupby(["Location"])["Wind_Speed_kmh"].mean().sort_values().reset_index()
    
    axis = sns.barplot(x="Location", y="Wind_Speed_kmh", data=groupedData, hue="Wind_Speed_kmh", legend=False, palette="RdYlGn_r")
        
    for bar in axis.patches:
        bar.set_edgecolor('black')
        bar.set_linewidth(0.5)
        
    plt.title("Avarage Wind Speed")
    plt.ylabel("Wind Speed (kmh)")
    plt.xticks(rotation=45)
    plt.xlabel("Cities")
    plt.show()



def CityTemperatureVisualisation(weatherData, cityName):
    dataForCity = weatherData[weatherData["Location"] == cityName]
    dataForCity = dataForCity.sort_values("Date_Time")
    
    sns.jointplot(x="Date_Time", y="Temperature_C", data=dataForCity, color="g")
    
    plt.title(f"Temperatures for {cityName}")
    plt.ylabel("Temperature (°C)")
    plt.xlabel("Date")
    plt.show()
    

def CityHumidityVisualisation(weatherData, cityName):
    dataForCity = weatherData[weatherData["Location"] == cityName]
    dataForCity = dataForCity.sort_values("Date_Time")
    
    sns.jointplot(x="Date_Time", y="Humidity_pct", data=dataForCity, color="g")
    
    plt.title(f"Humidity for {cityName}")
    plt.ylabel("Humidity (%)")
    plt.xlabel("Date")
    plt.show()
    

def CityPrecipitationVisualisation(weatherData, cityName):
    dataForCity = weatherData[weatherData["Location"] == cityName]
    dataForCity = dataForCity.sort_values("Date_Time")
    
    sns.jointplot(x="Date_Time", y="Precipitation_mm", data=dataForCity, color="g")
    
    plt.title(f"Precipitation for {cityName}")
    plt.ylabel("Precipitation (mm)")
    plt.xlabel("Date")
    plt.show()
    

def CityWindSpeedVisualisation(weatherData, cityName):
    dataForCity = weatherData[weatherData["Location"] == cityName]
    dataForCity = dataForCity.sort_values("Date_Time")
    
    sns.jointplot(x="Date_Time", y="Wind_Speed_kmh", data=dataForCity, color="g")
    
    plt.title(f"Avarage Wind Speed for {cityName}")
    plt.ylabel("Wind Speed (kmh)")
    plt.xlabel("Date")
    plt.show()
    

def CityDependencyBetweenHumidityAndPrecipitation(weatherData, cityName):
    dataForCity = weatherData[weatherData["Location"] == cityName]
    dataForCity = dataForCity.sort_values("Date_Time")
    
    sns.jointplot(x="Precipitation_mm", y="Humidity_pct", data=dataForCity, color="g",  kind="reg")
    
    plt.title(f"Dependency between humidity and precipitation for {cityName}")
    plt.ylabel("Precipitation (mm)")
    plt.xlabel("Humidity (%)")
    plt.show()