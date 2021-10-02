#!/usr/bin/env python

rh = {
    "username": "",
    "password": "",
}

config = {
    "statusEmailAddress": "",
    "cashToReserve": 165,
    "buyLimit": 1.0025,
    "sellLimit": 0.995,
    "exponentialMovingAverage": 20,
    "movingAverageShort": 20,
    "movingAverageLong": 50,    # Ticks are 5 min long
    "runMinute": [0,5,10,15,20,25,30,35,40,45,50,55],
    "coinList": ["LTC"],
    "tradesEnabled": True,
    #"rsiWindow": 48,
}




