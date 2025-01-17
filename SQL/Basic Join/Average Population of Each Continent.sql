/*
This problem is a little tricky because you need to join the CITY and COUNTRY tables on the COUNTRYCODE column. Once you have done that, you can use the AVG function to calculate the average population of each continent. The FLOOR function is used to round the average population to the nearest whole number.
*/
SELECT 
    co.Continent,
    FLOOR(AVG(city.Population)) AS AverageCityPopulation
FROM CITY city
JOIN COUNTRY co
    ON city.CountryCode = co.Code
GROUP BY co.Continent
ORDER BY co.Continent;

/*
Give me the second highest population of cities in each continent and add commend to explain the query.
*/
SELECT 
    co.Continent,
    MAX(city.Population) AS SecondHighestCityPopulation
FROM CITY city
JOIN COUNTRY co
    ON city.CountryCode = co.Code
WHERE city.Population < (
    SELECT 
        MAX(city.Population)
    FROM CITY city
    JOIN COUNTRY co
        ON city.CountryCode = co.Code
    WHERE co.Continent = co.Continent
)
GROUP BY co.Continent
ORDER BY co.Continent;