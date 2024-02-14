-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name, SUM(tv_shows.rating) as rating_sum
FROM tv_genres
INNER JOIN tv_genres_shows ON tv_genres.id = tv_genres_shows.genre_id
INNER JOIN tv_shows ON tv_genres_shows.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
