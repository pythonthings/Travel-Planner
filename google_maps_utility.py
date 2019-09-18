##
# API KEY AIzaSyAY1aatbdVCglJhXI0HFddm5pEkPTUpBFU
#python3.6
# importing required libraries
import sys 

"""
using Google Maps API to get directions from \

- start point to end end_point
- purpose is
- - to grab the distance in miles from start to end_point
- - to grab time in hours and minutes from start to end point

"""
import requests, json


class GoogleMapsUtility():
    def __init__(self):
        self.api_key = 'AIzaSyAlFOfYJqGZR3a_5VcbrihyaproXXWTeY4'

    def directionsRequest(self, start_point, end_point):
        try:
            # url variable store url
            url ='https://maps.googleapis.com/maps/api/directions/json'
            # Get method of requests module
            payload = {'key':self.api_key,'origin':start_point,'destination':end_point}
            # makes google directions API requests
            response = requests.get(url,params=payload)
            # grabs JSON object from API request
            data = response.json()
            # checks if the status is successful
            if response.status_code == 200:
                # iterates throught the JSON object
                for directions in data['routes'][0]['legs']:
                    # gets distance dictionary from json
                    distance = directions['distance']
                    # gets duration dictionary from json
                    duration = directions['duration']
                    # get the value from distance
                    distance_miles = distance.get("value") #meters
                    # get the value from duration
                    duration_hours = duration.get("value") #seconds
                    return int(distance_miles), int(duration_hours)

            elif response.status_code != 200:
                print(response.status_code)
                print(response.json())
                return response.status_code
        
        except:
            sys.exit("Something went wrong! Try again.")