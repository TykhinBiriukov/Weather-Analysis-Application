def PrintCitiesList(weatherData):
    citiesRow = set(weatherData.groups.keys())
    citiesList = list(citiesRow)
    
    for i, city in enumerate (citiesList, start=1):
        print(f"{i}. {city}")
        
        
def PrintParametersList():
    parametersList = ["Temperature", "Humidity", "Wind Speed", "Precipitation volume", "Dependency between humidity and precipitation"]
    
    for i, parameter in enumerate (parametersList, start=1):
        print(f"{i}. {parameter}")