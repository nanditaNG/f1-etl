with source as (
    select * from {{source('main_src', 'WEATHER')}}
)

select date(date) as date
        , session_key as session_key
        , wind_direction as wind_direction
        , humidity as humidity
        , air_temperature as air_temperature
        , pressure as pressure
        , track_temperature as track_temperature
        , wind_speed as wind_speed
        , rainfall as rainfall
        , meeting_key as meeting_key
from source