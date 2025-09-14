from extract.f1_wrapper import f1
import json
import pandas as pd

f1_wrapper = f1()
all_driver_names = []
filename = "drivers.csv"
headers = ["MEETING_KEY","SESSION_KEY","DRIVER_NUMBER",
           "BROADCAST_NAME","FULL_NAME","NAME_ACRONYM",
           "TEAM_NAME","TEAM_COLOUR","FIRST_NAME",
           "LAST_NAME", "COUNTRY_CODE"]
def get_driver_details():
    drivers = f1_wrapper.get_drivers()
    for driver in drivers:
        meeting_key = driver['meeting_key']
        session_key = driver['session_key']
        driver_name = driver['full_name']
        driver_number = driver['driver_number']
        full_name = driver['full_name']
        team_name = driver['team_name']
        country_code = driver['country_code']
        broadcast_name = driver['broadcast_name']
        name_acronym = driver['name_acronym']
        team_color = driver['team_colour']
        first_name = driver['first_name']
        last_name = driver['last_name']
        all_driver_names.append({"DRIVER_NUMBER": driver_number
                                 ,"DRIVER_NAME": driver_name
                                 , "MEETING_KEY": meeting_key
                                 , "SESSION_KEY": meeting_key
                                 , "FULL_NAME": full_name
                                 , "FIRST_NAME": first_name
                                 , "LAST_NAME": last_name
                                 , "TEAM_NAME": team_name
                                 , "TEAM_COLOR": team_color
                                 , "COUNTRY_CODE": country_code
                                 , "BROADCAST_NAME": broadcast_name
                                 , "NAME_ACRONYM": name_acronym
                                 , "TEAM_NAME": team_name
                                 , "COUNTRY_CODE": country_code
                                 , "SESSION_KEY": session_key})
    
    df = pd.DataFrame(all_driver_names, columns=headers)
    # print(df.head())
    return df

# get_driver_details()