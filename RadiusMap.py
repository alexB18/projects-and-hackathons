import urllib.request
import json
import re
import random
import pandas as pd

# starts of URLs
DESTINATION_URL_BASE = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
GEO_URL_BASE = 'https://maps.googleapis.com/maps/api/geocode/json?'
DISTANCE_MATRIX_URL_BASE = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
ROUTE_URL_BASE = 'https://maps.googleapis.com/maps/api/directions/json?'

# key
api_key = 'AIzaSyDGI3yK0ZiDsCG21TDLn6qraXAXhZXmyE0'
DONE_api_key = '&key=' + api_key


class RadiusMap:
                                    #Address             Meters
    def __init__(self, start_address: str, search_radius: int, destination_types: list):
        # Set start_address, search_radius, etc.
        self.start_address = start_address
        self.search_radius = search_radius
        self.destination_types = destination_types

        # 'DONE' attributes
        self.DONE_start_address = 'address=' + start_address.replace(' ', '+')
        self.DONE_search_radius = '&radius=' + str(search_radius)

        # initialize map with no start_geo and no DONE_start_geo
        self.start_geo = None
        self.DONE_start_geo = None

        # initialize destinations as None
        self.destinations = None
        # initialize destinations_dataframe as None
        self.destinations_dataframe = None
        # initialize destinations_coordinates as empty list
        self.possible_route_coordinates = []
        # initialize current_route as empty list
        self.current_route = []

        # initialize distances_dataframe as None
        self.distances_dataframe = None


    def get_start_address(self):
        return self.start_address

    def get_search_radius(self):
        return self.search_radius

    def get_destination_types(self):
        return self.destination_types

    def generate_destinations_dataframe(self):
        """ ONLY CALL THIS FUNCTION AFTER GENERATING STARTING GEOLOCATION
            IT WILL NOT WORK OTHERWISE. YOU HAVE BEEN WARNED!!"""
        self.destinations_dataframe = pd.DataFrame(columns=['name', 'geolocation'])

        for i in self.get_destination_types():

            '''For each type of destination, request name and geolocation'''
            destination_type = i
            DONE_destination_type = '&type=' + destination_type

            # create destinations_request url
            destinations_request = DESTINATION_URL_BASE + self.DONE_start_geo + DONE_destination_type + self.DONE_search_radius + DONE_api_key

            # Get response from destinations_request
            destinations_response = urllib.request.urlopen(destinations_request).read()

            # Load response into json
            destinations_json = json.loads(destinations_response)

            # Stick starting location at beginning of self.possible_route_coordinates
            self.possible_route_coordinates.append(self.start_geo)

            # Finally, for every destination in destination_type, retrieve lat, lng and geolocation
            for j in range(0, len(destinations_json['results'])):
                lat = str(destinations_json['results'][j]['geometry']['location']['lat'])
                lng = str(destinations_json['results'][j]['geometry']['location']['lng'])

                geo_location = lat + ',' + lng
                self.possible_route_coordinates.append(geo_location)

                name = str(destinations_json['results'][j]['name'])

                tempDF = pd.DataFrame({'name':[name], 'geolocation': [geo_location]})

                self.destinations_dataframe = self.destinations_dataframe.append(tempDF)

        self.destinations_dataframe = self.destinations_dataframe.reset_index(drop=True)

        print(self.destinations_dataframe, "\n")

    def generate_start_geo(self):
        '''Convert address into latitude and longitude
                            Create geo request url'''
        start_geo_request = GEO_URL_BASE + self.DONE_start_address + DONE_api_key

        # Get Response from geo request
        start_geo_response = urllib.request.urlopen(start_geo_request).read()

        # Load response into json
        start_geo_json = json.loads(start_geo_response)

        # Finally, Get start_geo lattitude and longitude
        lat = str(start_geo_json['results'][0]['geometry']['location']['lat'])
        lng = str(start_geo_json['results'][0]['geometry']['location']['lng'])

        self.start_geo = lat + ',' + lng
        self.DONE_start_geo = 'location=' + self.start_geo

    def plot_route_from_geolocations(self, route_coordinates: list, travel_mode: str):
        #https://maps.googleapis.com/maps/api/directions/json?origin=sydney,au&destination=perth,au&waypoints=via:-37.81223%2C144.96254%7Cvia:-34.92788%2C138.60008&key=

        possible_coordinates = []
        DONE_waypoints = '&waypoints='
        DONE_travel_mode = '&mode=' + travel_mode

        for coordinate in route_coordinates:
            stripped_coordinate = coordinate.split(",")
            possible_coordinates.append(stripped_coordinate)

        origin_lat = possible_coordinates[0][0]
        origin_lng = possible_coordinates[0][1]
        DONE_origin = '&origin=' + origin_lat + ',' + origin_lng

        destination_lat = possible_coordinates[-1][0]
        destination_lng = possible_coordinates[-1][1]
        DONE_destination = '&destination=' + destination_lat + ',' + destination_lng

        if(len(possible_coordinates) > 2):
            DONE_waypoints = DONE_waypoints + 'via:' + possible_coordinates[2][0] +'%2C' + \
                             possible_coordinates[2][1]

            for i in range(3, len(possible_coordinates) - 1):
                DONE_waypoints = DONE_waypoints + '%7C' + possible_coordinates[i][0] + '%2C' + \
                                 possible_coordinates[i][1]

        # Create route_request url
        route_request = ROUTE_URL_BASE + DONE_travel_mode + DONE_origin + DONE_destination + DONE_waypoints + DONE_waypoints + DONE_api_key

        # Get response from route_request
        route_response = urllib.request.urlopen(route_request).read()

        # Load response into json
        route_json = json.loads(route_response)


        for i in range(len(route_json['routes'][0]['legs'][0]['steps'])):
            instruction1 = str(route_json['routes'][0]['legs'][0]['steps'][i]['html_instructions'])
            instruction1 = re.sub('<[^<]+?>', '', instruction1)
            print(instruction1)

        print("")
        for j in range(0, len(route_json['routes'][0]['legs'][1]['steps'])):
            instruction2 = str(route_json['routes'][0]['legs'][1]['steps'][j]['html_instructions'])
            instruction2 = re.sub('<[^<]+?>', '', instruction2)
            print(instruction2)


        print("")
        for k in range(0, len(route_json['routes'][0]['legs'][2]['steps'])):
            instruction3 = str(route_json['routes'][0]['legs'][2]['steps'][k]['html_instructions'])
            instruction3 = re.sub('<[^<]+?>', '', instruction3)
            print(instruction3)

        print("")
        for l in range(0, len(route_json['routes'][0]['legs'][3]['steps'])):
            instruction4 = str(route_json['routes'][0]['legs'][3]['steps'][l]['html_instructions'])
            instruction4 = re.sub('<[^<]+?>', '', instruction4)
            print(instruction4)

        print("")
        for m in range(0, len(route_json['routes'][0]['legs'][4]['steps'])):
            instruction5 = str(route_json['routes'][0]['legs'][4]['steps'][m]['html_instructions'])
            instruction5 = re.sub('<[^<]+?>', '', instruction5)
            print(instruction5)


    def generate_random_route(self, possible_coordinates: list, num_of_waypoints: int):
        random_route = []

        random_route.append(possible_coordinates[0])
        for i in range(0, num_of_waypoints + 1):
            random_route.append(possible_coordinates[random.randrange(1, len(possible_coordinates))])

        random_route.append(possible_coordinates[0])

        self.current_route = random_route

