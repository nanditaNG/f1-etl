with source as (
    select * from {{source('main_src', 'SESSION_INFORMATION')}}
)

select position as position
        , driver_number as driver_number
        , number_of_laps as number_of_laps
        , points as points
        , dnf as did_not_finish
        , dns as did_not_start
        , dsq as disqualified
        , duration as duration_in_seconds
        , gap_to_leader as gap_to_leader
        , meeting_key as meeting_key
        , session_key as session_key

from source