import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for plots
sns.set(style="whitegrid")

# Load CSVs
jan_df = pd.read_csv("Bike share ridership 2024-01.csv")
july_df = pd.read_csv('Bike share ridership 2024-08.csv')

# Better prepare column names for reference for pandas
jan_df.columns = jan_df.columns.str.strip()
july_df.columns = july_df.columns.str.strip()

# Add month labels
jan_df["Month"] = "January"
july_df["Month"] = "July"

# Combine datasets into one cohesive dataset to perform analysis
df = pd.concat([jan_df, july_df], ignore_index=True)

# Ensure datetime and derived fields of the combined dataframe
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['Route'] = df['Start Station Name'] + ' → ' + df['End Station Name']
jan_df['Route'] = jan_df['Start Station Name'] + ' → ' + jan_df['End Station Name']
july_df['Route'] = july_df['Start Station Name'] + ' → ' + july_df['End Station Name']
df['Hour'] = df['Start Time'].dt.hour


# Top 5 routes for both January and July

for month in ['January', 'July']:
    top_routes = df[df['Month'] == month]['Route'].value_counts().head(5)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_routes.values, y=top_routes.index, palette='Blues_d')
    plt.title(f'Top 10 Bike Share Routes in {month}')
    plt.xlabel('Number of Trips')
    plt.ylabel('Route')
    plt.tight_layout()
    plt.show()


for month in ['January', 'July']:
    top_routes = df[df['Month'] == month]['Route'].value_counts().head(5)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_routes.values, y=top_routes.index, palette='Reds_d')
    plt.title(f'Top 10 Bike Share Routes in {month}')
    plt.xlabel('Number of Trips')
    plt.ylabel('Route')
    plt.tight_layout()
    plt.show()


# Get top 20 routes per month for Venn-style logic between January and July

jan_routes = set(jan_df['Route'].value_counts().head(20).index)
july_routes = set(july_df['Route'].value_counts().head(20).index)

shared_routes = jan_routes.intersection(july_routes)
jan_unique = jan_routes - july_routes
july_unique = july_routes - jan_routes

print("\n Shared Top Routes (Jan & July):")
for route in shared_routes:
    print(f"  - {route}")

print("\n Jan-Only Top Routes:")
for route in jan_unique:
    print(f"  - {route}")

print("\n July-Only Top Routes:")
for route in july_unique:
    print(f"  - {route}")
