# PROJECT 14: AIRLINE FLIGHT DELAY & ON-TIME PERFORMANCE
# Technologies: Python, Pandas, NumPy

import pandas as pd
import numpy as np
import os

# Step 1: Load the dataset
df = pd.read_csv("data/raw/14_flight_delays.csv")
print(df.head())          # show first 5 rows
print("Shape:", df.shape)  # rows and columns

# Step 2: Check missing values and remove duplicates
print(df.isnull().sum())                         # missing values in each column
print("Duplicates:", df["Flight_ID"].duplicated().sum())
df = df.drop_duplicates(subset="Flight_ID")      # keep only one row for each flight

# Step 3: Fix delay columns and fill missing arrival delay
df["Departure_Delay_Mins"] = pd.to_numeric(df["Departure_Delay_Mins"], errors="coerce")
df["Arrival_Delay_Mins"] = pd.to_numeric(df["Arrival_Delay_Mins"], errors="coerce")
median_value = df["Arrival_Delay_Mins"].median()
df["Arrival_Delay_Mins"] = df["Arrival_Delay_Mins"].fillna(median_value)

# Step 4: Total flights and on-time performance
total_flights = len(df)
average_delay = df["Departure_Delay_Mins"].mean()
on_time_flights = (df["Arrival_Delay_Mins"] <= 15).sum()   # on time = 15 minutes or less
on_time_percent = on_time_flights / total_flights * 100
print("Total flights:", total_flights)
print("Average departure delay:", round(average_delay, 2), "minutes")
print("On-time flights:", on_time_flights)
print("On-time percentage:", round(on_time_percent, 2), "%")

# Step 5: Airports with the highest average delay
airport_ranking = df.groupby("Origin")["Departure_Delay_Mins"].mean()
airport_ranking = airport_ranking.sort_values(ascending=False)
print(airport_ranking)

# Step 6: Top 10 routes with the highest arrival delay
df["Route"] = df["Origin"].astype(str) + " to " + df["Destination"].astype(str)
route_delay = df.groupby("Route")["Arrival_Delay_Mins"].mean()
worst_routes = route_delay.sort_values(ascending=False).head(10)
print(worst_routes)

# Step 7: Delay by time of day
def get_time_of_day(hour):
    if 5 <= hour <= 11:
        return "Morning"
    elif 12 <= hour <= 16:
        return "Afternoon"
    elif 17 <= hour <= 20:
        return "Evening"
    else:
        return "Night"

time_column = pd.to_datetime(df["Departure_Time"].astype(str), format="mixed", errors="coerce")
hour = time_column.dt.hour                       # take only the hour
df["Time_of_Day"] = hour.apply(get_time_of_day)  # use our function on every row
time_delay = df.groupby("Time_of_Day")["Departure_Delay_Mins"].mean()
time_analysis = time_delay.sort_values(ascending=False)
print(time_analysis)

# Step 8: Delay causes
if "Delay_Cause" in df.columns:
    print(df["Delay_Cause"].value_counts())

# Step 9: Cancelled and diverted flights (percentage for each airline)
for col in ["Cancelled", "Diverted"]:
    if col in df.columns:
        text = df[col].astype(str)
        text = text.str.strip()
        text = text.str.lower()
        is_yes = text == "yes"                      # True when the value is yes
        percent = is_yes.groupby(df["Airline"]).mean() * 100
        print(col, "percentage:")
        print(percent)

# Step 10: Relation between departure delay and arrival delay
correlation = df["Departure_Delay_Mins"].corr(df["Arrival_Delay_Mins"])
print("Correlation:", round(correlation, 2))

# Step 11: Basic statistics using NumPy
delays = df["Departure_Delay_Mins"].dropna().to_numpy()
print("Median:", np.median(delays))
print("Standard deviation:", round(np.std(delays), 2))
print("90th percentile:", np.percentile(delays, 90))

# Step 12: Find extreme delays (outliers) using IQR
Q1 = np.percentile(delays, 25)
Q3 = np.percentile(delays, 75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
too_low = df["Departure_Delay_Mins"] < lower_limit
too_high = df["Departure_Delay_Mins"] > upper_limit
outliers = df[too_low | too_high]
print("Lower limit:", lower_limit, "Upper limit:", upper_limit)
print("Total outliers:", len(outliers))

# Step 13: Delay severity
def get_severity(delay):
    if pd.isnull(delay):
        return "Unknown"
    elif delay <= 15:
        return "On Time"
    elif delay <= 60:
        return "Minor Delay"
    elif delay <= 180:
        return "Major Delay"
    else:
        return "Severe Delay"

df["Delay_Severity"] = df["Departure_Delay_Mins"].apply(get_severity)
print(df["Delay_Severity"].value_counts())

# Step 14: Recommendations
print("1. Airports with high delay should improve ground operations.")
print("2. Airlines should watch routes with high arrival delay.")
print("3. Airlines should keep more staff at peak delay times.")
print("4. Weather, carrier and air traffic causes should be monitored.")
print("5. Severely delayed flights should get priority attention.")

# Step 15: Save output files
os.makedirs("output", exist_ok=True)     # make output folder if it is not there
df.to_csv("output/cleaned_flight_data.csv", index=False)
airport_ranking.to_csv("output/airport_delay_ranking.csv")
worst_routes.to_csv("output/worst_10_routes.csv")
time_analysis.to_csv("output/time_of_day_analysis.csv")
print("Project completed! Files saved in the output folder.")

# GitHub repository: https://github.com/ravi00280/python-project
# Name: Ravi Kumar Mishra
# Adm no: 2026B15410305
# B.Tech CSE DS-2
# Email id: ravi.26b15410305@abes.ac.in
