# Airline Flight Delay and On-Time Performance Analysis

This is my Python project in which I study flight delay data. The program reads a CSV file of flights, cleans it, finds the on-time performance and shows which airports, routes and times of the day have the most delay.

## About the Project

Flights get delayed many times and it causes problems for airlines and passengers. Checking thousands of flight records by hand is slow, so I made this program to do the analysis automatically using Pandas and NumPy.

## What the Program Does

1. Loads the dataset and shows the first 5 rows and the shape
2. Checks missing values and removes duplicate flights (using `Flight_ID`)
3. Fills missing arrival delays with the median
4. Finds total flights, average departure delay and on-time percentage (on time = arrival delay of 15 minutes or less)
5. Ranks the origin airports by average departure delay
6. Finds the top 10 routes with the highest arrival delay
7. Checks delay by time of day (Morning, Afternoon, Evening, Night)
8. Counts the delay causes
9. Finds the cancelled and diverted percentage of each airline
10. Finds the correlation between departure delay and arrival delay
11. Finds median, standard deviation and 90th percentile using NumPy
12. Finds extreme delays (outliers) using the IQR method
13. Divides flights into On Time, Minor Delay, Major Delay and Severe Delay
14. Prints some recommendations to reduce delays
15. Saves the output files

## Tools Used

- Python 3
- Pandas
- NumPy

## Folder Structure

```
python-project/
|-- data/
|   |-- raw/
|       |-- 14_flight_delays.csv
|-- output/
|   |-- cleaned_flight_data.csv
|   |-- airport_delay_ranking.csv
|   |-- worst_10_routes.csv
|   |-- time_of_day_analysis.csv
|-- project_code.py
|-- README.md
```

The `output` folder is made automatically when the program runs.

## How to Run

1. Install Python 3 on your computer.
2. Install the libraries:

   ```
   pip install pandas numpy
   ```

3. Keep the dataset at `data/raw/14_flight_delays.csv`.
4. Run the program:

   ```
   python project_code.py
   ```

## Dataset Columns Used

`Flight_ID`, `Airline`, `Origin`, `Destination`, `Departure_Time`, `Departure_Delay_Mins`, `Arrival_Delay_Mins`, `Delay_Cause`, `Cancelled`, `Diverted`

`Delay_Cause`, `Cancelled` and `Diverted` are optional. If any of these columns is not in the file, that step is skipped.

## Output Files

| File | What it has |
| --- | --- |
| cleaned_flight_data.csv | Cleaned data with new columns (route, time of day, delay level) |
| airport_delay_ranking.csv | Average departure delay of each origin airport |
| worst_10_routes.csv | Top 10 routes with the highest average arrival delay |
| time_of_day_analysis.csv | Average departure delay for each time of day |

## Author

- Name: Ravi Kumar Mishra
- Admission No.: 2026B15410305
- Course: B.Tech CSE (DS-2)
- Institute: ABES Engineering College
- Email: ravi.26b15410305@abes.ac.in
- GitHub: https://github.com/ravi00280/python-project
