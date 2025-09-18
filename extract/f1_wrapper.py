from urllib.request import urlopen
import json
import requests


class f1:
    def __init__(self):
        self.base_url = "https://api.openf1.org/v1"

    def get_drivers(self):
        url = f"{self.base_url}/drivers"
        response = requests.get(url)
        print(f"{url}")

        try:
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"An unexpected error occured: {e}")
        

    def get_driver_details(self, driver_number, session_key, speed):
        url = f"{self.base_url}/car_data?driver_number={driver_number}&session_key={session_key}&speed>={speed}"
        response = requests.get(url)

        if response.status_code == 404:
            print(f"Error in getting driver information")
        else:
            return response.json()

    def get_session(self):
        # url = f'{self.base_url}/sessions?session_name={session_name}&year={year}'
        url = f'{self.base_url}/sessions'
        response = requests.get(url)

        if response.status_code == 404:
            print(f"Error in retriving session information")
        else:
            return response.json()
        
    def get_session_details(self, session_key):
        url = f'{self.base_url}/session_result?session_key={session_key}'
        response = requests.get(url)
        if response.status_code == 404:
            print(f"Error in retriving session details for session {session_key}")
        else:
            return response.json()
        
    def get_race_information(self,session_key):
        url=f'{self.base_url}/race_control?session_key={session_key}'
        response = requests.get(url)
        if response.status_code == 404:
            print('Error in retriving race information')
        else:
            return response.json()

    def get_weather(self, session_key):
        url = f'{self.base_url}/weather?session_key={session_key}'
        response = requests.get(url)
        if response.status_code == 404:
            print(f"Error in fetching weather data")
        else:
            return response.json()
        
    def get_position(self):
        url = f'{self.base_url}/starting_grid'
        response = requests.get(url)
        if response.status_code == 404:
            print(f"Error fetching positions")
        else:
            return response.json()