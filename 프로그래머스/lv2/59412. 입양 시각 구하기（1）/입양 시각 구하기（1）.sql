-- 코드를 입력하세요
SELECT 
    extract(hour from cast(datetime as timestamp)) as hour,
    count(animal_id) as count
    from animal_outs
    where extract(hour from cast(datetime as timestamp)) between 09 and 19
    group by extract(hour from cast(datetime as timestamp))
    order by hour