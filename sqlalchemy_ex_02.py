from sqlalchemy import create_engine, MetaData, Integer, String, Table, Column
from sqlalchemy.sql import select

engine = create_engine('sqlite:///database.db')

meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String),
   Column('lastname', String),)

meta.create_all(engine)
print(engine.table_names())

ins = students.insert()
# print(str(ins))

# print(ins.compile().params)


# ins = students.insert().values(name='Zuzia', lastname='Tolowska')

conn = engine.connect()
# result = conn.execute(ins)
conn.execute(ins, [
   {'name': 'John', 'lastname': 'Cleese'},
   {'name': 'Graham', 'lastname': 'Chapman'},
])



# meta = MetaData()
# students = Table(
#    'students', meta,
#    Column('id', Integer, primary_key=True),
#    Column('name', String),
#    Column('lastname', String),
# )

conn = engine.connect()


# s = students.select().where(students.c.id > 2)
# result = conn.execute(s)

# for row in result:
#    print(row)


# nie dziala:
s = select(students)
result = conn.execute(s)


for row in result:
    print(row)