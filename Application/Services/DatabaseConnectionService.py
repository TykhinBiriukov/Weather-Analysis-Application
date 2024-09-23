import Services.DatabaseService as dbService

def DatabaseConnection():
    dbPath = "D:\Programming\Projects\C#\Weather Application\Application\Files\Forecastdata.db"
    connection = dbService.ConnectToDatabase(dbPath)
    groupedData = dbService.ReadAndGroupDataByCity(connection)
    return groupedData