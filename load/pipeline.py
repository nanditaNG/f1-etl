import duckdb
import extract as fn
import config

def get_data():
    driver_df = fn.drivers.get_driver_details()
    race_df = fn.race.get_race()
    session_df = fn.sessions.sessions()
    session_information_df = fn.sessions.session_details()
    weather_df = fn.weather.weather()
    return {
        "DRIVERS": driver_df
        , "RACE": race_df
        , "SESSION": session_df
        , "SESSION_INFORMATION": session_information_df
        , "WEATHER": weather_df
    }

def load_to_duckdb(dfs: dict):
    # con = duckdb.connect(config.LOCAL_DB)
    con = duckdb.connect("md:f1")

    try:
        dfs = get_data()
        # print(f"This is the df {dfs}")
        for tablename, df in dfs.items():
            tmp = f"tmp_{tablename}"
            print(df.head())
            con.register(tmp, df)
            con.execute(f"CREATE OR REPLACE TABLE {tablename} AS SELECT * FROM {tmp}")
            con.unregister(tmp)
        print("These are the tables")
        print(con.execute("SHOW TABLES").fetch_df())
    except Exception as e:
        print(f"load_to_motherduck failed:, {e}")
    finally:
        con.close()

# def push_to_motherduck():
#     local_con = duckdb.connect("md:f1")
#     md_con = duckdb.connect(config.LOCAL_DB)
#     tables = local_con.execute("SHOW TABLES").fetchall()
#     print(tables)
#     for (table,) in tables:
#         if table.lower().startswith(("stg_", "int_", "my")) or table in {"debug", "example"}:
#             continue
#         print(f"Copying into {table}")
#         df = local_con.execute(f"SELECT * FROM {table}").fetchdf()
#         md_con.register("temp_df", df)
#         md_con.execute(f"CREATE OR REPLACE TABLE {table} AS SELECT * FROM temp_df")
#         md_con.unregister("temp_df")
#     md_con.close()

def main():
    dfs = get_data()
    load_to_duckdb(dfs)
    # push_to_motherduck()

if __name__ == "__main__":
    main()