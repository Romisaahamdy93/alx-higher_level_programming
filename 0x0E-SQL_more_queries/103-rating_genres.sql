-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name, SUM(rating.rate) as rating_sum
FROM tv_genres
LEFT JOIN show_genres ON tv_genres.id = show_genres.genre_id
LEFT JOIN tv_shows ON show_genres.show_id = tv_shows.id
LEFT JOIN rating ON tv_shows.id = rating.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC, tv_genres.name ASC;
