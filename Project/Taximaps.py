from geopy import distance

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="taxiwork")
import requests 


from requests import get

ip = get('https://api.ipify.org').text

r = requests.get('https://get.geojs.io/')
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
myip = ip_request.json()['ip']


url= 'https://get.geojs.io/v1/ip/geo/'+ip+'.json'
geo_request = requests.get(url)
geo_data = geo_request.json()

#Getting your location 

yourcoordinates = str(geo_data['latitude'])+","+str(geo_data['longitude'])

def show_full_add(add_coordinate,msg = "Your address"):     # This needs co ordinates 
    while True:
        try :
            location = geolocator.geocode(add_coordinate)
            print(msg)
            print(location)
            break
        except:
            print("Enable to find you")
    return str(location)

def get_distance_cost(source_name,destination_name,isCurrEqual_source):
    if isCurrEqual_source == False: # Source is not my location
        for i in range(10):
            try:
                add_obj = geolocator.geocode(source_name)
                coor_source = str(add_obj.latitude)+","+str(add_obj.longitude)
                add_obj = geolocator.geocode(destination_name)
                coor_destination = str(add_obj.latitude)+","+str(add_obj.longitude)
                break
            except:
                print("Finding Routes")

    elif isCurrEqual_source == True: # Source is my location 
        for i in range(10):
            try:
                coor_source = yourcoordinates
                add_obj = geolocator.geocode(destination_name)
                coor_destination = str(add_obj.latitude)+","+str(add_obj.longitude)        
                break
            except:
                print("Finding co-ordinates")
    s1 = show_full_add(coor_source,source_name)
    s2 = show_full_add(coor_destination,destination_name)
    print()
    print("The distance between "+source_name+" and "+destination_name +" is equal to")
    while True:
        try:
            x = round(float(distance.distance(coor_source, coor_destination).km),2)
            break
        except:
            print('Calculating distance ')
    print(x)
    return(s1,s2,x)

