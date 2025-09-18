from .f1_wrapper import f1
from . import sessions
import pandas as pd
import json

def get_starting_position():
    f1_wrapper = f1()
    # session = sessions.sessions()
    # session_keys = session['SESSION_KEY']
    headers=["POSITION", "DRIVER_NUMBER","LAP_DURATION","MEETING_KEY","SESSION_KEY"]
    df = pd.DataFrame(columns=headers)
    data = f1_wrapper.get_position()
    for d in data:
            rec = {
                "POSITION": d.get('position'),
                "DRIVER_NUMBER": d.get('driver_number'),
                "LAP_DURATION": d.get('lap_duration'),
                "MEETING_KEY": d.get('meeting_key'),
                "SESSION_KEY": d.get('session_key')
            }
            df = pd.concat([df, pd.DataFrame([rec])])
            # print(df)
    return df
# get_position()