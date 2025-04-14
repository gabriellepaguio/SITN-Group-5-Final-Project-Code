import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

data_file = 'Bike share ridership 2021-01.csv' # 2021 DATASET IMPORTANT CHOOSE ONE!!!
# data_file = 'Bike share ridership 2024-01.csv' # 2024 DATASET IMPORTANT CHOOSE ONE!!!
df = pd.read_csv(data_file) # Read either CSV file

start_time_data = ['Start Time'] # Define that we only want Start Time from dataset
df = df[start_time_data] # Extract the Start Time column from the dataset

df['Start Time'] = pd.to_datetime(df['Start Time']) # Convert 'Start Time' to datetime format

df['Hour'] = df['Start Time'].dt.hour # Extract hour from start time
df['Day of Week'] = df['Start Time'].dt.day_name() # Extract day of the week from start time

most_common_hour = df['Hour'].mode()[0] # Get most common hour for start time
most_common_day = df['Day of Week'].mode()[0] # Get most common day of the week for start time

rush_hours = range(7, 10)  # Define rush hours as between 7 and 9 AM
evening_rush_hours = range(16, 19)  # Define evening rush hours as between 4 and 6 PM
weekday_rush_hours = list(rush_hours) + list(evening_rush_hours) # Combine morning and evening rush hours

weekday_trips = df[df['Day of Week'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])]  # Filter for weekdays

weekday_trips['Is Rush Hour'] = weekday_trips['Hour'].isin(weekday_rush_hours) # Check if hour is in rush hours
rush_hour_trips_count = weekday_trips['Is Rush Hour'].sum() # Count rush hour trips on weekdays

total_weekday_trips = len(weekday_trips) # Count total trips on weekdays

rush_hour_percentage = (rush_hour_trips_count / total_weekday_trips) * 100 # Calculate percentage of trips during rush hours for all weekday trips

total_trips = len(df) # Count total trips

rush_hour_percentage_all_trips = (rush_hour_trips_count / total_trips) * 100 # Calculate percentage of rush hour trips relative to all trips

print("Most Common Start Hour:", most_common_hour)
print("Most Common Day of Week:", most_common_day)
print("Number of Trips During Rush Hours on Weekdays:", rush_hour_trips_count)
print("Total Weekday Trips:", total_weekday_trips)
print(f"Percentage of Trips During Rush Hours: {rush_hour_percentage:.2f}%")
print("Total Trips (Including Weekends):", total_trips)
print(f"Percentage of Trips During Rush Hours (All Trips): {rush_hour_percentage_all_trips:.2f}%")

labels = ['Weekday Trips', 'Other Trips'] # Labels for Weekday vs Everyday pie chart
sizes = [total_weekday_trips, total_trips - total_weekday_trips] # Sizes for Weekday vs Everyday pie chart
colors = ['blue', 'orange'] # Colors for Weekday vs Everyday pie chart

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90) # Create pie chart for weekday vs everyday trips
plt.title('Proportion of Weekday Trips') # Title for pie chart
plt.show() # Show pie chart

labels2 = ['Rush Hour Trips', 'Other Trips'] # Labels for Rush Hour vs Other Trips pie chart
sizes2 = [rush_hour_trips_count, total_trips - rush_hour_trips_count]  # Sizes for Rush Hour vs Other Trips pie chart
colors2 = ['teal', 'orange'] # Colors for Rush Hour vs Other Trips pie chart

plt2 = plt.pie(sizes2, labels=labels2, colors=colors2, autopct='%1.1f%%', startangle=90) # Create pie chart for rush hour vs other trips
plt.title('Proportion of Rush Hour Trips') # Title for pie chart
plt.show() # Show pie chart