import json
import requests

CITY = 'Calgary'

def getApiData():
    if not (CITY):
        city = input("Enter your city: ")
    url = 'http://api.weatherapi.com/v1/current.json?key=1df07905d29f407cb9b211248230109&q=Calgary/'
    response = requests.get(url)
    return response.json()

allData = getApiData()
print(allData)

def objectify(data): 
    locationData = allData['location']
    city = locationData['name']
    region = locationData ['region']
    country = locationData['country']
    temp_c = locationData['temp_c']
print("Weather in "+city+", " +region + ", "+country+": ")
print("Temperature: ")
