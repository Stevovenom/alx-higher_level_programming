-- script that lists all genres in the database hbtn_0d_tvshows_rate by ratings
SELECT tv_genres.name, SUM(rating) AS rating_sum
FROM tv_genres
JOIN tv_shows_genres ON tv_genres.id = tv_shows_genres.genre_id
JOIN tv_shows ON tv_shows_genres.show_id = tv_shows.id
JOIN ratings ON tv_shows.id = ratings.tv_show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
