-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title, SUM(rating.rate) as rating_sum
FROM tv_shows
LEFT JOIN rating ON tv_shows.id = rating.show_id
GROUP BY tv_shows.id
ORDER BY rating_sum DESC, tv_shows.title ASC;
