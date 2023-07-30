# SOULS SERIES SQL QUERY

SELECT DISTINCT id, name, year, rating, votes
FROM games A
WHERE(
	(A.name IN (
		"Demon’s Souls",
		"Dark Souls",
		"Dark Souls II",
		"Dark Souls II: Scholar of the First Sin",
		"Bloodborne ",
		"Dark Souls III",
		"Sekiro: Shadows Die Twice",
		"Demon’s Souls Remake",
		"Elden Ring"))
)
GROUP BY A.name
ORDER BY A.year DESC;

# GRAND THEFT AUTO SERIES SQL QUERY

SELECT DISTINCT id, name, CAST(year AS DOUBLE) AS year, rating, votes
FROM games A
WHERE 
	A.name LIKE 'Grand Theft Auto%' AND
    A.year < YEAR(CURDATE())
GROUP BY A.name
ORDER BY A.rating DESC;

# FANTASY GAMES SQL QUERY

SELECT MIN(id) AS id, name, CAST(year AS UNSIGNED) AS year, rating, votes, Fantasy
FROM games A
WHERE
	A.Fantasy = 1 AND
    A.Adventure = 1 AND
    A.rating != ""
GROUP BY A.name
ORDER BY A.rating DESC;

# THE OLDEST GAMES

SELECT id, name, year, rating, votes, plot
FROM games
WHERE name IN (
	"Halo: Combat Evolved",
	"Elden Ring",
	"The Last of Us",
	"Cyberpunk 2077",
	"Grand Theft Auto: San Andreas"
)
GROUP BY name
ORDER BY rating DESC;
