import mysql.connector
from tabulate import tabulate

from constants import *
from write import *

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="games"
)

consulta_sql = "SELECT * FROM games"
dataframe = pandas.read_sql(consulta_sql, conexion)
df_filled_none = dataframe.applymap(lambda x: None if x == "" else x)

games = pandas.DataFrame(df_filled_none)

# Souls Series
souls = games[games.name.isin(SOULS_GAMES)] \
    .astype({YEAR_COLUMN: DOUBLE_TYPE}) \
    .astype({YEAR_COLUMN: INT_TYPE}) \
    .drop_duplicates(subset=[NAME_COLUMN]) \
    .drop(columns=DROP_COLUMNS)

print(
    tabulate(
        souls,
        HEADERS,
        tablefmt="pretty",
        stralign="left"
    )
)

# Grand Theft Auto Series
df = games[GTA_COLUMNS]

gta = df[df.name.str.contains(GTA_TITLE)] \
    .sort_values(by=RATING_COLUMN, ascending=False) \
    .astype({YEAR_COLUMN: DOUBLE_TYPE}) \
    .astype({YEAR_COLUMN: INT_TYPE}) \
    .drop_duplicates(subset=[NAME_COLUMN]) \
    .head(5)

print(
    tabulate(
        gta,
        headers=GTA_COLUMNS,
        tablefmt="pretty",
        stralign="left"
    )
)

# Fantasy Games
fantasy = games[
    (games.Fantasy == "1") &
    (games.Adventure == "1") &
    (games.rating is not None)
    ] \
    .astype({YEAR_COLUMN: DOUBLE_TYPE})

fant = fantasy[FANTASY_COLUMNS] \
    .sort_values(by=[RATING_COLUMN, VOTES_COLUMN], ascending=False) \
    .drop_duplicates(subset=[NAME_COLUMN]) \
    .head(5)

print(
    tabulate(
        fant,
        headers=FANTASY_COLUMNS,
        tablefmt="pretty",
        stralign="left"
    )
)

# The Oldest Games
old_year = games.year.astype({YEAR_COLUMN: DOUBLE_TYPE}).min()

oldest = games[games.year.astype({YEAR_COLUMN: DOUBLE_TYPE}) == old_year] \
    .astype({YEAR_COLUMN: DOUBLE_TYPE}) \
    .astype({YEAR_COLUMN: INT_TYPE}) \
    .drop(columns=DROP_COLUMNS)

print(
    tabulate(
        oldest,
        HEADERS,
        tablefmt="pretty",
        stralign="left"
    )
)

# The Newest Games
not_nulls = games[
    (games.rating.isna()) &
    (games.votes.isna())
    ]

max_year = not_nulls.year.astype({YEAR_COLUMN: DOUBLE_TYPE}).max()

oldest = not_nulls[not_nulls.year.astype({YEAR_COLUMN: DOUBLE_TYPE}) == max_year] \
    .astype({YEAR_COLUMN: DOUBLE_TYPE}) \
    .astype({YEAR_COLUMN: INT_TYPE}) \
    .sort_values(by=NAME_COLUMN, ascending=True) \
    .drop(columns=DROP_COLUMNS) \
    .head(5)

print(
    tabulate(
        oldest,
        HEADERS,
        tablefmt="pretty",
        stralign="left"
    )
)

# My Favorite Games Top 5
top = games[games.name.isin(FAVORITE_GAMES)] \
    .astype({YEAR_COLUMN: DOUBLE_TYPE}) \
    .astype({YEAR_COLUMN: INT_TYPE}) \
    .sort_values(by=YEAR_COLUMN, ascending=True) \
    .drop_duplicates(subset=[NAME_COLUMN]) \
    .drop(columns=DROP_TOP5_COLUMNS)

print(
    tabulate(
        top,
        headers=TOP5_COLUMNS,
        tablefmt="pretty",
        stralign="left"
    )
)

# Write output DataFrame (parquet, csv, json)
write(PARQUET, souls)
