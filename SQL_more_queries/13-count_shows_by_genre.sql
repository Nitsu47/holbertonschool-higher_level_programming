-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genre.name AS genre
COUNT (*) AS number_of_shows
INNER JOIN genre ON tv_genre.genre_id = genre.id
GROUP BY genre.name
ORDER BY number_of_shows DESC;
