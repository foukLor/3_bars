import json
import sys
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath,'r') as data_file:
        data = json.load(data_file)
    return data



def get_biggest_bar(data):
    max_bar = max(data, key = lambda event: event['Cells']['SeatsCount'])
    return max_bar['Cells']['Name']


def get_smallest_bar(data):
    min_bar = min(data, key = lambda event: event['Cells']['SeatsCount'])
    return min_bar['Cells']['Name']


#we use eucledian metrics
def get_closest_bar(data, longitude, latitude):
    min_destination = min(data,key= lambda bar: ((longitude - bar['Cells']['geoData']['coordinates'][0])**2
         + (latitude - bar['Cells']['geoData']['coordinates'][1])**2 )**(1.0/2))
    return min_destination['Cells']['Name']



if __name__ == '__main__':
    if  len(sys.argv) != 2:
        print(" Usage:python3.5 bars.py file path to json")
    x_gps = float(input("longitude:"))
    y_gps = float(input("latitude:"))
    data = load_data(sys.argv[1])
    if data is None :
        exit("data is invalid")
    max_bar = get_biggest_bar(data)
    min_bar = get_smallest_bar(data)
    near_bar = get_closest_bar(data, x_gps, y_gps)
    print("\nThe biggest moscow's bar is:")
    print(max_bar)
    print("\nThe smallest moscow's bar is ")
    print(min_bar)
    print("\nThe nearest moscow's bar is ")
    print(near_bar)
