import pandas as pd

# list of all the file names that will be used for analysis
files = ['Bike share ridership 2024-01.csv', 'Bike share ridership 2024-02.csv', 'Bike share ridership 2024-03.csv',
         'Bike share ridership 2024-04.csv', 'Bike share ridership 2024-05.csv', 'Bike share ridership 2024-06.csv', 
         'Bike share ridership 2024-07.csv', 'Bike share ridership 2024-08.csv', 'Bike share ridership 2024-09.csv']

station_count = {}      # will contains the total number of trips for each station
love_park_stn_count = 0

def get_busiest_stations(love_park_stn_count, col):
    """
    Gets the top 5 busiest Bike Share stations of 2024 using the available data
    """

    if col == "Start":
        stn_id = 'Start Station Id'
        stn_name = 'Start Station Name'
    else:
        stn_id = 'End Station Id'
        stn_name = 'End Station Name'

    for file in files:  # iterates through all of the files 
        data = pd.read_csv(file, encoding='ISO-8859-1') # reads each file using the specified encoding
        print(f"Opened {file}")
        bike_share_dict = data.to_dict(orient='records')    # turns data into a dictionary for better access
        print(f"Turned into dictionary")

        for trip in bike_share_dict:    # iterates through the dictionary containing all the information of the trips
            station_id = trip[stn_id]   # gets the station ID since it's the dictionary key

            if station_id not in station_count: # if station ID is not in the dictionary
                station_count[station_id] = {'Station Name': trip[stn_name], 'Trips Count': 1}  # create a new key with values of the station name and trip count starting at 1

            else:   
                station_count[station_id]['Trips Count'] += 1   # else just add one to the count
            
            if trip["Start Station Name"] == "York St / Harbour St (Love Park)":    # had to manually count love park station; too much information and will not access it through dictionary
                love_park_stn_count += 1    # adds one to the count

    sorted_data = sorted(station_count.items(), key=lambda trip: trip[1]['Trips Count'], reverse=True)  # sorts the total trips of each station from highest to lowest
    sorted_data_lowest_first = sorted(station_count.items(), key=lambda trip: trip[1]['Trips Count'], reverse=False)    # sorts the total trips of each station from lowest to highest

    print(f"\nTop 5 Busiest {col} Stations in 2024")    # prints top 5 busiest start/stop stations in 2024
    for i in range(5):  # iterates only 5 times
        print(f"\n{i+1}. \nStation Name: {sorted_data[i][1]['Station Name']} - {int(sorted_data[i][0])}\nCount: {sorted_data[i][1]['Trips Count']}")    # prints the station name, ID, and count

    return sorted_data, love_park_stn_count, sorted_data_lowest_first   # returns both of the sorted dictionaries

def get_volume(sorted_data, love_park_stn_count):
    """
    Gets the volume of specified stations 
    """
    # close_stations = ["Bay St / Queens Quay W (Ferry Terminal)", "Queens Quay W / Lower Simcoe St", "Queens Quay / Yonge St", "Church St / Wood St"]    # for start stations
    close_stations = ["King St W / York St", "King St W / Jordan St", "Wellington St W / Bay St", "King St W / Bay St (East Side)", 
                      "Yonge St / Harbour St", "12 Harbour St"]    # for end stations
    
    close_stations_info = {}

    for station in close_stations:  # goes through each station in the list
        print(f"\nFinding Info For: {station}")
        for trip in sorted_data:    # loops through the sorted info to look for the current station it's looking for
            if trip[1]["Station Name"] == station:  # if current station is found
                print("Adding information")
                close_stations_info[trip[0]] = trip[1]  # adds the number of trips of that station
                break   # breaks so it doesn't have to go through the entire dictionary once found


    print(f"\n{close_stations_info}")   # prints the information added for each station in the closeby stations list
    # print(f"York St / Harbour St (Love Park) -- count: {love_park_stn_count}")  # for start stations

def get_average(sorted_data):
    """
    Gets the average trip count for 2024 using the sorted data
    """
    total_trips = 0
    for trip in sorted_data:    # for each trip within the dictionary
        total_trips += trip[1]['Trips Count']   # add each trip count 
    num_trips = len(sorted_data)    # gets the number of entries in dictionary
    avg = total_trips/num_trips # calculates the average

    print(f"\nAverage Number of Trips: {avg:.2f}\n")    # prints average with only up to 2 decimal points

def get_lowest(sorted_data_lowest_first):
    """
    Using the dictionary sorted from lowest to highest, gets the station with the lowest volume
    """
    print(sorted_data_lowest_first)
    info = sorted_data_lowest_first[0][1]   # because of the dataset, some are `nan`, had to print out the list and find the lowest manually
    print(info) 

def obs_start_stn(love_park_stn_count):
    """
    Oberserves the start station volume count
    """
    sorted_data, love_park_stn_count, sorted_data_lowest_first = get_busiest_stations(love_park_stn_count, "Start")
    get_volume(sorted_data, love_park_stn_count)
    get_average(sorted_data)
    get_lowest(sorted_data_lowest_first)

def osb_end_stn(love_park_stn_count):
    """
    Obeserves the end station volume count
    """
    sorted_data, love_park_stn_count, sorted_data_lowest_first = get_busiest_stations(love_park_stn_count, "End")
    get_volume(sorted_data, love_park_stn_count)
    get_average(sorted_data)
    get_lowest(sorted_data_lowest_first)

# obs_start_stn(love_park_stn_count)    # uncomment this along with line 54 and comment out line 55 and 56 to observe start stations only
osb_end_stn(love_park_stn_count)