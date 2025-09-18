from extract.f1_wrapper import f1
import json
import pandas as pd


def sessions():
    session_keys = []

    f1_wrapper = f1()

    # responses = f1_wrapper.get_session('Race', 2025)
    responses = f1_wrapper.get_session()
    # print(responses)
    # return
    headers = ["CIRCUIT_KEY", "CIRCUIT_SHORT_NAME","COUNTRY_CODE", "COUNTRY_KEY","COUNTRY_NAME","DATE_END", "DATE_START","GMT_OFFSET","LOCATION","MEETING_KEY","SESSION_KEY","SESSION_NAME","SESSION_TYPE","YEAR"]
    df = pd.DataFrame(columns=headers)
    for response in responses:
        # session_key = response['session_key']
        # session_keys.append(session_key)
        # print(response)
        # if not isinstance(response, dict):
        #     response = json.loads(response)
        # else:
        #     continue
        rec = {
            'MEETING_KEY': response.get('meeting_key'),
            'SESSION_KEY': response.get('session_key'),
            'LOCATION': response.get('location') ,
            'DATE_START': response.get('date_start'),
            'DATE_END': response.get('date_end'),
            'SESSION_TYPE': response.get('session_type') ,
            'SESSION_NAME': response.get('session_name'),
            'COUNTRY_KEY': response.get('country_key'),
            'COUNTRY_CODE': response.get('country_code'),
            'COUNTRY_NAME': response.get('country_name'),
            'CIRCUIT_KEY': response.get('circuit_key'),
            'CIRCUIT_SHORT_NAME': response.get('circuit_short_name'),
            'YEAR': response.get('year')
        }
        # print(rec)
        df = pd.concat([df, pd.DataFrame([rec])],ignore_index=False)
    # df = pd.DataFrame(session_keys, columns=headers)
    # print(df.head())
    return df
# sessions()

def session_details():
    f1_wrapper = f1()
    session = sessions()
    session_keys = session['SESSION_KEY']
    headers = ["POSITION", "DRIVER_NUMBER","NUMBER_OF_LAPS","POINTS", "DNF","DNS","DSQ","DURATION","GAP_TO_LEADER", "MEETING_KEY", "SESSION_KEY"]
    df_session_information = pd.DataFrame(columns=headers)
    for session_key in session_keys:
        session_details = f1_wrapper.get_session_details(session_key=session_key)
        for s in session_details:
            if not isinstance(s, dict):
                try:
                    s = json.loads(s)
                except Exception:
                    continue
            rec = {
                "POSITION": s.get('position'),
                "DRIVER_NUMBER": s.get("driver_number"),
                "NUMBER_OF_LAPS": s.get("number_of_laps"),
                "POINTS": s.get("points"),
                "DNF": s.get("dnf"),
                "DNS": s.get("dns"),
                "DSQ": s.get("dsq"),
                "DURATION": s.get("duration"),
                "GAP_TO_LEADER": s.get("gap_to_leader"),
                "MEETING_KEY": s.get("meeting_key"),
                "SESSION_KEY": s.get("session_key")
            } 
            df_session_information = pd.concat([df_session_information, pd.DataFrame([rec])], ignore_index=True)
    return df_session_information
