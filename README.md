# Bike Share Data Analysis

The goal of this project is to explore and analyze bike share data for three major cities in the United States: Chicago, New York City, and Washington, D.C. The analysis involves computing various descriptive statistics on the dataset provided for these cities, such as travel times, popular stations, and user demographics.

## Datasets
The dataset used for this project contains data for the first six months of 2017. The core columns in the dataset include:

- **Start Time**: The start time of the trip.
- **End Time**: The end time of the trip.
- **Trip Duration**: The duration of the trip in seconds.
- **Start Station**: The station where the trip started.
- **End Station**: The station where the trip ended.
- **User Type**: Type of user (Subscriber or Customer).

The Chicago and New York City datasets also contain the following columns:
- **Gender**: Gender of the user (only available for NYC and Chicago).
- **Birth Year**: The birth year of the user (only available for NYC and Chicago).

The data is provided by [**Motivate**](https://www.motivateco.com) and has been preprocessed by [**Udacity**](https://www.udacity.com). The original datasets can be found at:
- Chicago: [`https://divvybikes.com/system-data`](https://divvybikes.com/system-data)
- New York City: [`https://citibikenyc.com/system-data`](https://citibikenyc.com/system-data)
- Washington: [`https://capitalbikeshare.com/system-data`](https://capitalbikeshare.com/system-data)

## Functionality

This Python program provides the following functionalities:

1. **Popular Times of Travel**:
   - Most common month
   - Most common day of the week
   - Most common start hour

2. **Popular Stations and Trips**:
   - Most common start station
   - Most common end station
   - Most common trip (start to end station combination)

3. **Trip Duration**:
   - Total travel time
   - Average travel time

4. **User Information**:
   - Counts of each user type
   - Counts of each gender (only for Chicago and New York City)
   - Earliest, most recent, and most common birth year (only for Chicago and New York City)

5. **Raw Data**: Optionally, the user can view raw data in chunks of 5 records formatted as a table.

## Requirements
- Pandas is the only required package.

You can install it using `pip`:
```bash
pip install pandas
```

## **Installation Instructions**:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Bader-Almutlaq/bike-share-analysis.git
   ```
2. Download the required dataset files from the provided links:
   - Chicago: [Divvy Bikes Data](https://divvybikes.com/system-data)
   - New York City: [CitiBike Data](https://citibikenyc.com/system-data)
   - Washington D.C.: [Capital Bikeshare Data](https://capitalbikeshare.com/system-data)

3. Preprocess the data to insure it contains the same features as specified in the dataset section.
4. Place the downloaded files in the `data` folder.
5. Run the analysis script:
   ```bash
   python main.py
   ```

## Acknowledgments

- **[Udacity](https://www.udacity.com/):** For providing the preprocessed datasets and the project skeleton file (`main.py`) as part of the *Programming for Data Science with Python Nanodegree*.
- **[Motivate](https://www.motivateco.com/):** For supplying the raw bike-share data used in this analysis.
