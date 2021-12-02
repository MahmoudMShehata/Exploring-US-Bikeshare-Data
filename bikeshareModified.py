#!/usr/bin/env python
# coding: utf-8

# In[7]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    
    city = input("Please select a city (chicago, new york city or washington) :").lower()

    
    if city in CITY_DATA.keys():
        city = city 
    else:
        flag = True 
        while flag:
            city = input("Please enter a correct city name: ").lower()
            if city in CITY_DATA.keys():
                flag = False
                
    city = CITY_DATA[city]
          


    # TO DO: get user input for month (all, january, february, ... , june)

    month = input("Please select a month (all, january, february, ... , june) :").lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']

    while month not in months:
        month = input("Please enter a correct month name:").lower()
        if month in months:
            break
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please select a day (all,sunday, monday, tuesday, ...., saturday) :").lower()
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']

    while day not in days:
        day = input("Please enter a correct day name:").lower()
        if day in days:
            break    
        
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
    df = pd.read_csv('C:\\Users\\Mahmoud M. Shehata\\Downloads\\bikeshare-2\\'+city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

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

    frequent_month = df['month'].mode()
    # TO DO: display the most common day of week
    frequent_day = df['day_of_week'].mode()

    # TO DO: display the most common start hour
    frequent_hour = df['hour'].mode()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    frequent_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station

    frequent_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    
    df['Stations combinations'] = df['Start Station']+ " TO " +df['End Station']
    most_freq_combination = df['Stations combinations'].value_counts().keys().tolist()[0]
    print("\nThe most of frequent combination of start & end station is : "+most_freq_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Total travel time'] = df['End Time'] - df['Start Time']
    print("\nTotal travel time : \n" +str(df['Total travel time']))
    # TO DO: display mean travel time
    
    mean_travel_time = df['Total travel time'].mean()
    print("\nAverage travel time : \t"+str(mean_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print("\nCounts of user types : " +str(df['User Type'].value_counts()))

    # TO DO: Display counts of gender

    if 'Gender' not in df.columns:
        print("\nUsers genders are unknown")
    else:
        print("\nCounts of users genders : " +str(df['Gender'].value_counts()))    
        print("\nOldest user : "+str(int(df['Birth Year'].min()))+ " old")
        print("\nYoungest user : "+str(int(df['Birth Year'].max()))+ " old")
        print("\nMost common user year of birth: "+str(int(df['Birth Year'].value_counts().keys().tolist()[0])))
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display != 'yes':
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()


# In[ ]:




