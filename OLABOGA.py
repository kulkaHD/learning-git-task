from sqlalchemy import create_engine, MetaData, Integer, String, Table, Column
from sqlalchemy.sql import select
from sqlalchemy.dialects import postgresql
import csv

import sqlite3
from sqlite3 import Error


engine = create_engine('sqlite:///czyste_stacje.db')

meta = MetaData()


clean_stations = Table(
    'clean_stations', meta,
    Column('station', String, primary_key = True),
    Column('latitude', Integer),
    Column('longitude', Integer),
    Column('elevation', Integer),
    Column('name', String),
    Column('country', String),
    Column('state', String),
    )

clean_measure = Table(
    'clean_measure', meta,
    Column('id', Integer, primary_key=True),
    Column('station', String),
    Column('date', String),
    Column('precip', Integer),
    Column('tobs', String)
    )


meta.create_all(engine)

# insCS = clean_stations.insert()
# insCM = clean_measure.insert()
conn = engine.connect()

data_clean_stations = []
data_clean_measure = []



with open('clean_stations.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for rowCS in reader:
        data_clean_stations.append(dict(rowCS))

with open('clean_measure.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for rowCM in reader:
        data_clean_measure.append(dict(rowCM))

conn.execute(insCS,data_clean_stations)
conn.execute(insCM,data_clean_measure)


# s = clean_stations.select()
# result = conn.execute(s)
# for row in result:
#     print(row)


s = select(clean_stations)
result = conn.execute(s)
for row in result:
    print(row)
















# s = select([clean_measure.columns.id, 
#             clean_measure.columns.station,
#             clean_measure.columns.date,
#             clean_measure.columns.precip,
#             clean_measure.columns.tobs,
#             clean_stations.columns.latitude,
#             clean_stations.columns.longitude,
#             clean_stations.columns.elevation,
#             clean_stations.columns.name,
#             clean_stations.columns.country,
#             clean_stations.columns.state]).where(clean_measure.columns.station == clean_stations.columns.station)

# sql = str(s.compile(dialect=postgresql.dialect(), compile_kwargs={"literal_binds": True}))

# create_stations = "CREATE TABLE {0} AS {1}".format("stations", sql)

# print(create_stations)

# conn.execute(create_stations)













# print (f'''

# Odwołanie się do tabeli poprzez wywyołanie

# conn.execute("SELECT * FROM clean_stations LIMIT 5").fetchall()

# Daje następujące wyniki:
# ''')

# for i in conn.execute("SELECT * FROM clean_stations LIMIT 5").fetchall():
#     print (i)


conn.close()
