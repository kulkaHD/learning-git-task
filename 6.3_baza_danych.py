
from sqlalchemy import create_engine, MetaData, Integer, String, Table, Column

engine = create_engine('sqlite:///clean_stations.db')

meta = MetaData()

stations = Table(
    'clean_stations', meta,
    Column('id', Integer, primary_key=True),
    Column('station', String),
    Column('latitude', Integer),
    Column('longitude', Integer),
    Column('elevation', Integer),
    Column('name', String),
    Column('country', String),
    Column('state', String),
    )

meta.create_all(engine)

ins = stations.insert()
conn = engine.connect()

conn.execute(ins, [
    {'station' : 'USC00519397', 'latitude' : 21.2716, 'longitude' : -157.8168, 'elevation' : 3.0, 'name' : 'WAIKIKI 717.2', 'country' : 'US', 'state' : 'HI'},
    {'station' : 'USC00513117', 'latitude' : 21.4234, 'longitude' : -157.8015, 'elevation' : 14.6, 'name' : 'KANEOHE 838.1', 'country' : 'US', 'state' : 'HI'},
    {'station' : 'USC00514830', 'latitude' : 21.5213, 'longitude' : -157.8374, 'elevation' : 7.0, 'name' : 'KUALOA RANCH HEADQUARTERS 886.9', 'country' : 'US', 'state' : 'HI'},
    {'station' : 'USC00518838', 'latitude' : 21.4992, 'longitude' : -158.0111, 'elevation' : 306.6, 'name' : 'UPPER WAHIAWA 874.3', 'country' : 'US', 'state' : 'HI'},
    {'station' : 'USC00519523', 'latitude' : 21.3356, 'longitude' : -157.7114, 'elevation' : 19.5, 'name' : 'WAIMANALO EXPERIMENTAL FARM', 'country' : 'US', 'state' : 'HI'},
    {'station' : 'USC00519281', 'latitude' : 21.4517, 'longitude' : -157.8489, 'elevation' : 32.9, 'name' : 'WAIHEE 837.5', 'country' : 'US', 'state' : 'HI'},
    {'station' : 'USC00511918', 'latitude' : 21.3152, 'longitude' : -157.9992, 'elevation' : 0.9, 'name' : 'HONOLULU OBSERVATORY 702.2', 'country' : 'US', 'state' : 'HI'},
    {'station' : 'USC00516128', 'latitude' : 21.3331, 'longitude' : -157.8025, 'elevation' : 152.4, 'name' : 'MANOA LYON ARBO 785.2', 'country' : 'US', 'state' : 'HI'}
    ])


print (f'''

Odwołanie się do tabeli poprzez wywyołanie

conn.execute("SELECT * FROM clean_stations LIMIT 5").fetchall()

Daje następujące wyniki:
''')

for i in conn.execute("SELECT * FROM clean_stations LIMIT 5").fetchall():
    print (i)


conn.close()
