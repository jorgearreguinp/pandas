from tabulate import tabulate
from constants import *
from write import *
import pandas


data = pandas.read_csv(CSV_PATH, header=0)

games = pandas.DataFrame(data)

# Souls Series
souls = games[games.name.isin(SOULS_GAMES)] \
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
    (games.Fantasy == True) &
    (games.Adventure == True) &
    (games.rating.notnull())
    ].astype({YEAR_COLUMN: INT_TYPE})

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
old_year = games.year.min()

oldest = games[games.year == old_year] \
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
    (games.rating.notnull()) &
    (games.votes.notnull())
    ]

max_year = not_nulls.year.max()

oldest = not_nulls[not_nulls.year == max_year] \
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
write(PARQUET, top)
write(CSV, top)
