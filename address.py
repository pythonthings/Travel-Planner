import copy 
class Address():
    def __init__(self, address, distance, time, parent, hit_list):
        #google api 
        self.address = address 
        self.distance = distance #miles 
        self.time = time #minutes
        self.hit_list = hit_list
        

        self.parent = parent
        self.children = {}

    def __str__(self):
        return "\n~~~~~\naddress: " + str(self.address) + "\ndistance: " + str(self.distance) + "\ntime: " + str(self.time) + "\n~~~~~"

    def __lt__(self, other):
        return self.distance < other.distance