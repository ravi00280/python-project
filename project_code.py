

# ============================================================
# PROJECT 14: AIRLINE FLIGHT DELAY & ON-TIME PERFORMANCE
# Technologies: Python, Pandas, NumPy
# ============================================================

import pandas as pd
import numpy as np
import os

# ------------------------------------------------------------
# STEP 1: LOAD AND INSPECT DATASET
# ------------------------------------------------------------

print("\n========== STEP 1: LOAD DATASET ==========")

file_name = "data/raw/14_flight_delays.csv"

df = pd.read_csv(file_name)

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)


# ------------------------------------------------------------
# STEP 2: CHECK MISSING VALUES AND DUPLICATES
# ------------------------------------------------------------

print("\n========== STEP 2: DATA CLEANING ==========")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Flight_ID Records:")
print(df["Flight_ID"].duplicated().sum())

# Remove duplicate flight records
df = df.drop_duplicates(subset="Flight_ID")

print("\nShape After Removing Duplicates:")
print(df.shape)


# ------------------------------------------------------------
# STEP 3: HANDLE MISSING ARRIVAL DELAY VALUES
# ------------------------------------------------------------

print("\n========== STEP 3: HANDLE MISSING VALUES ==========")

df["Arrival_Delay_Mins"] = pd.to_numeric(
    df["Arrival_Delay_Mins"], errors="coerce"
)

# Fill missing arrival delays with median
median_delay = df["Arrival_Delay_Mins"].median()

df["Arrival_Delay_Mins"] = (
    df["Arrival_Delay_Mins"].fillna(median_delay)
)

print("Missing Arrival Delay Values Handled.")
print("Median Used:", median_delay)


# ------------------------------------------------------------
# STEP 4: CONVERT DATE AND EXTRACT MONTH AND DAY
# ------------------------------------------------------------

print("\n========== STEP 4: DATE ANALYSIS ==========")

df["Flight_Date"] = pd.to_datetime(
    df["Flight_Date"], errors="coerce"
)

df["Month"] = df["Flight_Date"].dt.month

df["Day_of_Week"] = df["Flight_Date"].dt.day_name()

print(df[["Flight_Date", "Month", "Day_of_Week"]].head())


# ------------------------------------------------------------
# STEP 5: TOTAL FLIGHTS AND ON-TIME PERFORMANCE
# ------------------------------------------------------------

print("\n========== STEP 5: FLIGHT PERFORMANCE ==========")

total_flights = len(df)

average_departure_delay = df["Departure_Delay_Mins"].mean()

on_time_flights = (
    df["Arrival_Delay_Mins"] <= 15
).sum()

on_time_percentage = (
    on_time_flights / total_flights * 100
    if total_flights > 0 else 0
)

print("Total Flights:", total_flights)

print("Average Departure Delay:",
      round(average_departure_delay, 2), "minutes")

print("On-Time Flights:", on_time_flights)

print("On-Time Percentage:",
      round(on_time_percentage, 2), "%")


# ------------------------------------------------------------
# STEP 6: RANK ORIGIN AIRPORTS BY AVERAGE DELAY
# ------------------------------------------------------------

print("\n========== STEP 6: AIRPORT DELAY RANKING ==========")

airport_ranking = (
    df.groupby("Origin")["Departure_Delay_Mins"]
    .mean()
    .sort_values(ascending=False)
)

print(airport_ranking)


# ------------------------------------------------------------
# STEP 7: TOP 10 WORST ROUTES
# ------------------------------------------------------------

print("\n========== STEP 7: ROUTE ANALYSIS ==========")

df["Route"] = (
    df["Origin"].astype(str) + " to " +
    df["Destination"].astype(str)
)

worst_routes = (
    df.groupby("Route")["Arrival_Delay_Mins"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("Top 10 Routes With Highest Arrival Delay:")
print(worst_routes)


# ------------------------------------------------------------
# STEP 8: DELAYS BY TIME OF DAY
# ------------------------------------------------------------

print("\n========== STEP 8: TIME OF DAY ANALYSIS ==========")

# Extract departure hour from Departure_Time
departure_time = pd.to_datetime(
    df["Departure_Time"].astype(str),
    format="mixed",
    errors="coerce"
)

df["Departure_Hour"] = departure_time.dt.hour

conditions = [
    df["Departure_Hour"].between(5, 11),
    df["Departure_Hour"].between(12, 16),
    df["Departure_Hour"].between(17, 20)
]

categories = [
    "Morning",
    "Afternoon",
    "Evening"
]

df["Time_of_Day"] = np.select(
    conditions,
    categories,
    default="Night"
)

time_analysis = (
    df.groupby("Time_of_Day")["Departure_Delay_Mins"]
    .mean()
    .sort_values(ascending=False)
)

print(time_analysis)


# ------------------------------------------------------------
# STEP 9: ANALYZE DELAY CAUSES
# ------------------------------------------------------------

print("\n========== STEP 9: DELAY CAUSES ==========")

if "Delay_Cause" in df.columns:

    delay_causes = df["Delay_Cause"].value_counts()

    print(delay_causes)

else:
    print("Delay_Cause column not available.")


# ------------------------------------------------------------
# STEP 10: CANCELLATION AND DIVERSION PERCENTAGES
# ------------------------------------------------------------

print("\n========== STEP 10: CANCELLATION ANALYSIS ==========")

def calculate_percentage(series, value):
    return (
        series.astype(str).str.strip().str.lower()
        .eq(value.lower()).mean() * 100
    )

cancel_column = "Cancelled"
divert_column = "Diverted"

if cancel_column in df.columns:

    cancellation = df.groupby("Airline")[cancel_column].apply(
        lambda x: calculate_percentage(x, "Yes")
    )

    print("\nCancellation Percentage:")
    print(cancellation)

else:
    print("Cancelled column not available.")

if divert_column in df.columns:

    diversion = df.groupby("Airline")[divert_column].apply(
        lambda x: calculate_percentage(x, "Yes")
    )

    print("\nDiversion Percentage:")
    print(diversion)

else:
    print("Diverted column not available.")


# ------------------------------------------------------------
# STEP 11: CORRELATION BETWEEN DEPARTURE AND ARRIVAL DELAYS
# ------------------------------------------------------------

print("\n========== STEP 11: CORRELATION ANALYSIS ==========")

df["Departure_Delay_Mins"] = pd.to_numeric(
    df["Departure_Delay_Mins"], errors="coerce"
)

correlation = df[
    ["Departure_Delay_Mins", "Arrival_Delay_Mins"]
].corr().iloc[0, 1]

print("Correlation:", round(correlation, 2))

if pd.notna(correlation):

    if correlation > 0:
        print("Positive relationship between departure and arrival delays.")

    elif correlation < 0:
        print("Negative relationship between departure and arrival delays.")

    else:
        print("No linear relationship found.")


# ------------------------------------------------------------
# STEP 12: NUMPY STATISTICS
# ------------------------------------------------------------

print("\n========== STEP 12: NUMPY STATISTICS ==========")

departure_delays = df["Departure_Delay_Mins"].dropna().to_numpy()

if len(departure_delays) > 0:

    median_delay = np.median(departure_delays)

    standard_deviation = np.std(departure_delays)

    percentile_90 = np.percentile(departure_delays, 90)

    print("Median Delay:", round(median_delay, 2))

    print("Standard Deviation:",
          round(standard_deviation, 2))

    print("90th Percentile:", round(percentile_90, 2))

else:
    print("No valid departure delay data available.")


# ------------------------------------------------------------
# STEP 13: IDENTIFY EXTREME DELAY OUTLIERS USING IQR
# ------------------------------------------------------------

print("\n========== STEP 13: OUTLIER DETECTION ==========")

if len(departure_delays) > 0:

    Q1 = np.percentile(departure_delays, 25)

    Q3 = np.percentile(departure_delays, 75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR

    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df["Departure_Delay_Mins"] < lower_limit) |
        (df["Departure_Delay_Mins"] > upper_limit)
    ]

    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)

    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)

    print("\nExtreme Delay Outliers:")
    print(outliers.head(10))

    print("\nTotal Outliers:", len(outliers))


# ------------------------------------------------------------
# STEP 14: CREATE DELAY SEVERITY CATEGORY
# ------------------------------------------------------------

print("\n========== STEP 14: DELAY SEVERITY ==========")

conditions = [
    df["Departure_Delay_Mins"] <= 15,
    df["Departure_Delay_Mins"].between(16, 60),
    df["Departure_Delay_Mins"].between(61, 180),
    df["Departure_Delay_Mins"] > 180
]

labels = [
    "On Time",
    "Minor Delay",
    "Major Delay",
    "Severe Delay"
]

df["Delay_Severity"] = np.select(
    conditions,
    labels,
    default="Unknown"
)

print("\nDelay Severity Count:")
print(df["Delay_Severity"].value_counts())


# ------------------------------------------------------------
# STEP 15: OPERATIONAL RECOMMENDATIONS
# ------------------------------------------------------------

print("\n========== STEP 15: RECOMMENDATIONS ==========")

print("\n1. Airports with higher average departure delays")
print("   should review ground operations and turnaround time.")

print("\n2. Airlines should monitor routes with high arrival delays")
print("   and improve schedule planning.")

print("\n3. Airlines should study peak delay periods")
print("   and allocate staff accordingly.")

print("\n4. Weather, carrier and air traffic delay causes")
print("   should be monitored to reduce disruptions.")

print("\n5. Flights with severe delays should receive")
print("   priority operational attention.")


# ------------------------------------------------------------
# SAVE CLEANED DATASET AND OUTPUT TABLES
# ------------------------------------------------------------

print("\n========== SAVE PROJECT OUTPUTS ==========")

os.makedirs("output", exist_ok=True)

df.to_csv(
    "output/cleaned_flight_data.csv",
    index=False
)

airport_ranking.to_csv(
    "output/airport_delay_ranking.csv"
)

worst_routes.to_csv(
    "output/worst_10_routes.csv"
)

time_analysis.to_csv(
    "output/time_of_day_analysis.csv"
)

print("\nProject Analysis Completed Successfully!")

print("All output files saved in the output folder.")

# ============================================================
# END OF PROJECT 14
# ============================================================
