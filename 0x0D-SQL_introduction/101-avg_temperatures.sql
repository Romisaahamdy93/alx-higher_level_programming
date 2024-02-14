-- displays the average temperature (Fahrenheit) by city ordered by temperature.
SELECT
    city,
    AVG(temperature) AS avg_temp
FROM
    temperature_data
GROUP BY
    city
ORDER BY
    avg_temp DESC;
