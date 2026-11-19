# Airline Flight Delay & On-Time Performance Analysis

## Project Overview
This project analyzes airline flight delay data to understand flight delays, on-time performance, cancellation rates, and delay patterns.

The project uses Python, Pandas, and NumPy to clean and analyze flight data and generate useful operational recommendations.

## Objectives
- Analyze airline flight delay data.
- Identify missing values and duplicate records.
- Calculate average departure and arrival delays.
- Find the best and worst performing airports.
- Identify routes with high arrival delays.
- Analyze delays by time of day.
- Study different causes of flight delays.
- Calculate cancellation and diversion percentages.
- Identify extreme delay outliers.
- Provide operational recommendations.

## Technologies Used
- Python
- Pandas
- NumPy

## Project Structure

```text
Airline-Flight-Delay-Project/
│
├── data/
│   ├── raw/
│   │   └── 14_flight_delays.csv
│   │
│   └── processed/
│       └── cleaned_flight_delays.csv
│
├── project_code.py
├── requirements.txt
└── README.md
```

## Dataset
The dataset contains flight information such as:
- Flight ID
- Flight Date
- Airline
- Origin Airport
- Destination Airport
- Departure Time
- Departure Delay
- Arrival Delay
- Delay Cause
- Cancellation Status
- Diversion Status

## Installation

Install the required libraries:

```bash
python3 -m pip install -r requirements.txt
```

## How to Run

Run the project using:

```bash
python3 project_code.py
```

## Analysis Performed
1. Dataset inspection
2. Missing values and duplicate identification
3. Data cleaning
4. Date conversion and extraction
5. Overall flight performance KPIs
6. Airport delay ranking
7. Top 10 delayed routes
8. Time-of-day delay analysis
9. Delay cause analysis
10. Airline cancellation and diversion analysis
11. Correlation analysis
12. NumPy statistical analysis
13. IQR outlier detection
14. Delay severity classification
15. Operational recommendations

## Output
The cleaned dataset is saved at:

`data/processed/cleaned_flight_delays.csv`

## Conclusion
This project helps understand airline flight delay patterns and on-time performance. The analysis provides useful insights that can help airlines improve scheduling, reduce delays, and enhance passenger satisfaction.

## Author
Ravi Mishra
