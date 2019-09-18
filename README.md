![PyPI - Python Version](https://img.shields.io/badge/python-3.7-blue)


# Travel Planner
Create a list of places that you can visit and provide multiple ways to move between cities. For this travel planner, there will only be traveling by car. The user will provide a starting location and multiple locations they want to travel to and indicate their preferences -- fastest way to reach the destination, time wise or distance wise.


# Technical implementation
We implemented the Best-First search algorithm on our states and state space. For our states, we used a class structure holding multiple properties to determine how to create the state space. Rather than creating the large state space first and then running the algorithm, we created multiple trees, look through their descendants, and implementing Best-First search algorithm, and repeat until we finally hit all our locations. With the final location visited, the program will be able to give the user the route they should take and the distance/time it will be (depending on user preference).

### Compile application - recommended
1. using a virtual environment: virtualenv venv
2. source bin/venv/activate
3. pip install requests
4. python3.7 app.py

# Summary
1. We will be allowing the user to enter an address where they would start.
2. Users will then add addresses that they want to travel to during their vacation.
3. We will use that information to pass an arguments to a GOOGLE MAP API request.
  1. the Google map API request will give us the miles or durations from the starting point to the other cities.
  2. we will store that information to a data structure.
4. we will use the data structure to perform a best first search to find out what the most optimal route would to travel.


# Technologies used
1. [Google API](https://developers.google.com/maps/documentation/directions/start)
2. Best First search algorithm


#### example

---------------- sample -----------------

Would you like the shortest distance or fastest time? (distance or time): distance
Enter starting point (Address, City, or State): california
Enter a destination (enter -1 to end): washington
Enter a destination (enter -1 to end): florida
Enter a destination (enter -1 to end): -1

		best route: california -> florida -> washington
		best distance: 5767 miles
