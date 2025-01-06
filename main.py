import time
import pandas as pd
import numpy as np

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # Get user input for the city (Chicago, New York City, Washington)
    # Use a while loop to ensure that the input is valid
    while True:
        try:
            # Ask the user to input a city name (lowercased)
            city = input(
                "Please choose a city (Chicago, New York city, Washington): "
            ).lower()

            # Check if the input city is valid by comparing it with the CITY_DATA dictionary keys
            if city in CITY_DATA:
                break  # If valid, break out of the loop
            else:
                print(
                    "Invalid city. Please choose a valid city."
                )  # Prompt the user to enter again if invalid
        except:
            print(
                "You did not enter a valid option, please try again!!"
            )  # Handle any unexpected input or errors

    # Define valid month options
    months = ["all", "january", "february", "march", "april", "may", "june"]

    # Get user input for the month (all, january, february, ..., june)
    while True:
        try:
            # Ask the user to input a month name (lowercased)
            month = input(
                "Please choose a month (all, january, february, ... , june): "
            ).lower()

            # Check if the month is in the valid list of months
            if month in months:
                break  # If valid, break out of the loop
            else:
                print(
                    "Invalid month. Please choose a valid month."
                )  # Prompt the user to enter again if invalid
        except:
            print(
                "You did not enter a valid option, please try again!!"
            )  # Handle any unexpected input or errors

    # Define valid days of the week options
    days = [
        "all",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    # Get user input for the day of the week (all, monday, tuesday, ..., sunday)
    while True:
        try:
            # Ask the user to input a day of the week (lowercased)
            day = input(
                "Please choose a day of the week (all, monday, tuesday, ... sunday): "
            ).lower()

            # Check if the day is valid by comparing it with the predefined days list
            if day in days:
                break  # If valid, break out of the loop
            else:
                print(
                    "Invalid day. Please choose a valid day."
                )  # Prompt the user to enter again if invalid
        except:
            print(
                "You did not enter a valid option, please try again!!"
            )  # Handle any unexpected input or errors

    print("-" * 100)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()

    # filter by month if applicable
    if month != "all":
        # use the index of the months list to get the corresponding int
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df["month"] == month]

    # filter by day of week if applicable
    if day != "all":
        # filter by day of week to create the new dataframe
        print(day, df["day_of_week"].dtypes)
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # Display the most common month
    # Extracts the month from the 'Start Time' column and calculates the mode (most frequent value)
    common_month = df["Start Time"].dt.month.mode()[0]
    print(f"Most Common Month: {common_month}")

    # Display the most common day of the week
    # Extracts the day of the week from the 'Start Time' column and calculates the mode
    common_day = df["Start Time"].dt.day_name().mode()[0]
    print(f"Most Common Day of Week: {common_day}")

    # Display the most common start hour
    # Extracts the hour from the 'Start Time' column and calculates the mode
    common_start_hour = df["Start Time"].dt.hour.mode()[0]
    print(f"Most Common Start Hour: {common_start_hour}")

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 100)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # Display most commonly used start station
    # The mode function returns the most frequent value in the column, [0] is used to access the first element if there are multiple modes.
    common_start_station = df["Start Station"].mode()[0]
    print(f"Most Common Start Station: {common_start_station}")

    # Display most commonly used end station
    # Similar to the start station, the mode function calculates the most frequent end station
    common_end_station = df["End Station"].mode()[0]
    print(
        f"Most Common End Station: {common_end_station}"
    )  # Print the most common end station

    # Display most frequent combination of start station and end station trip
    # Concatenate the values of "Start Station" and "End Station" with " -> " in between and calculate the mode
    common_station_combination = (
        df["Start Station"] + " -> " + df["End Station"]
    ).mode()[0]
    print(f"Most Common Combination: {common_station_combination}")

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time
    total_seconds = df["Trip Duration"].sum()
    # Convert to days, hours, minutes, seconds
    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    print(
        f"Total Travel Time: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    )

    # display mean travel time
    mean_seconds = df["Trip Duration"].mean()
    minutes = int(mean_seconds // 60)  # Get the number of whole minutes
    seconds = int(mean_seconds % 60)  # Get the remaining seconds
    print(f"Average Trip duration: {minutes} minutes and {seconds} seconds")

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 100)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types
    # Count occurrences of each user type
    user_types_count = df["User Type"].value_counts()

    for type, count in user_types_count.items():
        print(f"{type} : {count}")

    # Display counts of gender, only if the city is not Washington since it does not contian gender data.
    if city != "washington":
        gender_count = df["Gender"].value_counts()  # Count occurrences of each gender
        for gender, count in gender_count.items():
            print(f"{gender} : {count}")

        # Display earliest, most recent, and most common year of birth
        earliest_birth = df["Birth Year"].min()
        recent_birth = df["Birth Year"].max()
        common_year = df["Birth Year"].mode()[0]
        print(f"Earliest birth year: {earliest_birth}")
        print(f"Most recent birth year: {recent_birth}")
        print(f"Most common birth year: {common_year}")

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 80)


def raw_data(df):
    """
    Displays 5 records of raw data contain in a data frame. The function continues stops when the user input to stop or the data is fully displayed.

    Args:
        df - Pandas DataFrame containing the data.

    Returns:
        None
    """

    try:
        # Prompt the user to decide whether to display raw data
        display = input(
            "\nEnter 'yes' if you want to see the raw data, otherwise will be considered as 'no': "
        )
        if display.lower() != "yes":
            return  # Exit the function if user doesn't want to display raw data
    except:
        # In case of an error (like user interruption), simply exit the function
        return

    # Calculate the maximum width for each column dynamically
    column_widths = {
        col: max(
            len(str(col)), df[col].astype(str).str.len().max()
        )  # Determine max width per column
        for col in df.columns  # Iterate over each column in the DataFrame
    }

    # Dynamically generate the format string for the header and rows
    format_string = " | ".join(f"{{:<{column_widths[col]}}}" for col in df.columns)

    # Print the header row with the correct formatting
    print("\n")
    print(
        format_string.format(*df.columns)
    )  # Use the format string to print column names

    # Print a separator line with the same length as the formatted columns
    separator = "-" * (
        sum(column_widths.values()) + 3 * (len(column_widths) - 1)
    )  # Total separator length
    print(separator)

    # Display rows in chunks of 5
    for i in range(0, len(df.values), 5):
        for j in range(
            i, min(i + 5, len(df.values))
        ):  # Ensure we don't exceed the DataFrame length
            # Format and print each row using the dynamically generated format string
            print(format_string.format(*df.iloc[j].astype(str).values))

        # Prompt the user to continue or stop after every 5 records
        try:
            display = input("\nEnter 'yes' to see more, any other key to stop: ")
            if (
                display.lower() != "yes"
            ):  # If user doesn't enter 'yes', stop showing data
                break
        except:
            break  # Exit if there's an error or interruption during input

        print()  # Print an empty line between data chunks


def main():
    while True:
        # Prompt the user to specify the city, month, and day they want to analyze.
        city, month, day = get_filters()

        # Load the data based on the city, month, and day selected.
        df = load_data(city, month, day)

        # Display statistics on the most frequent times of travel.
        time_stats(df)

        # Display statistics on the most popular stations and trip combinations.
        station_stats(df)

        # Display statistics on the trip durations.
        trip_duration_stats(df)

        # Display statistics on the bikeshare users, including counts by user type and gender.
        user_stats(df, city)

        # Optionally display raw data for the user to view.
        raw_data(df)

        # Ask the user if they want to restart the analysis.
        restart = input("\nWould you like to restart? Enter yes or no.\n")
        # If the user enters 'yes', the loop continues; otherwise, the program stops.
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()
