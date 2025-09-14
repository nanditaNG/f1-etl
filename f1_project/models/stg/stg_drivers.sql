with source as (
    select *
    from {{ source('main_src', 'DRIVERS') }}
)

select
      session_key
    , driver_number
    , upper(full_name)        as driver_name
    , broadcast_name
    , name_acronym
    , team_name
    , team_colour
    , first_name
    , last_name
    , country_code
    , meeting_key
from source
where upper(driver_name) in (
    'MAX VERSTAPPEN',
    'SERGIO PEREZ',
    'CHARLES LECLERC',
    'CARLOS SAINZ',
    'LEWIS HAMILTON',
    'GEORGE RUSSELL',
    'LANDO NORRIS',
    'OSCAR PIASTRI',
    'ESTEBAN OCON',
    'PIERRE GASLY',
    'FERNANDO ALONSO',
    'LANCE STROLL',
    'VALTTERI BOTTAS',
    'ZHOU GUANYU',
    'KEVIN MAGNUSSEN',
    'NICO HULKENBERG',
    'YUKI TSUNODA',
    'DANIEL RICCIARDO',
    'NYCK DE VRIES',
    'LIAM LAWSON',
    'ALEXANDER ALBON',
    'LOGAN SARGEANT',
    'KIMI ANTONELLI',
    'ISACK HADJAR',
    'OLIVER BEARMAN',
    'FRANCO COLAPINTO',
    'JACK DOOHAN',
    'GABRIEL BORTOLETO'
)
group by all