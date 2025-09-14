with source as (
    select * from {{source('main_src', 'RACE')}}
)

select meeting_key as meeting_key
        , session_key as session_key
        , date(date) as date
        , driver_number as driver_number
        , lap_number as lap_number
        , category as category
        , flag as flag
        , sector as sectore
        , message as messages
from source