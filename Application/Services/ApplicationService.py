import Services.PrintingService as printDataService
import Services.VisualisationService as visualService


def Case1(weatherData):
    print("Choose city for analysis:")
    printDataService.PrintCitiesList
    cityInput = input()
    
    print("Choose parameter for analysis:")
    printDataService.PrintParametersList()
    parameterInput = input()
    
    if (parameterInput == "1"):
        visualService.CityTemperatureVisualisation(weatherData, cityInput)
    
    elif (parameterInput == "2"):
        visualService.CityHumidityVisualisation(weatherData, cityInput)
        
    elif (parameterInput == "3"):
        visualService.CityWindSpeedVisualisation(weatherData, cityInput)
    
    elif (parameterInput == "4"):
        visualService.CityPrecipitationVisualisation(weatherData, cityInput)
    
    elif (parameterInput == "5"):
        visualService.CityDependencyBetweenHumidityAndPrecipitation(weatherData, cityInput)



def Case2(weatherData):
    print("Choose parameter for analysis:")
    printDataService.PrintParametersList()
    parameterInput = input()
    
    if (parameterInput == "1"):
        visualService.AvarageTemperatureVisualisation(weatherData)
    
    elif (parameterInput == "2"):
        visualService.AvarageHumidityVisualisation(weatherData)
        
    elif (parameterInput == "3"):
        visualService.AvarageWindSpeedVisualisation(weatherData)
    
    elif (parameterInput == "4"):
        visualService.AvaragePrecipitationVisualisation(weatherData)
    
    elif (parameterInput == "5"):
        print("Not available for multiple cities")