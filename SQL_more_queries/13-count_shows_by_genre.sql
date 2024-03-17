-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_show.name AS genre
COUNT (*) AS number_of_shows
FROM hbtn_0d_tvshows
GROUP BY genre;
