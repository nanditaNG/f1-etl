from .f1_wrapper import f1
from . import sessions
import pandas as pd
import json

def get_race():
    session_keys = []
    race_details = []

    f1_wrapper = f1()

    session = sessions.sessions()
    session_keys = session['SESSION_KEY']
    print(session_keys)
    header_names = ["MEETING_KEY", "SESSION_KEY", "DATE",
                    "DRIVER_NUMBER", "LAP_NUMBER", "CATEGORY", "FLAG", "SCOPE",
                    "SECTOR", "MESSAGE"]
    df = pd.DataFrame(columns=header_names)

    # for _, row in session_keys.iterrows():
    for session_key in session_keys:
        # key = row[0]
        race = f1_wrapper.get_race_information(session_key)
        for r in race:
            if not isinstance(r, dict):
                try:
                    s = json.loads(s)
                except Exception:
                    continue
            rec = {
                "MEETING_KEY": r.get("meeting_key"),
                "SESSION_KEY": r.get("session_key"),
                "DATE": r.get("date"),
                "DRIVER_NUMBER": r.get("driver_number"),
                "LAP_NUMBER":    r.get("lap_number"),
                "CATEGORY":      r.get("category"),
                "FLAG":          r.get("flag"),
                "SCOPE":         r.get("scope"),
                "SECTOR":        r.get("sector"),
                "MESSAGE":       r.get("message"),

            }
            df = pd.concat([df, pd.DataFrame([rec])], ignore_index=True)
            # print(df.head())
    return df

# get_race()