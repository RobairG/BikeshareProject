import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        city = input('Please choose Chicago, New York City or Washington : ').title()
        if city in ['Chicago', 'Washington', 'New York City']:
            break
        else:
            print('Pleas enter a valid city')

	# TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please choose a month from January to June (type \'all\' to choose all months) : ').title()
        if month in ['All','January', 'February', 'March', 'April', 'May','June']:
            break
        else:
            print('Pleas enter a valid month !')

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please choose a weekday (type \'all\' to choose all weekdays) : ').title()
        if day in ['All', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
            break
        else:
            print('Pleas enter a valid weekday !')

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month=df['month'].mode()[0]
    print('\n The most common month is : {}'.format(common_month))
    # display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print('\n The most common day of the weekday is : {}'.format(common_day.title()))

    # display the most common start hour
    common_hour=df['Start Time'].dt.hour.mode()[0]
    print('\n The most common start hour is {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print('\n The most common start station is : {} '.format(common_start_station))
    # display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print('\n The most common end station is : {} '.format(common_end_station))

    # display most frequent combination of start station and end station trip
    df['common_combination']='From '+df['Start Station']+" to " + df['End Station']
    print('\n The most common start-end station combination is : {} '.format(df['common_combination'].mode()[0]))


    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total travel time is {} minutes'.format(str(total_travel_time)))
    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The mean travel time is {} minutes'.format(str(mean_travel_time)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        
        gender_counts=df['Gender'].value_counts()
        print(gender_counts)
    # Display earliest, most recent, and most common year of birth
    if 'Birtth Year' in df.columns:
        earliest_yob=df['Birth Year'].min()
        recent_yob=df['Birth Year'].max()
        common_yob=df["Birth Year"].mode()[0]
        print('\n The earliest birth year is {}'.format(str(int(earliest_yob))))
        print('\n The most recent birth year is {}'.format(str(int(recent_yob))))
        print('\n The most common birth year is {}'.format(str(int(common_yob))))
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data == 'yes' and start_loc+5 <= len(df):
        print(df.iloc[start_loc:start_loc +5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
