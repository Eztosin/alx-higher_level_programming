-- Import the database dump from hbtn_0d_tvshows to your
-- MySQL server: download (same as 12-no_genre.sql)
-- a script that lists all genres from hbtn_0d_tvshows and
-- displays the number of shows linked to each.
SELECT gn.'name' AS 'genre',
COUNT(*) AS 'number_of_shows' FROM 'tv_genres'
AS gn INNER JOIN 'tv_show_genres' AS t ON gn.'id' = t.'genre_id'
GROUP BY gn.'name' ORDER BY 'number_of_shows' DESC;
