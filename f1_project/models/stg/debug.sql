select 
table_catalog,
table_schema,
table_name
from information_schema.tables
where lower(table_name) in ('weather','session','race','drivers','session_information')
order by 1,2,3