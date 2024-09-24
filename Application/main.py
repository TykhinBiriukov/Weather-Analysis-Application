import Services.DatabaseConnectionService as dbConnectionService
import Services.JsonReaderService as jsonReadService
import Services.ApplicationService as appService

weatherData = jsonReadService.ReadJsonAndReturnWeatherData() #dbConnectionService.DatabaseConnection()

while (True):
    userInput = input("\nMenu:\
        \n1. Analyse once city over some period of time\
        \n2. Analyse avarage data from all cities\
        \n3. Exit\
        \nChoose which type of analysis you want: ")
    

    if (userInput == '1'):
        appService.Case1(weatherData)
    
    elif (userInput == '2'):
        appService.Case2(weatherData)
    
    elif (userInput == '3'):
        break
    
    else:
        print("Please enter number from 1 to 3")
