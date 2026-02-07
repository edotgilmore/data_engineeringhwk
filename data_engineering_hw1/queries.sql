SELECT "VendorID",
lpep_pickup_datetime, 
lpep_dropoff_datetime, 
store_and_fwd_flag, 
"RatecodeID", 
"PULocationID",
tzPU."Zone" as PUZone,
tzPU."Borough" as PUBorough,
"DOLocationID", 
tzDO."Zone" as DOZone,
tzDO."Borough" as DOBorough,
passenger_count, 
trip_distance,
fare_amount,
extra, 
mta_tax, 
tip_amount, 
tolls_amount, 
ehail_fee, 
improvement_surcharge, 
total_amount, 
payment_type, 
trip_type, 
congestion_surcharge, 
cbd_congestion_fee
FROM public.green_taxi_data gtd
join taxi_zone_lookup tzPU
	on tzPU."LocationID" = gtd."PULocationID" 
join taxi_zone_lookup tzDO 
	on tzDO."LocationID" = gtd."DOLocationID" 
where gtd.trip_distance <= 1 and  lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01';

SELECT 
    COUNT(*) as trip_count,
    ROUND(AVG(trip_distance), 2) as avg_distance,
    MIN(trip_distance) as min_distance,
    MAX(trip_distance) as max_distance
FROM green_taxi_data
WHERE trip_distance <= 1
  AND lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01';


SELECT lpep_pickup_datetime::date as pickup_day,
       lpep_pickup_datetime,
       trip_distance,
       "PULocationID",
       "DOLocationID"
FROM green_taxi_data
WHERE trip_distance < 100
  AND lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
ORDER BY trip_distance DESC
LIMIT 1;

SELECT tzPU."Zone" as pickup_zone,
       COUNT(*) as trip_count,
       SUM(gtd.total_amount) as total_amount_sum,
       ROUND(AVG(gtd.total_amount), 2) as avg_amount
FROM green_taxi_data gtd
JOIN taxi_zone_lookup tzPU
    ON tzPU."LocationID" = gtd."PULocationID"
WHERE lpep_pickup_datetime >= '2025-11-18'
  AND lpep_pickup_datetime < '2025-11-19'
GROUP BY tzPU."Zone"
ORDER BY total_amount_sum DESC
LIMIT 10;

SELECT tzDO."Zone" as dropoff_zone,
       MAX(gtd.tip_amount) as max_tip
FROM green_taxi_data gtd
JOIN taxi_zone_lookup tzPU
    ON tzPU."LocationID" = gtd."PULocationID"
JOIN taxi_zone_lookup tzDO
    ON tzDO."LocationID" = gtd."DOLocationID"
WHERE tzPU."Zone" = 'East Harlem North'
  AND lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
GROUP BY tzDO."Zone"
ORDER BY max_tip DESC
LIMIT 10;