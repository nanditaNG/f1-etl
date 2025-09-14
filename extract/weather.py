from extract.f1_wrapper import f1
import extract.sessions as sessions
import pandas as pd
import json

def weather():
        f1_wrapper = f1()
        session_keys = []
        weather_data = []
        # session_keys = sessions.sessions()
        session = sessions.sessions()
        session_keys = session['SESSION_KEY']
        headers = ["DATE","SESSION_KEY","WIND_DIRECTION","HUMIDITY","AIR_TEMPERATURE","PRESSURE","TRACK_TEMPERATURE","WIND_SPEED","RAINFALL","MEETING_KEY"]
        df =pd.DataFrame(columns=headers)
        # for _, row in session_keys.iterrows():
        for session_key in session_keys:
        #     key = row[0]
            weather = f1_wrapper.get_weather(session_key)
            for w in weather:
                try:
                        if not isinstance(w, dict):
                                w = json.loads(w)
                except Exception:
                        continue
                        
                rec = {
                     "DATE": w.get('date'),
                     "SESSION_KEY": w.get('session_key'),
                     "WIND_DIRECTION": w.get('wind_direction'),
                     "HUMIDITY": w.get('humidity'),
                     "AIR_TEMPERATURE": w.get('air_temperature'),
                     "PRESSURE": w.get('pressure'),
                     "TRACK_TEMPERATURE": w.get('track_temperature'),
                     "WIND_SPEED": w.get('wind_speed'),
                     "RAINFALL": w.get('rainfall'),
                     "MEETING_KEY": w.get('meeting_key')
                }

                df = pd.concat([df, pd.DataFrame([rec])], ignore_index=True)
        return df