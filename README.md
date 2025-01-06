# Bike Share Data Analysis

This project is part of the **Udacity Programming for Data Science with Python Nanodegree**. The goal of this project is to explore and analyze bike share data for three major cities in the United States: Chicago, New York City, and Washington, D.C. The analysis involves computing various descriptive statistics on the dataset provided for these cities, such as travel times, popular stations, and user demographics.

## Data Description

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

5. **Raw Data**: Optionally, the user can view raw data in chunks of 5 records.
