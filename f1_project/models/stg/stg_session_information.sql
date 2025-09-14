with source as (
    select * from {{source('main_src', 'SESSION')}}
)
select *
from source