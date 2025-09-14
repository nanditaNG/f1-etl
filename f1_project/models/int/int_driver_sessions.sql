with session_information as (
select *
from {{ ref('stg_session') }}
) 
, session as (
    select *
    from {{ ref('stg_session_information')}}
)
, drivers as (
    select *
    from {{ ref('stg_drivers')}}
)

select *
from session_information si

left join session s 
on si.session_key = s.session_key
and s.session_type = 'Race'

left join drivers dr
on si.driver_number = dr.driver_number
and si.session_key = dr.session_key
