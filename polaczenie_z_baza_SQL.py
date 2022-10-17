import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
   specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except sqlite3.Error as e:
       print(e)
   return conn

def create_connection_in_memory():
   """ create a database connection to a SQLite database """
   conn = None
   try:
       conn = sqlite3.connect(":memory:")
       print(f"Connected, sqlite version: {sqlite3.version}")
   except Error as e:
       print(e)
   finally:
       if conn:
           conn.close()

# def add_project(conn, projekt):
#    """
#    Create a new project into the projects table
#    :param conn:
#    :param projekt:
#    :return: project id
#    """
#    sql = '''INSERT INTO projects(nazwa, start_date, end_date)
#              VALUES(?,?,?)'''
#    cur = conn.cursor()
#    cur.execute(sql, projekt)
#    conn.commit()
#    return cur.lastrowid

# def add_task(conn, task):
#    """
#    Create a new task into the tasks table
#    :param conn:
#    :param task:
#    :return: task id
#    """
#    sql = '''INSERT INTO tasks(projekt_id, nazwa, opis, status, start_date, end_date)
#              VALUES(?,?,?,?,?,?)'''
#    cur = conn.cursor()
#    cur.execute(sql, task)
#    conn.commit()
#    return cur.lastrowid

# def select_all(conn, table):
#    """
#    Query all rows in the table
#    :param conn: the Connection object
#    :return:
#    """
#    cur = conn.cursor()
#    cur.execute(f"SELECT * FROM {table}")
#    rows = cur.fetchall()

#    return rows

# def select_where(conn, table, **query):
#    """
#    Query tasks from table with data from **query dict
#    :param conn: the Connection object
#    :param table: table name
#    :param query: dict of attributes and values
#    :return:
#    """
#    cur = conn.cursor()
#    qs = []
#    values = ()
#    for k, v in query.items():
#        qs.append(f"{k}=?")
#        values += (v,)
#    q = " AND ".join(qs)
#    cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
#    rows = cur.fetchall()
#    return rows

# def update(conn, table, id, **kwargs):
#    """
#    update status, begin_date, and end date of a task
#    :param conn:
#    :param table: table name
#    :param id: row id
#    :return:
#    """
#    parameters = [f"{k} = ?" for k in kwargs]
#    parameters = ", ".join(parameters)
#    values = tuple(v for v in kwargs.values())
#    values += (id, )

#    sql = f''' UPDATE {table}
#              SET {parameters}
#              WHERE id = ?'''
#    try:
#        cur = conn.cursor()
#        cur.execute(sql, values)
#        conn.commit()
#        print("OK")
#    except sqlite3.OperationalError as e:
#        print(e)

# def delete_where(conn, table, **kwargs):
#    """
#    Delete from table where attributes from
#    :param conn:  Connection to the SQLite database
#    :param table: table name
#    :param kwargs: dict of attributes and values
#    :return:
#    """
#    qs = []
#    values = tuple()
#    for k, v in kwargs.items():
#        qs.append(f"{k}=?")
#        values += (v,)
#    q = " AND ".join(qs)

#    sql = f'DELETE FROM {table} WHERE {q}'
#    cur = conn.cursor()
#    cur.execute(sql, values)
#    conn.commit()
#    print("Deleted")

# def delete_all(conn, table):
#    """
#    Delete all rows from table
#    :param conn: Connection to the SQLite database
#    :param table: table name
#    :return:
#    """
#    sql = f'DELETE FROM {table}'
#    cur = conn.cursor()
#    cur.execute(sql)
#    conn.commit()
#    print("Deleted")


if __name__ == "__main__":
    # projekt = ("Powtórka z polskiego", "2020-05-11 00:00:00", "2020-05-13 00:00:00")

    # conn = create_connection("clean_stations.db")
    # pr_id = add_project(conn, projekt)

    # task = (
    #     pr_id,
    #     "Czasowniki regularne",
    #     "Zapamiętaj czasowniki ze strony 30",
    #     "ended",
    #     "2020-05-11 12:00:00",
    #     "2020-05-11 15:00:00")

    # task_id = add_task(conn, task)

    # print(pr_id, task_id)
    # conn.commit()

    conn = create_connection("clean_stations.db")
    # cur = conn.cursor()
    # cur.execute("SELECT * FROM tasks")
    # rows = cur.fetchall()
    # print(rows)
    # print(cur.fetchone())
    # print(cur.fetchone())
    # print(cur.fetchone())
    print(conn.execute("SELECT * FROM clean_stations LIMIT 2").fetchall())

    # # conn = create_connection("clean_stations.db")
    # print(select_all(conn, "projects"))
    # print(select_all(conn, "tasks"))
    # print(select_where(conn, "tasks", projekt_id=1))
    # print(select_where(conn, "tasks", status = "ended"))
    # # conn = create_connection("clean_stations.db")
    # update(conn, "tasks", 2, status="ended")
    # update(conn, "tasks", 3, status="started")
    # conn.close()
    # conn = create_connection("clean_stations.db")
    # delete_where(conn, "tasks", id=3)
    # # delete_all(conn, "tasks")