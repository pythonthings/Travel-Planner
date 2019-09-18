from address import Address
from google_maps_utility import GoogleMapsUtility
import heapq
import copy

class Best_First():
    def __init__(self, start, hit_list, heuristic):
        self.hit_list = copy.deepcopy(hit_list)
        self.start = start

        self.best_distance = 0
        self.best_time = 0
        self.route = ""
        self.total_count = len(hit_list)+1

        self.heuristic = heuristic

        self.open = []
        heapq.heapify(self.open)
        self.closed = []
        heapq.heapify(self.closed)

        self.algorithm(Address(self.start, 0, 0, "", self.hit_list))

    def __str__(self):
        if self.heuristic == "distance":
            return f"~\n~~~\n~~~~~\n\t\tbest route: {self.route}\n\t\tbest distance: {self.meters_to_miles()} miles\n~~~~~\n~~~\n~"
        elif self.heuristic == "time":
            return f"~\n~~~\n~~~~~\n\t\tbest route: {self.route}\n\t\tbest time: {self.seconds_to_time()}\n~~~~~\n~~~\n~"

    def algorithm(self, next_state):
        root = next_state
        self.hit_list = root.hit_list

        if len(root.hit_list) == 0:
            #saving data
            foo = root
            for point in range(self.total_count):
                self.route = foo.address + " -> " + self.route
                self.best_distance = self.best_distance + foo.distance
                self.best_time = self.best_time + foo.time
                foo = foo.parent
            self.route = self.route[:-4]
            
            return ''

        for point in range(len(root.hit_list)):
            point_A = root.address
            point_B = root.hit_list[point]

            connection = GoogleMapsUtility()
            distance, time = connection.directionsRequest(point_A, point_B)

            interior_list = copy.deepcopy(root.hit_list)
            interior_list.remove(point_B)

            if self.heuristic == "distance":
                heapq.heappush(self.open, (distance, Address(point_B, distance, time, root, interior_list)))
            elif self.heuristic == "time":
                heapq.heappush(self.open, (time, Address(point_B, distance, time, root, interior_list)))

            #add children to root. key = address, value = Address
            root.children[point_B] = Address(point_B, distance, time, root, interior_list)

        #pop min off min-heap
        popped = heapq.heappop(self.open) #(miles/time, Address)
        heapq.heappush(self.closed, popped)
        addr = popped[1]

        #remove explored from list
        self.hit_list = addr.hit_list

        self.algorithm(addr)

    def meters_to_miles(self):
        return round((self.best_distance/1000) * 0.62137)

    def seconds_to_time(self):
        # https://www.w3resource.com/python-exercises/python-basic-exercise-65.php
        time = self.best_time
        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        return f"{day} days {hour} hours {minutes} minutes"
