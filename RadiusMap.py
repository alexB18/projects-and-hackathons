import urllib.request
import json
import pandas as pd

#start of URL
PLACE_URL_BASE = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
GEO_URL_BASE = 'https://maps.googleapis.com/maps/api/geocode/json?'

#key
api_key = 'AIzaSyCz_fTLy-L-adRcPTOqqXfOFyBBMex6UkM'
DONE_api_key = '&key=' + api_key


class RadiusMap:

                                   #Address            #Meters
    def __init__(self, start_address: str, search_radius: int, destination_types: list):
        self.start_address = start_address
        self.search_radius = search_radius
        self.destination_types = destination_types

        self.DONE_start_address = 'address=' + start_address.replace(' ', '+')
        self.DONE_search_radius = '&radius=' + str(search_radius)

        #initialize map with no start_geo
        self.start_geo = None


    def get_start_address(self):
        return self.start_address

    def get_search_radius(self):
        return self.search_radius

    def generate_start_geo(self):
        '''Convert address into latitude and longitude
                        Create geo request url'''
        start_geo_request = GEO_URL_BASE + self.DONE_start_address + DONE_api_key

        # Get Response from geo request
        start_geo_response = urllib.request.urlopen(start_geo_request).read()

        # Load response into JSON
        start_geo_json = json.loads(start_geo_response)

        # Finally, Get start_geo lattitude and longitude
        lat = str(start_geo_json['results'][0]['geometry']['location']['lat'])
        lng = str(start_geo_json['results'][0]['geometry']['location']['lng'])

        self.start_geo = (lat, lng)

    def get_location_types(self):
        return self.location_types

    def set_start_coord(self, start_coord: (float, float), search_radius: float):
        return None

if __name__ == "__main__":
    Map = RadiusMap("952 Olive Street Eugene, OR 97401", 800, ["library"])
    Map.generate_start_geo()
    print(Map.start_geo)





