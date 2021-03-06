import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
  
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city_names = ["chicago","new york city","washington"]

    while True :
       
            city = input("\nplease inter the city (chicago, new york city, washington)\n").lower()
            if city in city_names :
               break
            elif city not in city_names :
               print("sorry wrong inter ! ")
 

    # TO DO: get user input for month (all, january, february, ... , june)
    
    month_names = ["all" , "january", "february", "march", "april", "may" , "june"]
    
    while True :
     
            month = input("please inter the month (all , january, february, march, april, may , june)\n ").lower()
            if month in month_names :
                break
            elif month not in month_names :
                print("sorry wrong inter ! ")
   

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day_names = ["all" , "monday", "tuesday", "wednesday", "thursday" , "friday", "saturday", "sunday"]
    
    while True :
       
            day = input("\nplease inter the Day (all , monday, tuesday, wednesday, thursday , friday, saturday, sunday )\n ").lower()
            if day in day_names :
                break
            elif day not in day_names :
                print("sorry wrong inter ! ")
            
            
    
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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print("the most common month :" ,  popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("the most common day :" ,  popular_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour :', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    commonly_stard_station = df['Start Station'].mode()[0]
    
    print('The most common start_station is: ', commonly_stard_station)

    # TO DO: display most commonly used end station
    commonly_end_station = df['End Station'].mode()[0]
    print('The most common end station is:  ', commonly_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print("most frequent combination of start station and end station trip is " ,most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].count()
    print("the total travel time is : " ,total_travel_time)
    

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("the mean travel time is : " ,mean_travel_time)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print("the counts of user type : \n " , user_types)


    # TO DO: Display counts of gender
    #exception for washington
    try :
        gender = df['Gender'].value_counts()
        print("the counts of user Gender\n" , gender)
    except:
        pass
    
    # TO DO: Display earliest, most recent, and most common year of birth
    #exception for washington
    try:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
    
        print("the earliest year of birth" , earliest)
        print("the most recent year of birth" , most_recent)
        print("the common year of birth" , most_common)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except :
        pass

def raw_data(df):
    check = ['yes','no']
    
    while True :
        answer = input("Would you like to see 5 lines of raw data? enter yes or no\n ").lower()
        if answer not in check :
            print("please inter yes or no")
        elif answer == "yes" :
            print(df.head())
        else :
            break 
         
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
