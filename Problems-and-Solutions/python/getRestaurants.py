# A python script that will make a list of all restauarants in 5 miles
# Implemented with Google Maps API

import requests
import json
import urllib.parse
import re
import os 
from tkinter import *
from tkinter import messagebox


# creates the view 
def View():
    # setting up the view
    window = Tk()
    window.title("Get Restaurants App")
    window.geometry('420x200')
    lbl = Label(window, text="Enter Address: ")
    lbl.grid(column=0, row=0)
    txt = Entry(window)
    txt.grid(column=1, row=0, columnspan=2,)
    listbox = Listbox(window)
    listbox.grid(column=0, row=1, columnspan=4, sticky=N+E+S+W, padx=5, pady=5)
    listbox.config(width=0)
    window.winfo_toplevel().wm_geometry("")
    # # resizing the grids so that they fit to the contents
    # for i in range(3):
    #     window.grid_columnconfigure(i, weight=1)

    def clicked():
        address_txt = txt.get()
        if address_txt == '':
            messagebox.showerror("Error", "Please enter an address!")
            return

        getPlaces(address_txt)

        # read in the restaraunts line by line from places.txt generated in getPlaces method
        with open('Places.txt') as f:
            content = f.readlines()
        content = [x.strip('\n') for x in content] 

        # clear previous info in listbox
        listbox.delete(0,END)

        for index, i in enumerate(content):
            listbox.insert(index, i)

    btn = Button(window, text="Find restaurants", command=clicked, padx=5)
    btn.grid(column=3, row=0)

    window.mainloop()

# Get a list of places based on input location (in radius of 8000 meters(5 miles) ) and output into a text file
def getPlaces(input_address):
    # getting the geolocation of the address as a input parameter for Google maps places API

    # Registered for an enabled Google API project to get this API key, will be used to call Google Maps API in getPlaces and getLocation methods 

    API_key = "AIzaSyB3-8q6wF2coQppBg6-uRBoepL07eCAcWw"

    input_address = input_address.replace(' ', '+')
    # parameters for getting the geolocation of address
    loc_parameters = {'address': input_address, 'key': API_key}

    r_location = requests.get("https://maps.googleapis.com/maps/api/geocode/json?",params=loc_parameters)

    j_location = r_location.json()

    geo_lat = j_location['results'][0]['geometry']['location']['lat']
    geo_long = j_location['results'][0]['geometry']['location']['lng']

    geo_loc = str(geo_lat) + ', ' + str(geo_long)

    places_parameters = {'query': 'restaurants', 'location': geo_loc, 'radius': 8000, 'key': API_key}

    r_places = requests.get(
        "https://maps.googleapis.com/maps/api/place/textsearch/json?", params=places_parameters)
    j_places = r_places.json()

    if "error_message" in j_places:
        print('ERROR: ' + j_places['error_message'])
        sys.exit()

    else:
        place_name_list = []
        place_address_list = []
        for index in range(len(j_places['results'])):
            # get place name
            place_name = j_places['results'][index]['name'].encode('ascii', 'ignore')
            str_place_name = place_name.decode('utf-8')

            # get place address
            place_address = j_places['results'][index]['name'].encode('ascii', 'ignore')
            str_place_address = place_address.decode('utf-8')
            place_name_list.append(str_place_name)

            # get a geo location and convert to human readable address using Google APIs reverse geocoding
            place_lat = j_places['results'][index]['geometry']['location']['lat']
            place_lng = j_places['results'][index]['geometry']['location']['lng']
            place_latlng = str(place_lat) + ', ' + str(place_lng)

            places_parameters = {'latlng': place_latlng, 'key': API_key}
            r_place_location = requests.get("https://maps.googleapis.com/maps/api/geocode/json?l",params=places_parameters)

            j_place_location = r_place_location.json()
            str_location = j_place_location['results'][0]['formatted_address']
            place_address_list.append(str_location)

        # remove Places.txt if already exists
        try:
            os.remove('Places.txt')
        except OSError:
            pass

        with open('Places.txt', 'w') as f:
            for i in range(len(j_places['results'])):
                print(str(place_name_list[i]) + ', ' + str(place_address_list[i]))
                f.write(str(place_name_list[i]) + '; ' + str(place_address_list[i]) + '\n')


if __name__ == "__main__":
    View()
