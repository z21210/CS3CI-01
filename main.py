import numpy as np
from enum import Enum
from random import randint
import csv
import math as maths
from itertools import permutations

Cities = {}
with open('ulysses16.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        Cities[row['id']] = [float(row['x']), float(row['y'])]
CITIES = list(Cities.keys())

City = Enum('City', [[CITIES[i], i] for i in range(len(CITIES))])

def getEuclideanDistance(fromCity, toCity):
    fromName = City(fromCity).name
    toName = City(toCity).name
    fromX, fromY = Cities[fromName]
    toX, toY = Cities[toName]
    return maths.sqrt((toX - fromX)**2 + (toY - fromY)**2)


CONNECTIONS = np.zeros((len(CITIES), len(CITIES)))
for y in range(0, len(CITIES)):
    for x in range(0, len(CITIES)):
        CONNECTIONS[y][x] = getEuclideanDistance(y, x)

def getDistance(fromCity, toCity):
    return CONNECTIONS[fromCity, toCity]

def randElement(list):
    length = len(list)
    randIndex = randint(0, length-1)
    return list[randIndex]

def generateRoute():
    cityCount = len(CITIES)
    route = []
    unvisitedCities = list(range(0, cityCount))
    home = randElement(unvisitedCities)
    route.append(home)
    unvisitedCities.remove(home)
    for i in range(len(unvisitedCities)):
        city = randElement(unvisitedCities)
        route.append(city)
        unvisitedCities.remove(city)
    route.append(home)
    return route

def evaluateRoute(route):
    totalDistance = 0
    for i in range(0, len(route) - 1):
        fromCity = route[i]
        toCity = route[i+1]
        distance = getDistance(fromCity, toCity)
        totalDistance += distance
    return totalDistance

def nameRoute(route):
    return list(map(lambda city: City(city).name, route))

def formatRoute(route):
    formatted = ''
    for i in range(0, len(route) - 1):
        formatted += str(route[i]) + ' -> '
    formatted += str(route[len(route) - 1])
    return formatted

r = generateRoute()
print(f'Route: {formatRoute(nameRoute(r))}\nDistance: {evaluateRoute(r)}')

# allRoutes = list(permutations(CITIES))
# bestRoute = None
# bestDistance = None
# for i in range(0, len(allRoutes)):
#     allRoutes[i] = list(allRoutes[i] + (allRoutes[i][0],))
#     distance = evaluateRoute(allRoutes[i])
#     if (bestDistance is None) or (distance < bestDistance):
#         bestRoute = allRoutes[i]
#         bestDistance = distance

# print(list(allRoutes))
# print(f'Best Route: {formatRoute(nameRoute(bestRoute))}\nBest Distance: {bestDistance}')