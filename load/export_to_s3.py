import duckdb
import pandas as pd
import extract as fn
from utils import functions as func
from utils import models as md
from utils.models import settings, Settings
import config as config
import os

EXPORT_DIR = os.getenv("EXPORT_DIR", "/tmp")

def main():
    os.makedirs(EXPORT_DIR, exist_ok= True)
    con = duckdb.connect("md:f1")

    try:
        drivers_csv = os.path.join(EXPORT_DIR, "drivers.csv")
        race_csv = os.path.join(EXPORT_DIR, "race.csv")
        sessions_csv = os.path.join(EXPORT_DIR, "sessions.csv")
        session_information_csv = os.path.join(EXPORT_DIR, "session_information.csv")
        weather_csv = os.path.join(EXPORT_DIR, "weather.csv")

        con.execute(f"COPY (SELECT * FROM DRIVERS) TO '{drivers_csv}' (HEADER, DELIMITER ',');")
        con.execute(f"COPY (SELECT * FROM RACE) TO '{race_csv}' (HEADER, DELIMITER ',');")
        con.execute(f"COPY (SELECT * FROM SESSION) TO '{sessions_csv}' (HEADER, DELIMITER ',');")
        con.execute(f"COPY (SELECT * FROM SESSION_INFORMATION) TO '{session_information_csv}' (HEADER, DELIMITER ',');")
        con.execute(f"COPY (SELECT * FROM WEATHER) TO '{weather_csv}' (HEADER, DELIMITER ',');")

        # Upload to S3
        func.write_to_s3(drivers_csv, Settings.bucket_name, "f1/drivers.csv")
        func.write_to_s3(race_csv, Settings.bucket_name, "f1/race.csv")
        func.write_to_s3(sessions_csv, Settings.bucket_name, "f1/sessions.csv")
        func.write_to_s3(session_information_csv, Settings.bucket_name, "f1/session_information.csv")
        func.write_to_s3(weather_csv, Settings.bucket_name, "f1/weather.csv")
    finally:
        con.close()

if __name__ == "__main__":
    main()
