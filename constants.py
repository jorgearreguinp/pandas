# INPUT DATA
CSV_PATH = 'input/imdb-videogames.csv'

HEADS = ["id", "name", "url", "year", "certificate", "rating",
         "votes", "plot", "Action", "Adventure", "Comedy",
         "Crime", "Family", "Fantasy", "Mystery", "Sci-Fi",
         "Thriller"]

HEADERS = ["id", "name", "year", "rating", "votes",
           "Action", "Adventure", "Comedy", "Crime",
           "Family", "Fantasy", "Mystery", "Sci-Fi",
           "Thriller"]

# COLUMNS
RATING_COLUMN = "rating"
YEAR_COLUMN = "year"
NAME_COLUMN = "name"
VOTES_COLUMN = "votes"
DROP_COLUMNS = ["url", "certificate", "plot"]

# DATA TYPES
INT_TYPE = "int"
DOUBLE_TYPE = "float"

# SOULS GAMES
SOULS_GAMES = ["Demon’s Souls", "Dark Souls", "Dark Souls II",
               "Dark Souls II: Scholar of the First Sin", "Bloodborne ",
               "Dark Souls III", "Sekiro: Shadows Die Twice",
               "Demon’s Souls Remake", "Elden Ring"]

# GTA GAMES
GTA_COLUMNS = ["name", "year", "rating"]
GTA_TITLE = "Grand Theft Auto"

# FANTASY GAMES
FANTASY_COLUMNS = ["name", "year", "rating", "votes", "Fantasy"]

# MY TOP 5
FAVORITE_GAMES = ["Halo: Combat Evolved",
                  "Elden Ring",
                  "The Last of Us",
                  "Cyberpunk 2077",
                  "Grand Theft Auto: San Andreas"]

DROP_TOP5_COLUMNS = ["url", "certificate", "votes", "Action", "Adventure", "Comedy",
                     "Crime", "Family", "Fantasy", "Mystery", "SciFi", "Thriller"]

TOP5_COLUMNS = ["name", "year", "rating", "plot"]

# FILE TYPE
PARQUET = "parquet"
CSV = "csv"
