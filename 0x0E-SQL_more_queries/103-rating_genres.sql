-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT name, SUM(tv_shows_rating.rate) as rating
FROM tv_genres
INNER JOIN tv_genres_shows ON tv_genres.id = tv_genres_shows.genre_id
INNER JOIN tv_shows ON tv_genres_shows.show_id = tv_shows.id
GROUP BY name
ORDER BY rating DESC;
