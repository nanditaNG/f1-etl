with drivers as (
    select *
    from {{ref('stg_drivers')}}
) 
, race as (
    select *
    from {{ref('stg_race')}}
)
select *
from race r
left join drivers d
on r.driver_number = d.driver_number
and r.session_key = d.session_key